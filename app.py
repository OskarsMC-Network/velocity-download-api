from flask import Flask, jsonify, redirect, request
from flask_caching import Cache

import data_fetch

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

cache_time = 120  # 2 Minutes


@app.route('/')
@cache.cached(timeout=cache_time)
def index():
    fetcher = data_fetch.VelocityVersionFetcher()
    return jsonify(
        versions=fetcher.versions,
        latest_version=fetcher.latest_version,
        latest_release=fetcher.latest_release,
        stable_versions=fetcher.stable_versions,
        error=fetcher.errored
    )


@app.route('/version/<version>/')
@cache.cached(timeout=cache_time)
def specific_version_meta(version: str):
    version_object = data_fetch.get_version(version)

    return jsonify({
        "version": version_object.version,
        "exists": version_object.real,
        "snapshot": version_object.snapshot,
        "download": {
            "url": version_object.url,
            "name": version_object.relative_url,
            "checksum": {
                "sha512": version_object.velocity_file_sha512,
                "sha256": version_object.velocity_file_sha256,
                "sha1": version_object.velocity_file_sha1,
                "md5": version_object.velocity_file_md5
            }
        }
    })


@app.route('/version/<version>/download/')
@cache.cached(timeout=cache_time)
def specific_version_download(version: str):
    version_object = data_fetch.get_version(version)

    return redirect(version_object.url)


if __name__ == '__main__':
    app.run()

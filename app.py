from flask import Flask, jsonify, redirect
from flask_caching import Cache

import data_fetch

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cache.init_app(app)


@app.route('/')
@cache.cached(timeout=120)  # 2 minute cache should be fine
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
def specific_version_meta(version: str):
    return redirect(data_fetch.VelocityDownloadFetcher(version, extension=".module").url, 301)


@app.route('/version/<version>/download')
def specific_version_download(version: str):
    return redirect(data_fetch.VelocityDownloadFetcher(version).url, 301)


@app.route("/snapshot-error/")
def snapshot_error():
    return jsonify(
        error=True,
        message="SNAPSHOT versions are currently not supported."
    )


if __name__ == '__main__':
    app.run()

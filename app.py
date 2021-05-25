from flask import Flask, jsonify
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


if __name__ == '__main__':
    app.run()

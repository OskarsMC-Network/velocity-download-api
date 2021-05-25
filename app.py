from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import data_fetch

fetcher = data_fetch.VelocityVersionFetcher()

scheduler = BackgroundScheduler()
scheduler.add_job(fetcher.fetch_data, "interval", minutes=1)
scheduler.start()

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(
        versions=fetcher.versions,
        latest_version=fetcher.latest_version,
        latest_release=fetcher.latest_release,
        stable_versions=fetcher.stable_versions
    )


if __name__ == '__main__':
    app.run()

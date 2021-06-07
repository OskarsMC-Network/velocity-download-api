# velocity-download-api
Web API for velocity downloads written in python.

# Example API Response
```json
{
  "error": false,
  "latest_release": "1.1.6",
  "latest_version": "4.0.0-SNAPSHOT",
  "stable_versions": [
    "1.1.0",
    "1.1.1",
    "1.1.2",
    "1.1.3",
    "1.1.4",
    "1.1.5",
    "1.1.6"
  ],
  "versions": [
    "1.1.0-SNAPSHOT",
    "1.1.0",
    "1.1.1-SNAPSHOT",
    "1.1.1",
    "1.1.2-SNAPSHOT",
    "1.1.2",
    "1.1.3-SNAPSHOT",
    "1.1.3",
    "1.1.4-SNAPSHOT",
    "1.1.4",
    "1.1.5-SNAPSHOT",
    "1.1.5",
    "1.1.6-SNAPSHOT",
    "1.1.6",
    "1.1.7-SNAPSHOT",
    "2.0.0-SNAPSHOT",
    "3.0.0-SNAPSHOT",
    "4.0.0-SNAPSHOT"
  ]
}
```

# Deploying
##### Cloning the project
```
git clone https://github.com/OskarsMC-Network/velocity-download-api.git
cd velocity-download-api
```
##### Setting up the project (development)
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements
python3 app.py
```
##### Setting up the project (deployment)
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements
pip3 install gunicorn
# Deploys the application to 0.0.0.0:5000
# put this behind nginx for ssl, etc
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

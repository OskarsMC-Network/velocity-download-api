# velocity-download-api
Web API for velocity downloads written in python.

# API Endpoints
Base URL: https://velocity-download-api.herokuapp.com/
<details close>
<summary>/</summary>

GET `/`
```json
{
  "error": false,
  "latest_release": "3.0.0",
  "latest_version": "4.0.0-SNAPSHOT",
  "stable_versions": [
    "1.1.",
    "1.1.0",
    "1.1.1",
    "1.1.2",
    "1.1.3",
    "1.1.4",
    "1.1.5",
    "1.1.6",
    "1.1.7",
    "1.1.8",
    "1.1.9",
    "3.0.0"
  ],
  "versions": [
    "1.1.",
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
    "1.1.7",
    "1.1.8-SNAPSHOT",
    "1.1.8",
    "1.1.9-SNAPSHOT",
    "1.1.9",
    "1.1.10-SNAPSHOT",
    "2.0.0-SNAPSHOT",
    "3.0.0-SNAPSHOT",
    "3.0.0",
    "3.0.1-SNAPSHOT",
    "4.0.0-SNAPSHOT"
  ]
}
```
</details>
<details close>
<summary>/version/{version}/</summary>

GET `/version/3.0.0/`
```json
{
  "download": {
    "checksum": {
      "md5": "55c20c0fdd74ae4a00af328a74f82724",
      "sha1": "315ba63c9bee028234800f1b1317a503b96e7159",
      "sha256": "2479f6915b43c63145f5b33d5c15eec491d60e31cccc685f4175afea7cc1b40c",
      "sha512": "3dccfafa52a7972f7430522863f06e3544e41f770ee2ff5fde0c0c8afac343bcb87d9b2253d0ebbda9ac779eda72e0d8f1b9c4550ba5f2434d487ab957c00372"
    },
    "name": "velocity-native-3.0.0.jar",
    "url": "https://nexus.velocitypowered.com/repository/maven-public/com/velocitypowered/velocity-native/3.0.0/velocity-native-3.0.0.jar"
  },
  "exists": true,
  "snapshot": false,
  "version": "3.0.0"
}
```
</details>
<details close>
<summary>/version/{version}/download/</summary>

GET `/version/3.0.0/download/`

Redirects to: 
```text
https://nexus.velocitypowered.com/repository/maven-public/com/velocitypowered/velocity-native/3.0.0/velocity-native-3.0.0.jar
```

</details>

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

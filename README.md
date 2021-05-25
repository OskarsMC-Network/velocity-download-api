# velocity-download-api
Web API for velocity downloads written in python.

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
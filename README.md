flask - microblog full stack webapp

$ mkdir microblog
$ cd microblog

$ python3 -m venv venv

$ virtualenv venv

$ source venv/bin/activate
(venv) $ _

(venv) $ pip install flask

(venv) $ pip install python-dotenv
  Then you can just write the environment variable name and value in a .flaskenv file in the top-level directory of the project:
  .flaskenv: Environment variables for flask command
      FLASK_APP=microblog.py

(venv) $ pip install flask-wtf

(venv) $ pip install flask-sqlalchemy

(venv) $ pip install flask-migrate

(venv) $ pip install flask-login






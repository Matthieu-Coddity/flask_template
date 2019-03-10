## **Provide a simple Python Flask web app with DB**

**library used:**

 flask
 - flask-script
 - SQLAlchemy
 
**Installation**

1- clone the project

2- $cd flask_template

3- create a virtual env : `$python3 -m venv env`

4- activate the virtual env: `$source env/bin/activate`

5- upgrade pip : `$pip install --upgrade pip`

6- install packages: `$pip install -r requirements.txt`

7- set the env variable for security: `$export "SECRET_KEY"="your_secret_passphrase"`

7bis- set the env variable for dev or production: `$export "APP_SETTINGS"="dev_or_prod"` (dev by default)

7ter- set the env variable for db if prod: `$export "DATABASE"="database"`

8- init the db: `$python3 manage.py db init`

9- migrate the db: `$python3 manage.py db migrate`

10- upgrade the db: `$python3 manage.py db upgrade`

11- run the server: `$python3 manage.py runserver`

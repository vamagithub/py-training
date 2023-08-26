# Run the codes

Firstly, install the required packages.

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Create database:
```
flask db init
flask db migrate
flask db upgrade
```

Run the flask app:
```
export FLASK_APP=student.py
flask run
```

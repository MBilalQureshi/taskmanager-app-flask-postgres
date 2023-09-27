# __init__.py will make sure to initialize our taskmanager application as a
# package, allowing us to use our own imports, as well as any standard imports.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)

# The reason this is being imported last, is because the 'routes' file, that
# we're about to create, will rely on using both the 'app' and 'db' variables
# defined above.

from taskmanager import routes  # noqa

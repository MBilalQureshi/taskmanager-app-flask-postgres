from flask import render_template
from taskmanager import app, db
# At the top of the routes, we need to import these classes in order to generate our database next.
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("base.html")

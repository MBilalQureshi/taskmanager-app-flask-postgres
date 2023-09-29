from flask import render_template
from taskmanager import app, db
# At the top of the routes, we need to import these classes in order to
# generate our database next.
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# we need to include a list of the two methods "GET" and "POST", since we will
# be submitting a form to the database.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    return render_template("add_category.html")
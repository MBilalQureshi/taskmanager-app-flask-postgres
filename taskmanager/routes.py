from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# At the top of the routes, we need to import these classes in order to
# generate our database next.
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


# we need to include a list of the two methods "GET" and "POST", since we will
# be submitting a form to the database.
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # IMPORTANT: In realworld add defensive programming to prevent brute force attacks along with error handling
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    # 1 Initially get method will occur and start below code as return, behave as else
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
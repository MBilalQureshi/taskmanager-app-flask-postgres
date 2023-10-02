from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# At the top of the routes, we need to import these classes in order to
# generate our database next.
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


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


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=request.form.get(True if request.form.get("is_urgent")
                                       else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )     
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)


# @app.route("/task")
# def task():
    
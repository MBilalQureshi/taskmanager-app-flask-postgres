from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # Since we aren't using db.Column, this will not be visible on the database itself like
    # the other columns, as it's just to reference the one-to-many relationship.

    # Then, we need to use something called 'backref' which establishes a bidirectional relationship
    # in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
    # It needs to back-reference itself, but in quotes and lowercase, so backref="category".
    # Also, it needs to have the 'cascade' parameter set to 'all, delete' which means it will find
    # all related tasks and delete them.
    # The last parameter here is lazy=True, which means that when we query the database for
    # categories, it can simultaneously identify any task linked to the categories.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string, another
        # function is def __str__(self) that behave quite similar
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # BELOW if you need to include time on your database, then db.DateTime or
    # db.Time are suitable.
    due_date = db.Column(db.Date, nullable=False)
    # BELOW we are going to apply something called ondelete="CASCADE" for this foreign key.
    # Since each of our tasks need a category selected, this is what's known as a one-to-many relationship.
    # One category can be applied to many different tasks, but one task cannot have many categories.

    # "CASCADE", Later, we decide to delete 1 of those categories, so any of the 5 tasks that have this specific
    # category linked as a foreign key, will throw an error, since this ID is no longer available.
    # This is where the ondelete="CASCADE" comes into play, and essentially means that once
    # a category is deleted, it will perform a cascading effect and also delete any task linked to it.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string, another
        # function is def __str__(self) that behave quite similar
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"
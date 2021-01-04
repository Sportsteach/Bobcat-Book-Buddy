from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class NewBook(db.Model):
    """User Model."""

    __tablename__ = "new_books"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    google_id = db.Column(db.String)
    title = db.Column(db.String)
    author = db.Column(db.String)
    thumbs_up = db.Column(db.Integer)
    isbn = db.Column(db.Integer)


class Inventory(db.Model):
    """Inventory model."""

    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    author = db.Column(db.String)

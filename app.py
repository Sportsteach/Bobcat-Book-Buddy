from book_shielf_func import book_shelf_func
from details_func import details_func
from popular import popular_func
from similar_books import similar_books_func
from flask import Flask, request, jsonify, render_template, redirect, session, flash
from models import db, connect_db, NewBook, Inventory
import requests
import re
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'postgresql:///library')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "youwillneverknow3124")

connect_db(app)

"""app"""


@app.route("/")
def homepage():
    """Show homepage."""
    popular_list = popular_func()
    return render_template("index.html", popular_list=popular_list)


@app.route('/book_to_add')
def add_book():
    """Where users make a book recommendation"""
    return render_template('book_to_add.html')


@ app.route('/book_search')
def search_book_post():
    """route for the search function"""
    book_list = book_shelf_func(request.args['search'])
    return render_template('book_search.html', book_list=book_list)


@ app.route('/book_details/<int:id>')
def book_details(id):
    """route to show specific book details"""
    book_details = details_func(id)
    similar_books = similar_books_func(id)
    long_title = (book_details[0].get("").get('title'))
    b_title = re.sub(r'\([^)]*\)', '', long_title)

    b_author = (book_details[0].get("").get('author'))

    description = (book_details[0].get("").get('description'))
    cleanr = re.compile('<.*?>')
    b_description = re.sub(cleanr, '', description)
    short_title = b_title[:(len(b_title)-1)]

    title = (f'%1s' % short_title)
    author = (f'%.1s' % b_author)
    title_search = "%{}%".format(title)
    author_search = "%{}%".format(author)

    the_title = Inventory.query.filter(Inventory.title.ilike(title_search)). \
        filter(Inventory.author.ilike(author_search)).all()

    the_book = NewBook.query.filter_by(gb_num=id).first()
    return render_template('book_details.html', book_details=book_details, similar_books=similar_books, the_title=the_title, b_title=b_title, b_description=b_description, the_book=the_book)


@ app.route('/book_details/<int:id>', methods=["POST"])
def create_book(id):
    """Add book to database"""

    gb_num = request.form["id"]
    title = request.form["title"]
    author = request.form["author"]
    thumbs_up = request.form["thumbs_up"]
    isbn = request.form["isbn"]

    new_book = NewBook(gb_num=gb_num, title=title,
                       author=author, thumbs_up=thumbs_up, isbn=isbn)
    flash('Thank you for add to suggestion!')
    db.session.add(new_book)
    db.session.commit()

    return redirect(f'/book_details/{gb_num}')


@ app.route('/<int:id>/edit', methods=["POST"])
def edit_book(id):
    """edit book to database"""
    flash('Thank you, Thumbs Up Added!')
    the_book = NewBook.query.get_or_404(id)
    the_book.gb_num = request.form["id"]
    the_book.title = request.form["title"]
    the_book.author = request.form["author"]
    the_book.thumbs_up = request.form["thumbs_up"]
    the_book.isbn = request.form["isbn"]

    db.session.add(the_book)
    db.session.commit()

    return redirect(f'/book_details/{the_book.gb_num}')


@ app.route('/popular_books')
def popular_books():
    """route for returning popular childrens books"""
    popular_list = popular_func()
    long_title = (popular_list[0].get("").get('title'))
    b_title = re.sub(r'\([^)]*\)', '', long_title)

    return render_template('popular_books.html', popular_list=popular_list, b_title=b_title)

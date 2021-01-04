from flask import Flask, render_template, request
import requests


def details_func(book_id):
    url = f'https://www.googleapis.com/books/v1/volumes/{book_id}'
    response = requests.get(url)
    works = response.json()
    book_details = []
    book_tags = ""
    id_tag = works['id']

    try:
        id_tag = works['id']
    except KeyError:
        id_tag = "KYIHM5unh3UC"
    try:
        title_tag = works['volumeInfo']['title']
    except KeyError:
        title_tag = "No Title Avalible"
    try:
        author_tag = works['volumeInfo']['authors'][0]
    except KeyError:
        author_tag = ""
    try:
        image_tag = works['volumeInfo']['imageLinks']['smallThumbnail']
    except KeyError:
        image_tag = 'https://i.imgur.com/J5LVHEL.jpg'
    try:
        average_tag = works['volumeInfo']['averageRating']
    except KeyError:
        average_tag = 0
    try:
        description_tag = works["volumeInfo"]["description"]
    except KeyError:
        description_tag = ""
    try:
        isbn_tag = works["volumeInfo"]["industryIdentifiers"][0]['identifier']
    except KeyError:
        isbn_tag = 000000
    try:
        category_tag = works["volumeInfo"]['categories'][0]
    except KeyError:
        category_tag = "Juvenile"

    outer_book = {
        book_tags: {
            "id": id_tag,
            "title": title_tag,
            "author": author_tag,
            "image": image_tag,
            "rating": average_tag,
            "description": description_tag,
            "isbn": isbn_tag,
            "category": category_tag
        }
    }
    book_details.append(outer_book)
    return book_details

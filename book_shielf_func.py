from flask import Flask, render_template, request
import requests


def book_shelf_func(search_function):
    url = f'https://www.googleapis.com/books/v1/volumes?q={search_function}&maxResults=16&maxAllowedMaturityRating=not-mature&orderBy=relevance'
    response = requests.get(url)
    r = response.json()
    items = r['items']

    book_arr = []
    book_tags = ""

    for item in items:
        try:
            id_tag = item['id']
        except KeyError:
            id_tag = "KYIHM5unh3UC"
        try:
            title_tag = item['volumeInfo']['title']
        except KeyError:
            title_tag = "No Title Avalible"
        try:
            author_tag = item['volumeInfo']['authors'][0]
        except KeyError:
            author_tag = ""
        try:
            image_tag = item['volumeInfo']['imageLinks']['smallThumbnail']
        except KeyError:
            image_tag = 'https://i.imgur.com/J5LVHEL.jpg'
        try:
            average_tag = item['volumeInfo']['averageRating']
        except KeyError:
            average_tag = 0
        try:
            description_tag = item["volumeInfo"]["description"]
        except KeyError:
            description_tag = ""
        try:
            isbn_tag = item["volumeInfo"]["industryIdentifiers"][0]['identifier']
        except KeyError:
            isbn_tag = 000000
        try:
            category_tag = item["volumeInfo"]['categories'][0]
        except KeyError:
            category_tag = "Juvenile"
        outer_book = {
            book_tags: {
                "id": id_tag,
                "title": title_tag,
                "author": author_tag,
                "image": image_tag,
                "rating": average_tag
            }
        }
        book_arr.append(outer_book)

    return book_arr

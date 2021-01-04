from flask import Flask, render_template, request
import requests
import random


def popular_func():
    startIdx = random.randint(0, 15)
    url = f'https://www.googleapis.com/books/v1/users/105693815034359728209/bookshelves/1001/volumes?maxResults=8&startIndex={startIdx}'
    response = requests.get(url)
    r = response.json()
    items = r['items']

    startIdx2 = random.randint(23, 46)
    url2 = f'https://www.googleapis.com/books/v1/users/105693815034359728209/bookshelves/1001/volumes?maxResults=8&startIndex={startIdx2}'
    response2 = requests.get(url2)
    r2 = response2.json()
    items2 = r2['items']

    pop_books = []
    pop_tags = ""
    for secondBooks in items2:
        try:
            id_tag = secondBooks['id']
        except KeyError:
            id_tag = "KYIHM5unh3UC"
        try:
            title_tag = secondBooks['volumeInfo']['title']
        except KeyError:
            title_tag = "No Title Avalible"
        try:
            author_tag = secondBooks['volumeInfo']['authors'][0]
        except KeyError:
            author_tag = ""
        try:
            image_tag = secondBooks['volumeInfo']['imageLinks']['smallThumbnail']
        except KeyError:
            image_tag = 'https://i.imgur.com/J5LVHEL.jpg'
        try:
            average_tag = secondBooks['volumeInfo']['averageRating']
        except KeyError:
            average_tag = 0
        try:
            description_tag = secondBooks["volumeInfo"]["description"]
        except KeyError:
            description_tag = ""
        try:
            isbn_tag = secondBooks["volumeInfo"]["industryIdentifiers"][0]['identifier']
        except KeyError:
            isbn_tag = 000000
        try:
            category_tag = secondBooks["volumeInfo"]['categories'][0]
        except KeyError:
            category_tag = "Juvenile"

        outer_pop = {
            pop_tags: {
                "title": title_tag,
                "author": author_tag,
                "image": image_tag,
                "rating": average_tag,
                "id": id_tag
            }
        }
        pop_books.append(outer_pop)
    for firstBooks in items:
        try:
            id_tag = firstBooks['id']
        except KeyError:
            id_tag = "KYIHM5unh3UC"
        try:
            title_tag = firstBooks['volumeInfo']['title']
        except KeyError:
            title_tag = "No Title Avalible"
        try:
            author_tag = firstBooks['volumeInfo']['authors'][0]
        except KeyError:
            author_tag = ""
        try:
            image_tag = firstBooks['volumeInfo']['imageLinks']['smallThumbnail']
        except KeyError:
            image_tag = 'https://i.imgur.com/J5LVHEL.jpg'
        try:
            average_tag = firstBooks['volumeInfo']['averageRating']
        except KeyError:
            average_tag = 0
        try:
            description_tag = firstBooks["volumeInfo"]["description"]
        except KeyError:
            description_tag = ""
        try:
            isbn_tag = firstBooks["volumeInfo"]["industryIdentifiers"][0]['identifier']
        except KeyError:
            isbn_tag = 000000
        try:
            category_tag = firstBooks["volumeInfo"]['categories'][0]
        except KeyError:
            category_tag = "Juvenile"

        outer_pop = {
            pop_tags: {
                "title": title_tag,
                "author": author_tag,
                "image": image_tag,
                "rating": average_tag,
                "id": id_tag
            }
        }
        pop_books.append(outer_pop)
        random.shuffle(pop_books)
    return pop_books

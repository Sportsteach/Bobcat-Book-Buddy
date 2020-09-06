from urllib.request import Request, urlopen
import ssl
import random
import xml.dom.minidom
from secrets import key


def popular_func():
    req = Request(
        f'https://www.goodreads.com/review/list/120321158.xml?key={key}')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    r = urlopen(req, context=ctx)
    rString = r.read().decode("utf-8")

    xmlparse = xml.dom.minidom.parseString(rString)
    prettyxml = xmlparse.toprettyxml()

    populars = xmlparse.getElementsByTagName('book')
    pop_books = []
    pop_tags = ""
    for popular in populars:
        title_tag = popular.getElementsByTagName('title')
        author_tag = popular.getElementsByTagName('name')
        image_tag = popular.getElementsByTagName('image_url')
        average_tag = popular.getElementsByTagName('average_rating')
        id_tag = popular.getElementsByTagName('id')
        outer_pop = {
            pop_tags: {
                "title": (title_tag[0].firstChild.data),
                "author": (author_tag[0].firstChild.data),
                "image": (image_tag[0].firstChild.data),
                "rating": (average_tag[0].firstChild.data),
                "id": (id_tag[0].firstChild.data)
            }
        }
        pop_books.append(outer_pop)
        random.shuffle(pop_books)
    r.close()
    return pop_books

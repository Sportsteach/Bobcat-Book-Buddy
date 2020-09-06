from urllib.request import Request, urlopen
import ssl
import xml.dom.minidom
from secrets import key


def book_shelf_func(search_function):

    book = search_function.replace(" ", "+")

    req = Request(
        f'https://www.goodreads.com/search/index.xml?key={key}&q={book}')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    r = urlopen(req, context=ctx)
    rString = r.read().decode("utf-8")

    xmlparse = xml.dom.minidom.parseString(rString)
    prettyxml = xmlparse.toprettyxml()

    works = xmlparse.getElementsByTagName('work')
    book_arr = []
    book_tags = ""
    for work in works:
        title_tag = work.getElementsByTagName('title')
        author_tag = work.getElementsByTagName('name')
        image_tag = work.getElementsByTagName('image_url')
        average_tag = work.getElementsByTagName('average_rating')
        id_tag = work.getElementsByTagName('id')
        outer_book = {
            book_tags: {
                "title": (title_tag[0].firstChild.data),
                "author": (author_tag[0].firstChild.data),
                "image": (image_tag[0].firstChild.data),
                "rating": (average_tag[0].firstChild.data),
                "id": (id_tag[1].firstChild.data)
            }
        }
        book_arr.append(outer_book)

    r.close()
    return book_arr

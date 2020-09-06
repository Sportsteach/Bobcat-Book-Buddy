from urllib.request import Request, urlopen
import ssl
import xml.dom.minidom
from secrets import key


def details_func(book_id):
    book = book_id
    req = Request(
        f'https://www.goodreads.com/book/show/{book}.xml?key={key}')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    r = urlopen(req, context=ctx)
    rString = r.read().decode("utf-8")

    xmlparse = xml.dom.minidom.parseString(rString)
    prettyxml = xmlparse.toprettyxml()

    works = xmlparse.getElementsByTagName('GoodreadsResponse')
    book_details = []
    book_tags = ""
    for work in works:
        id_tag = work.getElementsByTagName('id')
        title_tag = work.getElementsByTagName('title')
        description_tag = work.getElementsByTagName('description')
        if description_tag[0].firstChild == None:
            des = 'Sorry no book summary.'

        else:
            des = (description_tag[0].childNodes[0].data)
        author_tag = work.getElementsByTagName('name')
        image_tag = work.getElementsByTagName('image_url')
        average_tag = work.getElementsByTagName('average_rating')
        isbn_tag = work.getElementsByTagName('isbn')
        if isbn_tag[0].firstChild == None:
            tag = "Missing"
        else:
            tag = (isbn_tag[0].firstChild.data)

        outer_book = {
            book_tags: {
                "id": (id_tag[0].firstChild.data),
                "title": (title_tag[0].firstChild.data),
                "author": (author_tag[0].firstChild.data),
                "image": (image_tag[0].firstChild.data),
                "rating": (average_tag[0].firstChild.data),
                "description": des,
                "isbn": tag
            }
        }
        book_details.append(outer_book)
    r.close()
    return book_details

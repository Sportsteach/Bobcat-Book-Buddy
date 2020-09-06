from urllib.request import Request, urlopen
import ssl
import xml.dom.minidom
from secrets import key


def similar_books_func(book_id):
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

    similars = xmlparse.getElementsByTagName('book')
    sim_books = []
    sim_tags = ""
    for sim in similars:
        title_tag = sim.getElementsByTagName('title')
        author_tag = sim.getElementsByTagName('name')
        image_tag = sim.getElementsByTagName('image_url')
        average_tag = sim.getElementsByTagName('average_rating')
        id_tag = sim.getElementsByTagName('id')
        outer_sim = {
            sim_tags: {
                "title": (title_tag[0].firstChild.data),
                "author": (author_tag[0].firstChild.data),
                "image": (image_tag[0].firstChild.data),
                "rating": (average_tag[0].firstChild.data),
                "id": (id_tag[0].firstChild.data)
            }
        }
        sim_books.append(outer_sim)
    r.close()
    return sim_books

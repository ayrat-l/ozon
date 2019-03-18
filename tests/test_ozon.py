from App.lib import create_book, add_book


def test_create_book():
    books = {'title': 'Война и Мир', 'author': 'Лев Толстой', 'price': 500, 'tags': ['#война', '#любовь', '#толстой'], 'availability': True}

    result = create_book('Война и Мир', 'Лев Толстой', 500, ['#война', '#любовь', '#толстой'], True)

    assert books == result

def test_add_book():
    books = []
    book = create_book('Война и Мир', 'Лев Толстой', 500, ['#война', '#любовь', '#толстой'], True)
    add_book(books, book)
    assert len(books) != 0
    assert book in books
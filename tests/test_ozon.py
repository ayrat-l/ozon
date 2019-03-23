from app.lib import create_book, add_book, search_books, search_by_tags, search_full, search_by_price


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

def test_search_books():
    books = [{'title': 'Война и Мир', 'author': 'Лев Толстой', 'price': 500, 'tags': ['#война', '#любовь', '#толстой'], 'availability': True}]
    result = search_books(books, 'война')
    assert result == books

def test_search_by_tags():
    books = [{'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 300, 'tags': ['#поезд', '#любовь', '#толстой'], 'availability': False}]
    result = search_by_tags(books, '#поезд')
    assert result == books

def test_search_full():
    books = [{'title': 'Палата 6', 'author': 'Антон Чехов', 'price': 600, 'tags': ['#больница', '#шесть', '#доктор'], 'availability': True}]
    result = search_full(books, 'палата 6')
    assert result == books

def test_search_by_price():
    books = [{'title': 'Война и Мир', 'author': 'Лев Толстой', 'price': 500, 'tags': ['#война', '#любовь', '#толстой'], 'availability': True}, {'title': 'Анна Каренина', 'author': 'Лев Толстой', 'price': 300, 'tags': ['#поезд', '#любовь', '#толстой'], 'availability': False}]
    result = search_by_price(books, 500)
    assert result == books
from App.lib import create_book

def test_create_book():
    books = {'title': 'Война и Мир', 'author': 'Лев Толстой', 'price': 500, 'tags': ['#война', '#любовь', '#толстой'], 'available': True}

    result = create_book('Война и Мир', 'Лев Толстой', 500, ['#война', '#любовь', '#толстой'], True)

    assert books == result
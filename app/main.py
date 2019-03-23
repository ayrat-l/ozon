from app.lib import create_book, add_book, search_by_tags, search_books, search_full

books = []

# Создание книги
book_war_and_peace = create_book('Война и Мир', 'Лев Толстой', 500, ['#война', '#любовь', '#толстой'], True)
book_anna_karenina = create_book('Анна Каренина', 'Лев Толстой', 300, ['#поезд', '#любовь', '#толстой'], False)
book_chamber6 = create_book('Палата 6', 'Антон Чехов', 600, ['#больница', '#шесть', '#доктор'], True)

# Добавление книги
add_book(books, book_war_and_peace)
add_book(books, book_anna_karenina)
add_book(books, book_chamber6)

# Поиск по тегу
print(search_by_tags(books, '#любовь'))

# Поиск по названию книги
print(search_books(books, 'мир'))

# Поиск по полному совпадению в названии книги
print(search_full(books, 'Война и Мир'))

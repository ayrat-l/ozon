def create_book(title, author, price, tags, availability):
    return {
        'title': title,
        'author': author,
        'price': price,
        'tags': tags,
        'availability': availability
    }

def add_book(container, book):
    container.append(book)

def list_books(container, page, page_size):
    # page_size = 50
    start = (page - 1) * page_size  # для первой страницы стартуем с 0
    finish = start + page_size
    return container[start:finish]

def search_books(container, search):  # search - строка поиска
    search_lowercased = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower():
            result.append(book)
            continue  # не даёт идти дальше на 30 строку

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться, если будем добавлять новые возможности

    return result

#Поиск по тегу
def search_books_tags(container, search):
    search_tag = search.strip().lower()  # 1. search.strip() 2. (результат search.strip()).lower()
    result = []
    for book in container:
        if search_tag in book['tags'].lower():
            result.append(book)
            continue  # не даёт идти дальше на 30 строку

        if search_tag in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться, если будем добавлять новые возможности

    return result

#Поиск по полному совпадению
def search_full(container, search):
    search_lowercased = search.strip().lower()
    result = []
    for book in container:
        if search_lowercased in book['title'].lower() == book['title'].lower():
            result.append(book)
            continue

        if search_lowercased in book['author'].lower():
            result.append(book)
            continue  # пока не нужно, но на будущее пригодиться
    return result
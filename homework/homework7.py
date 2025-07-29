from sqlite3 import connect

connect = connect("books.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fio VARCHAR(100) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title VARCHAR(200) NOT NULL,
        author VARCHAR(200) NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

connect.commit()

def add_user(fio):
    cursor.execute(
        'INSERT INTO users(fio) VALUES(?)',
        (fio,)
    )
    connect.commit()
    print(f"{fio} добавлен")

def add_book(title, author, user_id):
    cursor.execute(
        'INSERT INTO books(title, author, user_id) VALUES (?, ?, ?)',
        (title, author, user_id)
    )
    connect.commit()
    print(f"Книга '{title}' добавлена")

def get_all_books():
    cursor.execute(
        '''
        SELECT books.title, books.author, users.fio
        FROM books JOIN users ON books.user_id = users.id
        '''
    )
    data = cursor.fetchall()
    for row in data:
        print(f"Книга: {row[0]}, Автор: {row[1]}, Читатель: {row[2]}")

def update_book_title(book_id, new_title):
    cursor.execute(
        "UPDATE books SET title = ? WHERE id = ?",
        (new_title, book_id)
    )
    connect.commit()
    print("Название книги обновлено")

def delete_book(book_id):
    cursor.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )
    connect.commit()
    print("Книга удалена")

add_user("Kirito")
add_user("Do ro ro")
add_user("Asuna")

add_book("Гарри Поттер", "Дж. Роулинг", 1)
add_book("Преступление и наказание", "Ф.М. Достоевский", 2)
add_book("Атлант расправил плечи", "Айн Рэнд", 3)
add_book("1984", "Джордж Оруэлл", 1)
add_book("Мастер и Маргарита", "М.А. Булгаков", 2)

get_all_books()



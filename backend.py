import sqlite3
class Database:
    def __init__(self, db):
        db = sqlite3.connect("books.db")
        curs=db.cursor()
        curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year INTEGER,isbn INTEGER)")
        db.commit()
        db.close()

    def insert(self, title, author, year, isbn):
        db = sqlite3.connect("books.db")
        curs = db.cursor()
        curs.execute("INSERT INTO book  VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        db.commit()
        db.close()
    def search(self, title="", author="", year="", isbn=""):
        db = sqlite3.connect("books.db")
        curs = db.cursor()
        curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = curs.fetchall()
        db.close()
        return rows
    def viewAll(self):
        db = sqlite3.connect("books.db")
        curs = db.cursor()
        curs.execute("SELECT * FROM book")
        rows = curs.fetchall()
        db.close()
        return rows
    def delete(self,id):
        db = sqlite3.connect("books.db")
        curs = db.cursor()
        curs.execute("DELETE FROM book WHERE id=?",(id,))
        db.commit()
        db.close()

    def update(self,id, title, author, year, isbn):
        db = sqlite3.connect("books.db")
        curs= db.cursor()
        curs.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        db.commit()
        db.close()

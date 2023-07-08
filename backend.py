import sqlite3
class Database:
    def __init__(self, db):
        self.db = sqlite3.connect("books.db")
        self.curs=self.db.cursor()
        self.curs.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text,year INTEGER,isbn INTEGER)")
        self.db.commit()
        

    def insert(self, title, author, year, isbn):
        self.curs.execute("INSERT INTO book  VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
        self.db.commit()
    def search(self, title="", author="", year="", isbn=""):
        self.curs.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows = self.curs.fetchall()
        self.db.close()
        return rows
    def viewAll(self):
        self.curs.execute("SELECT * FROM book")
        rows = self.curs.fetchall()
        return rows
    def delete(self,id):
        self.curs.execute("DELETE FROM book WHERE id=?",(id,))
        self.db.commit()

    def update(self,id, title, author, year, isbn):
        self.curs.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.db.commit()
       

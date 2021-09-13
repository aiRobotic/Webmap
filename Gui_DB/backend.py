import sqlite3 as db

def connect():
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()

def insert(title ="", author="", year="", isbn=""):
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?,?,?,?)", (title,author, year, isbn))
    con.commit()
    con.close()   

def view():
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book")
    values = cur.fetchall()
    con.close()
    return values  

def search(title ="", author="", year="", isbn=""):
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE (title =? OR author=? OR year =? OR isbn=?)",(title,author,year,isbn))
    values = cur.fetchall()
    con.close()
    return values 

def delete(id):
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE (ID =?)",(id,))
    con.commit()
    con.close()

def update(id,title, author, year, isbn):
    con = db.connect("Books.db")
    cur = con.cursor()
    cur.execute("UPDATE book set title =?, author=?, year =?, isbn=? WHERE ID =?",(title,author, year, isbn, id))
    con.commit()
    con.close() 

connect()
import sqlite3

def connect():
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,Title text, Author text, Year integer, ISBN integer)")
    data.commit()
    data.close()

def Add(Title,Author, Year, ISBN):  #parameters
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(Title, Author, Year, ISBN))
    data.commit()
    data.close()

def view():
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    data.close()
    return rows

def Search(Title="",Author="",Year="",ISBN=""): #parameters
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("SELECT * FROM books WHERE Title =? or Author=? or Year =? or ISBN=?",(Title, Author, Year, ISBN)) #with loop compare all with parameters
    rows = cur.fetchall()
    data.close()
    return rows

def Delete(id):
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id,))
    data.commit()
    data.close()

def Update(id, Title, Author, Year, ISBN):
    data = sqlite3.connect("books.db")
    cur = data.cursor()
    cur.execute("UPDATE books SET Title =?, Author=? ,Year =?, ISBN =? WHERE id=?",(Title, Author, Year, ISBN, id) )
    data.commit()
    data.close()

#connect()
#Add('kar','dit',5954395,12334289)
#print(view())
#print("\n")
#print(search(Year= "2001"))
#Delete(2001)
#print(view())
#pdate(1,'Ro','hit',1995,1289)
#Update(3,"Kill","Delhi", 3567,243244)
#print(view())

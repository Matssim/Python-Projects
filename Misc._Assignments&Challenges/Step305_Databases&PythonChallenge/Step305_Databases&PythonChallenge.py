import sqlite3

def create_db():
    connection = sqlite3.connect('db_test1')
    with connection:
        editor = connection.cursor()
        editor.execute("CREATE TABLE if not exists tbl_entries( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            Name TEXT, \
            Species TEXT, \
            IQ TEXT \
            );")
        connection.commit()
        entries()
        update()
        display()
    connection.close()
    

def entries():
    connection = sqlite3.connect('db_test1')
    editor = connection.cursor()
    editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Jean-Baptiste Zorg', 'Human', '122'))
    editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Korben Dallas', 'Meat Popsicle', '100'))
    editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Ak\'not', 'Mangalore', '-5'))
    connection.commit()
    
def update():
    connection = sqlite3.connect('db_test1')
    editor = connection.cursor()
    editor.execute("""UPDATE tbl_entries SET Species = 'Human' WHERE Name = 'Korben Dallas'""")
    connection.commit()

def display():
    connection = sqlite3.connect('db_test1')
    editor = connection.cursor()
    editor.execute("""SELECT Name,IQ FROM tbl_entries WHERE Species = 'Human'""")
    for row in editor.fetchall():
        print(row)



if __name__ == "__main__":
    create_db()

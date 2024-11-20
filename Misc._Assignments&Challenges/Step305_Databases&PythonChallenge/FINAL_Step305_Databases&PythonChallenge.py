import sqlite3

def create_db():
    connection = sqlite3.connect(':memory:')
    with connection:
        editor = connection.cursor()
        editor.execute("CREATE TABLE if not exists tbl_entries( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            Name TEXT, \
            Species TEXT, \
            IQ TEXT \
            );")
        connection.commit()
        editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Jean-Baptiste Zorg', 'Human', '122'))
        editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Korben Dallas', 'Meat Popsicle', '100'))
        editor.execute("""INSERT INTO tbl_entries (Name,Species,IQ) VALUES (?,?,?)""",('Ak\'not', 'Mangalore', '-5'))
        connection.commit()
        editor.execute("""UPDATE tbl_entries SET Species = 'Human' WHERE Name = 'Korben Dallas'""")
        connection.commit()
        editor.execute("""SELECT Name,IQ FROM tbl_entries WHERE Species = 'Human'""")
        for row in editor.fetchall():
            print(row)
    connection.close()
    

if __name__ == "__main__":
    create_db()

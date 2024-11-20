#import sqlite3

## get personal data from user and insert into a tuple
#firstName = input("Enter your first name: ")
#lastName = input("Enter your last name: ")
#age = int(input("Enter your age: "))
#personData = (firstName, lastName, age)

## execute insert statement fro supplied person data
#with sqlite3.connect('test_database.db') as connection:
#    c = connection.cursor()
#    c.execute("INSERT INTO People VALUES(?, ?, ?)", personData)

#   c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?,
#             (45, 'Luigi', 'Vercotti'))

import sqlite3

peopleValues = (('Ron', 'Obvious', 42), ('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28))

with sqlite3.connect('test_database.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS People")
    c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
    c.executemany("INSERT INTO People VALUES(?, ?, ?)",
                  peopleValues)

##select all first and last name from people over age 30
    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
    for row in c.fetchall():
        print (row)

c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)

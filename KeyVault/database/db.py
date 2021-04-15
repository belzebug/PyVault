import sqlite3
import getpass

connection = sqlite3.connect('/home/' + getpass.getuser() + '/PyVault/database/' + getpass.getuser() + '.db')


def setupDb():
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS keys
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, key text)''')

def readAll():
    cur = connection.cursor()
    res = cur.execute('SELECT * FROM keys')
    return res

def writeKey(name, value):
    cur = connection.cursor()
    Query = "INSERT INTO keys (name, key) VALUES ({name}, {value})"
    QueryF = Query.format(name = "\'" + name + "\'", value = "\'" + value + "\'")
    cur.execute(QueryF)
    connection.commit()



con = sqlite3.connect('example.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE IF NOT EXISTS stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
print(con.execute("SELECT * FROM stocks"))
con.close()
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



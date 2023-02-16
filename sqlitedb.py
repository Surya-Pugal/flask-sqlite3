import sqlite3

conn = sqlite3.connect('users.db',check_same_thread=False)

c = conn.cursor()

#c.execute("CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, city text)")

def insert(data):
    with conn:
        c.execute('INSERT INTO users(name,city) VALUES (?,?)',(data['name'],data['city']))
    
def select():
    with conn:
        c.execute('SELECT * FROM users')
        return c.fetchall()
    
conn.commit()


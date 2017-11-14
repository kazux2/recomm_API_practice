import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor() #create cursor
        self.c.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") #connect to the database. if the database exist, it'll connect. if it doesn't exist, it'll be created.
        self.conn.commit()
        #not closed

    def create_table(self, dbname):
        self.c.execute("INSERT INTO store VALUES ('Apple', 8, 1.5 ) ") # Create table

    def insert(self, item, quantity, price):
        self.c.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

    def view(self):
        self.c.execute("SELECT * From store")
        rows = self.c.fetchall()
        return rows

    def __del__(self):
        self.conn.close()

dbname = "example.db"
db = Database(dbname)
db.create_table(dbname)
db.insert("Orange", 15, 0.75)
print(db.view())









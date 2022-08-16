# Import sqlite3 DB
import sqlite3

# Connecting To Our DB
connection = sqlite3.connect('cars.db')

# Opening Our schema.sql File To Read Code Inside It
with open('schema.sql') as f:
    # Executes The Create Table Code Inside The schema.sql File
    connection.executescript(f.read())

# Creating A Cursor To Our DB So We Can Update It
cur = connection.cursor()

# Inserting Dummy Data To Our DB
cur.execute("INSERT INTO vehicles (manufacturer, model) VALUES (?, ?)",
            ('Nissan', 'GTR')
            )

cur.execute("INSERT INTO vehicles (manufacturer, model) VALUES (?, ?)",
            ('Bugatti', 'Veyron')
            )

# Commiting All Changes Made To DB
connection.commit()

# Closing DB Connection
connection.close()

################## WE NEED TO RUN THIS FILE IN TERMINAL SO IT CREATES OUR DB FILE, SO TO RUN THIS FILE WE WOULD DO 'python init_db.py' ##################

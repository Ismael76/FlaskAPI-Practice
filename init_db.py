import sqlite3

connection = sqlite3.connect('cars.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO vehicles (manufacturer, model) VALUES (?, ?)",
            ('Nissan', 'GTR')
            )

cur.execute("INSERT INTO vehicles (manufacturer, model) VALUES (?, ?)",
            ('Bugatti', 'Veyron')
            )

connection.commit()
connection.close()

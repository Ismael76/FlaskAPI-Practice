import sqlite3


def get_db_connection():
    conn = sqlite3.connect('cars.db')
    conn.row_factory = sqlite3.Row
    return conn


class Vehicles():
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    @staticmethod
    def create(manufacturer, model):
        conn = get_db_connection()
        conn.execute('INSERT INTO vehicles (manufacturer, model) VALUES (?, ?)',
                     (manufacturer, model))
        conn.commit()
        conn.close()

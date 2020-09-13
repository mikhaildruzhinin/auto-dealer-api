import sqlite3

class AutoModel():
    __tablename__ = 'cars'

    def __init__(self, mark, max_speed, distance, handler, stock):
        self.mark = mark
        self.max_speed = max_speed
        self.distance = distance
        self.handler = handler
        self.stock = stock

    def json(self):
        return {'mark': self.mark, 'max_speed': self.max_speed, 'distance': self.distance, 'handler': self.handler, 'stock': self.stock}

    @classmethod
    def search_mark(cls, mark):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = 'SELECT * FROM {} WHERE mark=?'.format(cls.__tablename__)
        row = cur.execute(select_query, (mark,)).fetchone()
        conn.close()
        if row:
            return {'mark': row[0], 'max_speed': row[1], 'distance': row[2], 'handler': row[3], 'stock': row[4]}

    @classmethod
    def get_all(cls):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        select_query = 'SELECT * FROM {}'.format(cls.__tablename__)
        cars = []
        for row in cur.execute(select_query):
            cars.append({'mark': row[0], 'max_speed': row[1], 'distance': row[2], 'handler': row[3], 'stock': row[4]})

        conn.close()
        return cars

    def insert(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        insert_query = 'INSERT INTO {} VALUES (?, ?, ?, ?, ?)'.format(self.__tablename__)
        cur.execute(insert_query, (self.mark, self.max_speed, self.distance, self.handler, self.stock,))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        update_query = 'UPDATE {} SET max_speed=?, distance=?, handler=?, stock=? WHERE mark=?'.format(self.__tablename__)
        cur.execute(update_query, (self.max_speed, self.distance, self.handler, self.stock, self.mark,))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()

        delete_query = 'DELETE FROM {} WHERE mark=?'.format(self.__tablename__)
        cur.execute(delete_query, (self.mark,))
        
        conn.commit()
        conn.close()

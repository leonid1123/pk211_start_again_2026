import pymysql.cursors


class Db_handler:
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='pk211',
            password='1234',
            database='pk211_db'
        )
        self.cur = self.conn.cursor()

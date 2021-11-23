import sqlite3
from sqlite3 import Error


class SQLManager(object):

    def __init__(self):
        self.conn = None
        self.dbPath = 'review_database.db'
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.dbPath)
            print("connection created")
        except Error as e:
            print(e)

    def select_all_sentiment(self, choice):
        """
        Query the entire training table dataset to grab the sentiment choice for setting up the training data
        :param conn: the connection object
        :param choice: and binary choice to select sentiment 0 = negative. 1 = positive
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT review FROM training WHERE sentiment = ?", (choice,))

        results = cur.fetchall()
        return results

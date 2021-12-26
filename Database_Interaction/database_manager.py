# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# database_manager.py
# database management for setting up connections and hard coded queries for
# accessing review and movie data
# Author: Dalton Senseman
# version 0.1a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
from sqlite3 import Error


class SQLManager(object):

    def __init__(self):
        self.conn = None
        self.dbPath = 'Unprocessed Data Loader/review_database.db'
        self.create_connection()

    def create_connection(self):
        """
        establishes the initial connection to the SQL database
        :param self: references the object
        """
        try:
            self.conn = sqlite3.connect(self.dbPath)
            print("connection created")
        except Error as e:
            print(e)

    def close_connection(self):
        """
        establishes the initial connection to the SQL database
        :param self: references the object
        """
        try:
            self.conn.close()
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

    def select_a_review(self, choice):
        cur = self.conn.cursor()
        cur.execute("SELECT review_detail FROM review WHERE review_id = ?", (choice,))

        results = cur.fetchall()
        return results

    def display_a_review(self, choice):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM review WHERE review_id = ?", (choice,))

        results = cur.fetchall()
        return results

    def display_review_results(self, id):
        cur = self.conn.cursor()

        cur.execute("select * from review where movie_id = ?", (str(id),))

        results = cur.fetchall()
        return results

    def search_movies(self,title):
        cur=self.conn.cursor()
        fixed_title = "%" + title.replace("%20", " ") + "%"

        print(fixed_title)
        cur.execute("SELECT * from movies WHERE movies.name LIKE ?", (fixed_title,))

        results = cur.fetchall()
        return results


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

    def __init__(self, path):
        self.conn = None
        self.dbPath = path
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

    def select_all_reviews_to_list(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM review")
        review_list = cur.fetchall()

        return review_list

    def select_a_review(self, choice):
        cur = self.conn.cursor()
        cur.execute("SELECT review_detail FROM review WHERE review_id = ?", (choice,))

        results = cur.fetchall()
        return results

    def insert_processed_review(self, review, sentiment):
        cur = self.conn.cursor()
        print(review)
        print(sentiment)
        cur.execute(f"INSERT OR IGNORE INTO proc_review VALUES (?,?,?,?,?,?,?,?,?,?,?);", (review[0], review[1],
                                                                        review[2], review[3],
                                                                        review[4], review[5],
                                                                        review[6], review[7],
                                                                        review[8], review[9], sentiment))
        self.conn.commit()

    def init_proc_table(self):
        cur = self.conn.cursor()
        processed_table_creation = "CREATE TABLE IF NOT EXISTS proc_review (review_id varchar PRIMARY KEY," \
                                    "reviewer varchar," \
                                    "movie_id int," \
                                    "rating int," \
                                    "review_summary varchar," \
                                    "review_date varchar," \
                                    "spoiler_tag boolean, " \
                                    "review_detail varchar," \
                                    "helpful int," \
                                    "not_helpful int," \
                                    "sentiment_score float," \
                                    "FOREIGN KEY(movie_id) REFERENCES movie(ref_num));"
        cur.execute(processed_table_creation)

    # API Usage
    def display_a_review(self, choice):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM proc_review WHERE review_id = ?", (choice,))

        results = cur.fetchall()
        return results

    def display_review_results(self, id):
        cur = self.conn.cursor()

        cur.execute("select * from proc_review where movie_id = ?", (str(id),))

        results = cur.fetchall()
        return results

    def search_movies(self, title):
        cur=self.conn.cursor()
        fixed_title = "%" + title+ "%"

        print(fixed_title)
        cur.execute("SELECT * from movies WHERE movies.name LIKE ?", (fixed_title,))

        results = cur.fetchall()
        return results

    def select_a_movie(self,id):
        cur = self.conn.cursor()
        cur.execute("SELECT * from movies WHERE ref_num = ?", (str(id),))

        results = cur.fetchall()
        return results

    def display_user(self, name):
        cur = self.conn.cursor()
        name = '\'' + name + '\''
        print(name)
        cur.execute("SELECT *, movies.name from proc_review INNER JOIN movies on movies.ref_num=proc_review.movie_id WHERE proc_review.reviewer = ?", (name,))

        results = cur.fetchall()

        return results


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# database_manager.py
# database management for setting up connections and hard coded queries for
# accessing review and movie data
# Author: Dalton Senseman
# version 0.1a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
from sqlite3 import Error
from numpy import mean


class SQLManager(object):

    def __init__(self):
        self.conn = None
        self.dbPath = '/home/ubuntu/reviewsense/FlaskServer/review_database.db' 
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

    def update_processed_review(self, review):
        cur = self.conn.cursor()
        print(review)
        cur.execute(f"UPDATE  proc_review set review_detail = ? WHERE review_id = ?;", (review[7], review[0]))
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
        cur.execute("SELECT * from review "
                    "INNER JOIN scores on review.review_id = scores.review_id where review.review_id = ?;", (choice,))

        results = cur.fetchall()
        return results

    def display_review_results(self, id, page, sentiment):
        cur = self.conn.cursor()
        query = ''
        if sentiment == 'positive':
            query = 'AND scores.sentiment_score > 0'
        elif sentiment == 'negative': 
            query = 'AND scores.sentiment_score < 0'	
        if int(page) >=0:
            offset = (20 * int(page))
            cur.execute("SELECT * from review INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ?"+query + " LIMIT 20 OFFSET ?;", (str(id),offset))
        else:    
            cur.execute("SELECT * from review INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ?"+query + ";", (str(id),))


        results = cur.fetchall()
        
        return results
    
    def display_sentiment(self, id, page, pos_or_neg):
        cur = self.conn.cursor()
        query = "SELECT * from review INNER JOIN movies on review.movie_id = movies.ref_num "\
		"INNER JOIN scores on review.review_id = scores.review_id where movie_id = ? AND scores.sentiment_score"    
	
        if (pos_or_neg == 'positive'):
            query = query + '> 0'
        elif (pos_or_neg == 'negative'):
            query = query + '< 0'
        offset = (20 * (int(page)))
        cur.execute(query+ " LIMIT 20 OFFSET ?;", (str(id),offset))
        results = cur.fetchall()
        return results

    def sentiment_count(self, id, keyword):
        cur = self.conn.cursor()
        query = "SELECT COUNT(*) from review INNER JOIN movies on review.movie_id = movies.ref_num "\
                "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ?"    
        if keyword != 'null':
            query += ' AND (review.review_detail LIKE ? OR review.review_summary LIKE ?) '
            pos_query = query + 'AND scores.sentiment_score >0;'
            neg_query = query + 'AND scores.sentiment_score< 0;'
           
            print(pos_query)
            cur.execute(pos_query, (str(id),"%"+keyword+"%", "%"+keyword+"%"))
            pos_result = cur.fetchall()
            cur.execute(neg_query, (str(id),"%"+keyword+"%", "%"+keyword+"%"))
            neg_result = cur.fetchall()
            print(pos_result)
        else:
         
            pos_query = query + 'AND scores.sentiment_score >0;'
            neg_query = query + 'AND scores.sentiment_score< 0;'
        
            print(pos_query)
            cur.execute(pos_query, (str(id),))
            pos_result = cur.fetchall()

            cur.execute(neg_query, (str(id),))
            neg_result = cur.fetchall()
            print(pos_result)
        return [{'value': pos_result[0][0], 'name':'Positive'}, {'value': neg_result[0][0], 'name':'Negative'}]

    def search_movies(self, title, page):
        cur=self.conn.cursor()
        fixed_title = "%" + title+ "%"
        offset = (20 * int(page))
        print(fixed_title)
        cur.execute("SELECT * from movies WHERE movies.name LIKE ? COLLATE NOCASE LIMIT 20 OFFSET ?", (fixed_title,str(offset)))

        results = cur.fetchall()
        return results
     
    def keyword_search(self, id, page, keyword):
        cur=self.conn.cursor()
        fixed_keyword = "%"+keyword + "%"
        offset = (20 *(int(page)))
        cur.execute("SELECT * from review INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ? AND (review.review_detail LIKE ? OR review.review_summary LIKE ?) LIMIT 20 OFFSET ?", (str(id),fixed_keyword, fixed_keyword, offset))
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
        cur.execute("SELECT *, scores.sentiment_score, movies.name from review "
                    "INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where review.reviewer = ?", (name,))

        results = cur.fetchall()

        return results

    def get_all_movies(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from movies")
        results = cur.fetchall()

        return results

    def get_all_sentiment(self, id):
        print(id[0])
        cur = self.conn.cursor()
        cur.execute("SELECT scores.sentiment_score from review "
                    "INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ?;", (str(id[0]),))

        results = cur.fetchall()
        results = [result[0] for result in results]
        print(results)
        return mean(results)

    def add_sentiment(self, id, score):
        print(id)
        cur = self.conn.cursor()
        cur.execute("UPDATE movies set average_score = ? where ref_num = ?;", (str(score), str(id)))
        self.conn.commit()

    def get_review_count(self, id):
        print(id[0])
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) from review "
                    "INNER JOIN movies on review.movie_id = movies.ref_num "
                    "INNER JOIN scores on review.review_id = scores.review_id where movie_id = ?;", (str(id[0]),))

        results = cur.fetchall()[0][0]
        print(results)
        return results

    def add_review_count(self, id, count):
        print(id)
        cur = self.conn.cursor()
        cur.execute("UPDATE movies set review_count = ? where ref_num = ?;", (str(count), str(id)))
        self.conn.commit()

    def add_poster_url(self, id, url):
        cur = self.conn.cursor()
        print(id)
        cur.execute("UPDATE movies set poster_url = ? where ref_num = ?;", (str(url), str(id)))
        self.conn.commit()

    def display_x_movies(self, count):
        cur = self.conn.cursor()
        print(id)
        cur.execute("SELECT * from movies ORDER BY review_count DESC LIMIT ?", (str(count),))

        results=cur.fetchall()
        return results

    def get_lowest_movies(self, count):
        cur = self.conn.cursor()

        cur.execute("SELECT * from movies WHERE review_count > 3 ORDER BY average_score ASC, review_count DESC  LIMIT ?", (str(count),))

        results = cur.fetchall()
        return results

    def get_highest_movies(self, count):
        cur = self.conn.cursor()

        cur.execute("SELECT * from movies WHERE review_count > 3 ORDER BY average_score DESC, review_count DESC  LIMIT ?", (str(count),))

        results = cur.fetchall()
        return results


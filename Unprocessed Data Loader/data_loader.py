# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data_loading.py
# Tool for loading review data into an sqlite database
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
import data_scrubber as ds
import sys
import csv
import json

con = sqlite3.connect('./review_database.db')

training_table_creation = 'CREATE TABLE IF NOT EXISTS training (' \
                          'review_id integer PRIMARY KEY,' \
                          'review text,' \
                          'sentiment integer)'

cur = con.cursor()

cur.execute(training_table_creation)
con.commit()

cur.execute("DROP TABLE movies;")

movie_table_creation = "CREATE TABLE IF NOT EXISTS movies (ref_num int PRIMARY KEY, name varchar, UNIQUE(name));"

cur.execute(movie_table_creation)
con.commit()

processing_table_creation = "CREATE TABLE IF NOT EXISTS review (review_id varchar PRIMARY KEY," \
                            "reviewer varchar," \
                            "movie_id int," \
                            "rating int," \
                            "review_summary varchar," \
                            "review_date varchar," \
                            "spoiler_tag boolean, " \
                            "review_detail varchar," \
                            "helpful int," \
                            "not_helpful int," \
                            "FOREIGN KEY(movie_id) REFERENCES movie(ref_num));"

cur.execute(processing_table_creation)
con.commit()

target = sys.argv[1]
file = sys.argv[2]

sentiments = {
    "positive": 1,
    "negative": 0
}

statements = []
if target.lower() == "training":
    print("training")
    with open(file, newline='', encoding="utf8") as csvfile:
        training_batch_statement = 'INSERT OR IGNORE INTO ' \
                                   'training VALUES'
        reader = csv.reader(csvfile, delimiter='\"', quotechar='|')
        next(reader, None)
        counter = 0
        for row in reader:
            counter = counter + 1
            sentiment = row[-1][1:]
            if (row[0]):
                review = ds.clean_string(''.join(row[:-1]))
            else:
                review = ds.clean_string(''.join(row[1:-1]))

            try:
                review_addition = ds.package_training_review(
                    counter, review, sentiments[sentiment])
                training_batch_statement = training_batch_statement + \
                                           review_addition + ','

            except KeyError:
                fixed_review = row[-1].rsplit(',', 1)

                review = ds.clean_string(fixed_review[0])

                review_addition = ds.package_training_review(
                    counter, review, sentiments[fixed_review[1]])
                training_batch_statement = training_batch_statement + \
                                           review_addition + ','

            if counter % 1000 == 0:  # 1000 increment batches

                statements.append(training_batch_statement[:-1] + ';')

                try:
                    cur.execute(statements[-1])
                    con.commit()
                except sqlite3.OperationalError as e:
                    print(e)

                training_batch_statement = 'INSERT INTO training ' \
                                           'VALUES '


elif target.lower() == "processing":
    print("processing")
    with open(file, newline='', encoding="utf8") as jsonfile:
        data = json.load(jsonfile)
        cur.execute("SELECT COUNT(*) from movies")
        count = cur.fetchone()[0]
        movie_statement = f"INSERT INTO movies VALUES"
        for review in data:
            try:
                cur.execute(ds.package_movie(count, review['movie']))
                print(ds.package_movie(count, review['movie']))
                count = count + 1
            except sqlite3.IntegrityError:
                try:
                    movie_title = '\'' + review['movie'] + '\''
                    cur.execute(f"SELECT ref_num from movies WHERE name = {movie_title};")
                    print(cur.fetchone())
                    print(ds.package_processing_review(review))
                except sqlite3.OperationalError as e:
                    print(e)
                    print(ds.package_movie(count, review['movie']))
                    break





elif target.lower() == "display_training":
    select = 'SELECT * from training LIMIT 1;'
    cur.execute(select)
    rows = cur.fetchall()
    print(rows)

con.close()

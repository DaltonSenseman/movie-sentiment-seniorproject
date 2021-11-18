# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data_loading.py
# Tool for loading review data into an sqlite database
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import sqlite3
import data_scrubber as ds
import sys
import csv

con = sqlite3.connect('review_database.db')

table_creation = 'CREATE TABLE IF NOT EXISTS training (' \
                 'review_id integer PRIMARY KEY,' \
                 'review text,' \
                 'sentiment integer)'

cur = con.cursor()

cur.execute(table_creation)
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
        training_batch_statement = 'INSERT INTO training VALUES'
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
                review_addition = ds.package_training_review(counter, review, sentiments[sentiment])
                training_batch_statement = training_batch_statement + review_addition + ','

            except KeyError:
                fixed_review = row[-1].rsplit(',', 1)

                review = ds.clean_string(fixed_review[0])

                review_addition = ds.package_training_review(counter, review, sentiments[fixed_review[1]])
                training_batch_statement = training_batch_statement + review_addition + ','

            if (counter % 1000 == 0):

                statements.append(training_batch_statement[:-1] + ';')

                try:
                    cur.execute(statements[-1])
                    con.commit()
                except sqlite3.OperationalError as e:
                    print(e)

                training_batch_statement = 'INSERT INTO training VALUES '


elif target.lower() == "processing":
    print("processing")

select = 'SELECT * from training;'

cur.execute(select)

con.close()

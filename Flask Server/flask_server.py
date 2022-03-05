# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# flask_server.py
# Backend server program responsible for API calls and data management
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
from Database_Interaction.database_manager import SQLManager
from collections import Counter
from nltk.corpus import stopwords
import re
import csv

# document containing common filler words not in stopwords and words that will appear problematic in word cloud
with open('removal_words.csv', newline='') as f:
    reader = csv.reader(f)
    data = [row[0] for row in reader]

app = Flask(__name__)
CORS(app)

cached_stopwords = stopwords.words('english') + data


@app.route('/reviews', methods=['GET'])
def specific_review():
    review_id = request.args.get('review_id')
    sql_manager = SQLManager()
    test_review = sql_manager.display_a_review("\'" + review_id + "\'")[0]

    review_data = {'name': test_review[1].strip('\'').replace('\"', '\''),
                   'date': test_review[5].strip('\'').replace('\"', '\''),
                   'title': test_review[4].strip('\'').replace('\"', '\''),
                   'review': test_review[7].strip('\'').replace('\"', '\''),
                   'sentiment': test_review[12]}

    sql_manager.close_connection()

    response = jsonify(review_data)

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/reviewlists', methods=['GET'])
def reviews():
    id = request.args.get('movie_id')
    sql_manager = SQLManager()
    response = sql_manager.display_review_results(id)
    movie = sql_manager.select_a_movie(id)[0]
    movie_title = movie[1].lower()
    movie_title = re.sub(r'[^\w\s]', '', movie_title)

    review_tokens = []
    reviews = []
    overall_sentiment = movie[2]
    for review in response:
        removables = cached_stopwords + movie_title.split()
        review_tokens += ([re.sub(r'[^\w\s]', '', x.lower()) for x in review[7].strip('\'').replace('\"', '\'').split()
                           + review[4].strip('\'').replace('\"', '\'').split()
                           if (re.sub(r'[^\w\s]', '', x.lower()) not in removables)])
        review_data = {'review_id': review[0].strip('\''),
                       'name': review[1].strip('\'').replace('\"', '\''),
                       'date': review[5].strip('\''),
                       'title': review[4].strip('\'').replace('\"', '\''),
                       'review': review[7].strip('\'').replace('\"', '\''),
                       'sentiment': review[16]}
        reviews.append(review_data)

    counter = Counter(review_tokens)
    del counter[""]

    reviews.append({'Review Tokens': counter.most_common(20)})

    reviews.append({'Overall Sentiment': overall_sentiment})
    response = jsonify(reviews)

    response.headers.add('Access-Control-Allow-Origin', '*')
    sql_manager.close_connection()
    return response


@app.route('/moviesearches', methods=['GET'])
def search():
    title = request.args.get('title').replace("%20", " ")
    sql_manager = SQLManager()
    response = sql_manager.search_movies(title)
    movies = []
    for movie in response:
        movie_data = {'ref_num': movie[0],
                      'name': movie[1],
                      'poster_url': movie[4]}
        movies.append(movie_data)
    response = jsonify(movies)

    response.headers.add('Access-Control-Allow-Origin', '*')

    sql_manager.close_connection()
    return response


@app.route('/movies', methods=['GET'])
def movie():
    id = request.args.get('ref_num')
    print(id)
    sql_manager = SQLManager()
    movie = sql_manager.select_a_movie(id)[0]
    print(movie)
    movie_data = {'ref_num': movie[0],
                  'name': movie[1],
                  'poster_url': movie[4]}
    sql_manager.close_connection()
    response = jsonify(movie_data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/homepage', methods=['GET'])
def homepage():
    sql_manager = SQLManager()
    response = sql_manager.display_x_movies(20)
    movies = []
    for movie in response:
        movie_data = {'ref_num': movie[0],
                      'name': movie[1],
                      'poster_url': movie[4]}
        movies.append(movie_data)
    response = jsonify(movies)
    response.headers.add('Access-Control-Allow-Origin', '*')

    sql_manager.close_connection()
    return response


@app.route('/users', methods=['GET'])
def user():
    name = request.args.get('name').replace("%20", " ")
    sql_manager = SQLManager()
    response = sql_manager.display_user(name)

    reviews = []

    for review in response:
        print(review)
        review_data = {'review_id': review[0],
                       'movie': review[11],
                       'review_summary': review[4].strip('\'').replace('\"', '\''),
                       'review_date': review[5].strip('\''),
                       'review': review[7].strip('\'').replace('\"', '\''),
                       'rating': review[3],
                       'sentiment': review[14]}
        reviews.append(review_data)

    sql_manager.close_connection()
    return jsonify(reviews)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, ssl_context='adhoc')

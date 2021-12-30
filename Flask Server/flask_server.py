# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# flask_server.py
# Backend server program responsible for API calls and data management
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from flask import Flask
from flask import jsonify
from flask import request
from Database_Interaction.database_manager import SQLManager

app = Flask(__name__)


@app.route('/get', methods=['GET'])
def hello():
    review_id = request.args.get('review_id')
    sql_manager = SQLManager()
    test_review = sql_manager.display_a_review("\'" + review_id + "\'")[0]

    review_data = {'name': test_review[1].strip('\'').replace('\"', '\''),
                   'date': test_review[5].strip('\'').replace('\"', '\''),
                   'title': test_review[4].strip('\'').replace('\"', '\''),
                   'review': test_review[7].strip('\'').replace('\"', '\'')}

    sql_manager.close_connection()
    return jsonify(review_data)


@app.route('/reviews', methods=['GET'])
def reviews():
    id = request.args.get('id')
    sql_manager = SQLManager()
    response = sql_manager.display_review_results(id)

    reviews = []
    for review in response:
        review_data = {'name': review[1].strip('\'').replace('\"', '\''),
                       'date': review[5].strip('\'').replace('\"', '\''),
                       'title': review[4].strip('\'').replace('\"', '\''),
                       'review': review[7].strip('\'').replace('\"', '\'')}
        reviews.append(review_data)

    sql_manager.close_connection()
    return jsonify(reviews)

@app.route('/search', methods=['GET'])
def search():
    title = request.args.get('title').replace("%20", " ")
    sql_manager = SQLManager()
    response = sql_manager.search_movies(title)

    movies = []
    for movie in response:
        movie_data = {'ref_num': movie[0],
                      'name': movie[1]}
        movies.append(movie_data)

    sql_manager.close_connection()
    return jsonify(movies)

@app.route('/user', methods=['GET'])
def user():
    name = request.args.get('name').replace("%20", " ")
    sql_manager = SQLManager()
    response = sql_manager.display_user(name)

    reviews = []
    for review in response:
        print(review)
        review_data = {'review_id': review[0],
                       'movie': review[11],
                       'review_summary': review[4],
                       'review_date': review[5],
                       'review': review[7],
                       'rating': review[3]}
        reviews.append(review_data)


    sql_manager.close_connection()
    return jsonify(reviews)


import Database_Interaction.database_manager as db

import requests
import re

sql_manager = db.SQLManager()

movies = sql_manager.get_all_movies()

for movie in movies:
    title = movie[1].split('(')[0]
    title = re.sub(r"[^a-zA-Z0-9 \s]","",title)
    try:
        poster_path = requests.get('https://api.themoviedb.org/3/search/multi?api_key=f213c4954a309bf85342338cab0ba8a6&'
                               'language=en-US&query=' + title + '&page=1&include_adult=true').json()
        print(poster_path)

        sql_manager.add_poster_url(movie[0], 'https://image.tmdb.org/t/p/w220_and_h330_face' + poster_path['results'][0]['backdrop_path'])
    except IndexError:
        print('no poster found, no movie found')
    except TypeError:
        print('no poster found, movie found')
    except KeyError:
        print('no poster found, incorrect search')

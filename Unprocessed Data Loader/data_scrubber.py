# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data_scrubber.py
# Tool for cleaning out extraneous data
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def clean_string(string):
    cleaned_string = string.replace('<br/>', '')
    cleaned_string = cleaned_string.replace('<br />', '')
    cleaned_string = cleaned_string.replace('\'', '\"')
    cleaned_string = cleaned_string.replace('`', '\"')
    cleaned_string = cleaned_string.replace('\n', '')
    #cleaned_string = cleaned_string.replace('(', '[')
    #cleaned_string = cleaned_string.replace(')', ']')
    return cleaned_string


def package_training_review(counter, review, sentiment):
    response = '(' + str(counter) + ',\'' + review + '\',' + \
               str(sentiment) + ')'

    return response


# "CREATE TABLE IF NOT EXISTS review (review_id varchar PRIMARY KEY," \
#                           "reviewer varchar," \
#                          "movie_id int," \
#                         "rating int," \
#                        "review_summary varchar," \
#                       "review_date varchar," \
#                      "spoiler_tag boolean, " \
#                     "review_detail varchar," \
#                    "helpful int," \
#                   "not_helpful int," \
#                  "FOREIGN KEY(movie_id) REFERENCES movie(ref_num));"

def package_processing_review(review):
    response = f"({review['review_id']}, {review['reviewer']}, " \
               f"{review['rating']}," \
               f"{clean_string(review['review_summary'])}, {review['review_date']}," \
               f" {bool(review['spoiler_tag'])}," \
               f"{clean_string(review['review_detail'])},{review['helpful'][0]}," \
               f"{review['helpful'][1]})"
    return response

def package_movie(count, title):
    movie_title = '\'' + clean_string(title) + '\''
    response = f"INSERT INTO movies VALUES({count}, {movie_title});"
    return response

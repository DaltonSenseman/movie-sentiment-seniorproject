# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data_scrubber.py
# Tool for cleaning out extraneous data
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def clean_string(string):
    """
    Cleans a string of any characters that would disrupt data upload
    :param string: the string to be cleaned
    :return: a version of the string without the given special characters
    """
    cleaned_string = string.replace('<br/>', '')
    cleaned_string = cleaned_string.replace('<br />', '')
    cleaned_string = cleaned_string.replace('\'', '"')
    cleaned_string = cleaned_string.replace('`', '"')
    cleaned_string = cleaned_string.replace('\n', '')

    return cleaned_string


def package_training_review(id_num, review, sentiment):
    """
    Prepares a piece of training data for database storage
    :param id_num: the integer assigned to the review as a tag
    :param review: the review itself
    :param sentiment: the binary score for sentiment as given by the training data
    :return: a SQLite input piece to be combined in an INSERT statement
    """
    response = '(' + str(id_num) + ',\'' + review + '\',' + \
               str(sentiment) + ')'

    return response


def package_processing_review(review, movie_tag):
    """
    Prepares a piece of processing data for database storage
    :param review: the review itself
    :param movie_tag: the int id given to the movie the review is referring to as found in the MOVIES table
    :return: a list of values to be referred to in an SQL formatted statement
    """
    review_id = '\'' + review['review_id'] + '\''
    reviewer = '\'' + review['reviewer'] + '\''
    review_summary = '\'' + clean_string(review['review_summary']) + '\''
    full_review = '\'' + clean_string(review['review_detail']) + '\''
    date = '\'' + review['review_date'] + '\''

    rating = review['rating']
    if rating is None:
        rating = -1

    response = f"({review_id},{reviewer},{movie_tag}," \
               f"{rating}," \
               f"{review_summary},{date}," \
               f" {bool(review['spoiler_tag'])}," \
               f"{full_review},{(review['helpful'][0]).replace(',', '')}," \
               f"{(review['helpful'][1]).replace(',', '')}),"

    response = [review_id,reviewer,movie_tag,
               rating,review_summary,date,
               bool(review['spoiler_tag']),
               full_review,(review['helpful'][0]).replace(',', ''),
               (review['helpful'][1]).replace(',', '')]
    return response


def package_movie(count, title):
    """
    Prepares a movie for database storage
    :param count: the next available id_num for a movie
    :param title: the name of the movie
    :return: a SQLite INSERT statement for the given movie
    """
    movie_title = '\'' + clean_string(title) + '\''
    response = f"INSERT INTO movies VALUES({count},{movie_title});"
    return response

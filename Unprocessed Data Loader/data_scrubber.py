# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# data_scrubber.py
# Tool for cleaning out extraneous data
# Carrie West
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def clean_string(string):
    cleaned_string = string.replace('<br/>', '')
    cleaned_string = cleaned_string.replace('<br />', '')
    cleaned_string = cleaned_string.replace('\'', '"')
    cleaned_string = cleaned_string.replace('`', '"')
    cleaned_string = cleaned_string.replace('\n', '')
    #cleaned_string = cleaned_string.replace('(', '[')
    #cleaned_string = cleaned_string.replace(')', ']')
    return cleaned_string


def package_training_review(counter, review, sentiment):
    response = '(' + str(counter) + ',\'' + review + '\',' + \
               str(sentiment) + ')'

    return response

def package_processing_review(review, movie_tag):
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
               f"{full_review},{(review['helpful'][0]).replace(',','')}," \
               f"{(review['helpful'][1]).replace(',','')}),"
    return response

def package_movie(count, title):
    movie_title = '\'' + clean_string(title) + '\''
    response = f"INSERT INTO movies VALUES({count},{movie_title});"
    return response

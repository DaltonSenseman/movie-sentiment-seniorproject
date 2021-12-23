# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NaiveBayes.py
# Root file for the Naive Bayes algorithm, grabs the training data, creates the
# initial histograms to set up the ML environment
# Author: Dalton Senseman
# version 0.1a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import Counter

from Database_Interaction.database_manager import SQLManager
import re


def data_cleaning(data):
    """
    Cleans the training data to not have punctuation and also be in all lowercase
    :param data: an array/list of strings
    :return: a array/list of strings
    """
    cleaned_list = []
    for content in data:
        changed_content = re.sub(r'[\.\!\?]', ' ', str(content))
        changed_content = re.sub(r'[\']', '', str(content))
        changed_content = re.sub(r'[\W]', ' ', str(content))
        cleaned_list.append(changed_content.strip().lower())

    return cleaned_list


def generate_histogram(string_list):
    """
    Creates a histogram of each occurrence of the word in the list
    :param string_list: a list/array of words
    :return: a list of the words and how many times it appeared in the entire array/list ("word": value)
    """
    large_concat = ' '.join(string_list)
    words = large_concat.split()
    count_all = Counter(words)
    return count_all


def create_dictionary(database_connection, value):
    """
    Creates the training data dictionary's by cleaning the data amd having a histogram made
    :param database_connection: connection to the testdata SQL server connection
    :param value: what training data list to grab (0 for negative, 1 for positive)
    :return: a compiled dictionary
    """
    clean = data_cleaning(database_connection.select_all_sentiment(value))
    new_list = generate_histogram(clean)
    dictionary = dict(new_list)
    return dictionary


def sentiment_generator(review_data, test_data_pos, test_data_neg):
    """
    Takes in a single review and checks it against the positive and negative data lists to generate the sentiment
    :param review_data: the review dictionary of the review we are creating the sentiment for
    :param test_data_pos: the positive dictionary of training data to check against for the ML
    :param test_data_neg: the negative dictionary of training data to check against for the ML
    :return: will return the score of sentiment for that particular review
             (0 for negative 1 for positive) -1 is a placeholder for now
    """
    for key in review_data.keys():
        print("\"" + key + "\"" + " value -> " + str(review_data.get(key)))  # get value of that key in the dict

        if key in test_data_pos.keys():
            print("pos HIT")
            print(test_data_pos.get(key))  # get value of that key in the dict
        if key in test_data_neg.keys():
            print("neg HIT")
            print(test_data_neg.get(key))  # get value of that key in the dict
        else:
            print("no Key need a black box (artificial value to not have * or / by Zero errors)")

    sentiment_score = -1

    return sentiment_score


def main():
    sentiment = SQLManager()

    neg_dict = create_dictionary(sentiment, 0)
    pos_dict = create_dictionary(sentiment, 1)

    # total number of words in the entire dictionary for use in making fractional probability
    pos_dict_TOTAL = sum(pos_dict.values())  # total number of words 5,702,647
    neg_dict_TOTAL = sum(neg_dict.values())  # total  number of words 5,609,804
    testdata_TOTAL = (pos_dict_TOTAL + neg_dict_TOTAL)  # total data points(words) 113,124,451

    pos_prior_probability = (pos_dict_TOTAL / testdata_TOTAL)  # .5041
    neg_prior_probability = (neg_dict_TOTAL / testdata_TOTAL)  # .4958

    # grabbing a single review to use as a test to create the algorithm
    review_test = sentiment.select_a_review("rw1985329")
    review_test_clean = data_cleaning(review_test)
    review_test = dict(generate_histogram(review_test_clean))

    # testing searching in the positive and negative lists for matching keys

    # method below will return the score of the review to then be pushed into the DB

    print(sentiment_generator(review_test, pos_dict, neg_dict))

    # after compiling matching keys we can then get probabilities and do the algorithm :D
    # setting the value into a after-ML Table in the DB and iterate though the entire pre-ML data set
    # then we can tinker with accuracy -Dalton S.


"""             START OF PROGRAM                      """

main()

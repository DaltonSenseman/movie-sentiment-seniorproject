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
        changed_content = re.sub(r'[^\w\s]', '', str(content))
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


def main():
    sentiment = SQLManager()

    neg_dict = create_dictionary(sentiment, 0)
    pos_dict = create_dictionary(sentiment, 1)

    # total number of words in the entire dictionary for use in making fractional probability
    pos_dict_TOTAL = sum(pos_dict.values())  # total number 5702647
    neg_dict_TOTAL = sum(neg_dict.values())  # total number 5609804
    testdata_TOTAL = (pos_dict_TOTAL + neg_dict_TOTAL)  # total 113124451

    pos_prior_probability = (pos_dict_TOTAL / testdata_TOTAL)  # .5041
    neg_prior_probability = (neg_dict_TOTAL / testdata_TOTAL)  # .4958

    # grabbing a single review to use as a test to create the algorithm

    review_test = sentiment.select_a_review("rw1985329")
    
    print(review_test)


"""             START OF PROGRAM                      """

main()

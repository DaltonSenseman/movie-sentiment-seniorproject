# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NaiveBayes.py
# Root file for the Naive Bayes algorithm, grabs the training data, creates the
# initial histograms to set up the ML environment
# Author: Dalton Senseman
# version 0.1a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from collections import Counter

from database_manager import SQLManager
import re


def training_data_cleaning(data):
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


def main():
    sentiment = SQLManager()
    negative_result = sentiment.select_all_sentiment(0)
    negative_clean = training_data_cleaning(negative_result)
    positive_result = sentiment.select_all_sentiment(1)
    positive_clean = training_data_cleaning(positive_result)

    positive_list = generate_histogram(positive_clean)
    negative_list = generate_histogram(negative_clean)

    # print(positive_list)
    # print(negative_list)


"""             START OF PROGRAM                      """

main()

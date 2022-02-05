# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# NaiveBayes.py
# Root file for the Naive Bayes algorithm, grabs the training data, creates the
# initial histograms to set up the ML environment
# Author: Dalton Senseman
# version 0.1a
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
from collections import Counter

from Database_Interaction.database_manager import SQLManager
import re
import math
from nltk.corpus import stopwords


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
    clean_dictionary = remove_stopwords(dictionary)

    return clean_dictionary


def remove_stopwords(dictionary):
    """
    Takes in a dictionary and compares it to a list of stopwords, if the stopword is in the dictionary it is removed.
    :param dictionary: a dictionary of words to be checked in the tuple form (word : #)
    :return: the dictionary that has the words in the stopwords list removed from it.
    """
    stopwords_list = set(stopwords.words('english'))
    for word in dictionary.copy():  # copies the dictionary so the indexes don't change while popping out words
        if word in stopwords_list:
            dictionary.pop(word)

    return dictionary


def sentiment_generator(review_full,review_data, test_data_pos, test_data_neg, pos_dict_TOTAL, neg_dict_TOTAL,
                        pos_prior_probability, neg_prior_probability):
    """
    Takes in a single review and checks it against the positive and negative data lists to generate the sentiment
    :param neg_prior_probability:
    :param pos_prior_probability:
    :param neg_dict_TOTAL:
    :param pos_dict_TOTAL:
    :param review_data: the review dictionary of the review we are creating the sentiment for
    :param test_data_pos: the positive dictionary of training data to check against for the ML
    :param test_data_neg: the negative dictionary of training data to check against for the ML
    :return: will return the score of sentiment for that particular review
             (0 for negative 1 for positive) -1 is a placeholder for now
    """

    positive_running_total = 1
    negative_running_total = 1

    num_blackbox_keys = len(review_data.keys())  # number to add to total to account for blackboxing out 0 values
    alpha = 1  # value to blackbox values to negate * 0 possibilities

    for key in review_data.keys():
        #print("\"" + key + "\"" + " value -> " + str(review_data.get(key)))  # get value of that key in the dict

        # Naives Bayes P(# of time happened in training data / total # in data) ^ # of times happened in data being
        # tested, then * to all other keys probabilities * the prior probability.
        if key in test_data_pos.keys():
            #print("pos HIT")
            value_of_words_pos = pow(((test_data_pos.get(key) + alpha) / (pos_dict_TOTAL + num_blackbox_keys)),
                                     review_data.get(key))  # get value of that key in the dict
            try:
                positive_running_total += math.log(value_of_words_pos)
            except ValueError as e:
                print(review_full)
                print("ERROR HERE %.40f" %(value_of_words_pos))
                sys.exit()
        else:
            #print("NO pos")
            value_of_words_pos = pow((alpha / (pos_dict_TOTAL + num_blackbox_keys)),
                                     review_data.get(key))  # get value of that key in the dict
            positive_running_total += math.log(value_of_words_pos)

        if key in test_data_neg.keys():
            #print("neg HIT")
            value_of_words_neg = pow(((test_data_neg.get(key) + alpha) / (neg_dict_TOTAL + num_blackbox_keys)),
                                     review_data.get(key))  # get value of that key in the dict
            try:
                negative_running_total += math.log(value_of_words_neg)
            except ValueError as e:
                print(review_full)
                print("ERROR HERE %.40f" %(value_of_words_neg))
                sys.exit()
        else:
            #print("NO neg")
            value_of_words_neg = pow((alpha / (neg_dict_TOTAL + num_blackbox_keys)),
                                     review_data.get(key))  # get value of that key in the dict
            negative_running_total += math.log(value_of_words_neg)

    #print(positive_running_total)
    pos_result = pos_prior_probability + positive_running_total
    #print(negative_running_total)
    neg_result = neg_prior_probability + negative_running_total

    #print("Cumulative percentage: " + str(((neg_result - (pos_result) )/ neg_result)))

    if (pos_result == 0) or (neg_result == 0):
        raise Exception("Encountered a result that overflowed the running total % float value of the data set")

    #if pos_result > neg_result:
     #   sentiment_score = 1
   # else:
       # sentiment_score = 0

    sentiment_score = (neg_result - pos_result) / neg_result

    return sentiment_score


def main():
    db_manager = SQLManager()

    neg_dict = create_dictionary(db_manager, 0)
    pos_dict = create_dictionary(db_manager, 1)

    # total number of words in the entire dictionary for use in making fractional probability
    pos_dict_TOTAL = sum(pos_dict.values())  # total number of words 5,702,647
    neg_dict_TOTAL = sum(neg_dict.values())  # total  number of words 5,609,804
    testdata_TOTAL = (pos_dict_TOTAL + neg_dict_TOTAL)  # total data points(words) 13,124,451

    pos_prior_probability = math.log((pos_dict_TOTAL / testdata_TOTAL))  # .5041
    neg_prior_probability = math.log((neg_dict_TOTAL / testdata_TOTAL))  # .4958

    # grabbing a single review to use as a test to create the algorithm
    # review_test = sentiment.select_a_review("\'rw6205775\'")
    # review_test_clean = data_cleaning(review_test)
    # review_test = remove_stopwords(dict(generate_histogram(review_test_clean)))

    # print(review_test)

    db_manager.init_proc_table()

    # Looping though the DB grabbing
    movie_list_to_process = db_manager.select_all_reviews_to_list()
    for review in movie_list_to_process:  # steps though a list of lists of all teh reviews
        review_test_clean = data_cleaning([review[7]])  # grabs the 7th index containing the review cast's to a list to clean
        review_test = remove_stopwords(dict(generate_histogram(review_test_clean)))

        sentiment_score = sentiment_generator(review_test_clean,review_test, pos_dict, neg_dict, pos_dict_TOTAL, neg_dict_TOTAL, pos_prior_probability,neg_prior_probability)
        db_manager.insert_processed_review(review, sentiment_score)

    # testing searching in the positive and negative lists for matching keys

    # method below will return the score of the review to then be pushed into the DB

    # print(sentiment_generator(review_test, pos_dict, neg_dict, pos_dict_TOTAL, neg_dict_TOTAL, pos_prior_probability,
    #                         neg_prior_probability))

    # after compiling matching keys we can then get probabilities and do the algorithm :D
    # setting the value into a after-ML Table in the DB and iterate though the entire pre-ML data set
    # then we can tinker with accuracy -Dalton S.


"""             START OF PROGRAM                      """

main()
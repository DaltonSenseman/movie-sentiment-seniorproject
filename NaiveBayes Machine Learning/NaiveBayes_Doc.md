# ReviewSense NaiveBayes Doc
Machine learning algorithm used to generate sentiment analysis on movies reveiws

## data_cleaning(data)
Cleans the training data to not have punctuation and also be in all lowercase
  
**Params**
  
data: an array/list of strings 
  
**Returns** 
  
an array/list for strings 
  
## generate_histogram(string_list)
Creates a histogram of each occurrence of the word in the list  
  
**param**   
  
string_list: a list/array of words  
  
**return** 
  
a list of the words and how many times it appeared in the entire array/list ("word": value)  
  
## create_dictionary(database_connection, value)  
Creates the training data dictionary's by cleaning the data amd having a histogram made  
  
**param**  
  
database_connection: connection to the testdata SQL server connection  
value: what training data list to grab (0 for negative, 1 for positive)  
  
**return**  
  
a compiled dictionary   
  
## remove_stopwords(dictionary)  
Takes in a dictionary and compares it to a list of stopwords, if the stopword is in the dictionary it is removed.  
  
**param**  
  
dictionary: a dictionary of words to be checked in the tuple form (word : #) 
  
**return**   
  
the dictionary that has the words in the stopwords list removed from it.  
  
## sentiment_generator(review_data, test_data_pos, test_data_neg, pos_dict_TOTAL, neg_dict_TOTAL, pos_prior_probability, neg_prior_probability)  
Takes in a single review and checks it against the positive and negative data lists to generate the sentiment  
  
**param**  
  
neg_prior_probability: float value of the probability that a reveiw could be negative 
pos_prior_probability:  float value of the probability that a reveiw could be positive 
neg_dict_TOTAL: int value of the total number of words in the negative dictionary
pos_dict_TOTAL: int value of the total number of words in the positive dictionary
review_data: the review dictionary of the review we are creating the sentiment for  
test_data_pos: the positive dictionary of training data to check against for the ML  
test_data_neg: the negative dictionary of training data to check against for the ML  
  
**return**  
  
 will return the score of sentiment for that particular review (0 for negative 1 for positive) -1 is a placeholder for now  
                      

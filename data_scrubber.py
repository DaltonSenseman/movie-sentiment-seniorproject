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
    response = '(' + str(counter) + ',\'' + review + '\',' + str(sentiment) + ')'

    return response
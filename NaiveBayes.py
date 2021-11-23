from collections import Counter

from database_manager import SQLManager
import re


def training_data_cleaning(data):
    cleaned_list = []
    for content in data:
        changed_content = re.sub(r'[^\w\s]', '', str(content))
        cleaned_list.append(changed_content.strip().lower())

    return cleaned_list


sentiment = SQLManager()
result = sentiment.select_all_sentiment(0)

clean = training_data_cleaning(result)
large_concat = ' '.join(clean)
words = large_concat.split()
count_all = Counter(words)

print(count_all)

# for row in clean:
#     print(row)


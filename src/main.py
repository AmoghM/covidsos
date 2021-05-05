import ner
import tweet_extraction
from cleantext import clean
import re
import emoji
import nltk
# nltk.download('words')
words = set(nltk.corpus.words.words())

# def cleaner(tweet):
#     tweet = re.sub("@[A-Za-z0-9]+","",tweet) #Remove @ sign
#     tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", tweet) #Remove http links
#     tweet = " ".join(tweet.split())
#     tweet = ''.join(c for c in tweet if c not in emoji.UNICODE_EMOJI) #Remove Emojis
#     tweet = tweet.replace("#", "").replace("_", " ") #Remove hashtag sign but keep the text
#     tweet = " ".join(w for w in nltk.wordpunct_tokenize(tweet) \
#          if w.lower() in words or not w.isalpha())
#     return tweet

import datetime
print(" ==== TWEET EXTRACTION IN PROCESS ===")
startDate = datetime.datetime(2021, 5, 4, 0, 0, 0)
endDate =   datetime.datetime(2012, 5, 5, 1, 50, 0)

tweet_dump = tweet_extraction.get_tweets(search_words = "#pondiamoghkishangiri",#COVID19India", 
                                        date_since = "2021-05-04",
                                        size = 5)
# text = 'New Delhi is having a lot of cases. Help needed.'
 
print(" ==== TWEETS CLEANING IN PROCESS ===")
text_dump = [] #OXYGEN REFILL - Lucknow. Register at \n \n\nCylinders to be refilled as per oxygen level.…'
for i in tweet_dump:
    text_dump.append(i)


print(tweet_dump)
# print("\n")
# print(text_dump)

# print(" ==== TAGGING IN PROCESS ===")
# for text in text_dump:
#     classified_text = ner.get_ner(text)
#     print(classified_text)
#     for i in classified_text:
#         if i[1] == 'LOCATION':
#             print(i[0])

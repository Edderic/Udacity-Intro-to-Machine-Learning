#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        # temp_counter += 1
        # if temp_counter < 2:
        path = os.path.join('..', path[:-1])
        # print path
        email = open(path, "r")
        parsedOutText = parseOutText(email)
        # parsedOutText = 'sbaile2 nonprivilegedpst susan pleas send the forego list to richard thank sara shackleton enron wholesal servic 1400 smith street eb3801a houston tx 77002 ph 713 8535620 fax 713 6463490 reduced'
        ### use parseOutText to extract the text from the opened email

        ### use str.replace() to remove any instances of the words
        ### ["sara", "shackleton", "chris", "germani"]
        signature_words = ["sara", "shackleton", "chris", "germani",
                "sshacklensf", "cgermannsf"]
        for word in signature_words:
            parsedOutText = parsedOutText.replace(word, '')

        print parsedOutText

        ### append the text to word_data
        word_data.append(parsedOutText.strip())

        ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
        if name == 'sara':
            from_data.append(0)
        else:
            from_data.append(1)

        email.close()

print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )


### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit_transform(word_data)

pickle.dump( vectorizer, open("tfidf_vectorizer.pkl", "w") )

feature_names = vectorizer.get_feature_names()
num_unique_words_tfidf = len(feature_names)

print 'number of unique words in the Tfidf: ', num_unique_words_tfidf
print 'word number 34597 in Tfidf: ', feature_names[34597]

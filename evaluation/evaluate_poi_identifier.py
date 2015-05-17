#!/usr/bin/python


"""
    starter code for the evaluation mini-project
    start by copying your trained/tested POI identifier from
    that you built in the validation mini-project

    the second step toward building your POI identifier!

    start by loading/formatting the data

"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here

def true_positives(labels_test, predictions):
    num_true_positives = 0
    for index in range(0, len(labels_test)):
        if labels_test[index] == predictions[index] and labels_test[index] == 1.0:
            num_true_positives += 1
    return num_true_positives

from sklearn import cross_validation
from sklearn import tree
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, random_state=42, test_size=.3)

proper_clf = tree.DecisionTreeClassifier()
proper_clf.fit(features_train, labels_train)

print 'labels_test', labels_test
predictions = proper_clf.predict(features_test)
print 'predictions', predictions
print 'number of predicted POIs in the test set', reduce(lambda x,y: x+y, predictions)
print 'number of people total in the test set', len(predictions)
print 'number of true positives', true_positives(labels_test, predictions)
print 'precision_score: ', precision_score(labels_test, predictions)
print 'recall_score: ', recall_score(labels_test, predictions)

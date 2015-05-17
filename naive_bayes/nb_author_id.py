#!/usr/bin/python

"""
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project

    use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

# print features_train.shape[0]
# print features_test.shape[0]
def print_output(clf, features_train, features_test, labels_train, labels_test):
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    y_pred = clf.predict(features_test)
    print "prediction time:", round(time()-t1, 3), "s"

    print("Accuracy: %s" % (clf.score(features_test, labels_test)))
    # prettyPicture(clf, features_test, labels_test)

print_output(gnb, features_train, features_test, labels_train, labels_test)
#########################################################

#########################################################
### With SVM (rbf kernel)
# from sklearn.svm import SVC
# clf = SVC(kernel='linear')

# print_output(clf, features_train, features_test, labels_train, labels_test)
#########################################################

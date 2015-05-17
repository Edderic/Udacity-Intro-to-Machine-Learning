#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

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
# Speed up by only using 1% of the training set
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

def print_output(clf, features_train, features_test, labels_train, labels_test):
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t1 = time()
    y_pred = clf.predict(features_test)
    print "prediction time:", round(time()-t1, 3), "s"

    print("Accuracy: %s" % (clf.score(features_test, labels_test)))
    # prettyPicture(clf, features_test, labels_test)

# def print_prediction(clf, features_test, index):
    # print "prediction at %d: %d", index, clf.predict([features_test[index]])
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C=10000.)

print_output(clf, features_train, features_test, labels_train, labels_test)

#######################################
# Load serialized classifier
from sklearn.externals import joblib
joblib.dump(clf, 'rbf_c_10000.pkl')




# print_prediction(clf, features_test, 10)
# print_prediction(clf, features_test, 26)
# print_prediction(clf, features_test, 50)
#########################################################



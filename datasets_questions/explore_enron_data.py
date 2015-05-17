#!/usr/bin/python
from __future__ import division

"""
    starter code for exploring the Enron dataset (emails + finances)
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])

count = 0

# POIs
for key in enron_data.keys():
    if enron_data[key]['poi'] == 1:
        count += 1
print "Number of POIs:", count
print "Number of people in the data set:", len(enron_data)

# print 'keys:'
# for key in enron_data.keys():
    # print enron_data[key]

# Number of keys per person
# name = "SKILLING JEFFREY K"
# for key in enron_data[name].keys():
    # print key

# Total stock value of James Prentice
# SKILLING
# LAY
#
print "PRENTICE JAMES total_stock_value:",  enron_data["PRENTICE JAMES"]["total_stock_value"]
print "COLWELL WESLEY from_this_person_to_poi:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print "SKILLING JEFFREY K exercised_stock_options:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print "SKILLING JEFFREY K total_payments:", enron_data['SKILLING JEFFREY K']['total_payments']
print "FASTOW ANDREW S total_payments:", enron_data['FASTOW ANDREW S']['total_payments']
print "LAY KENNETH L total_payments:", enron_data['LAY KENNETH L']['total_payments']

# Number of people that have a quantified salary
quantified_salary_count = 0
for key in enron_data.keys():
    if enron_data[key]['salary'] != 'NaN':
        quantified_salary_count += 1

print "Number of quantified salaries:", quantified_salary_count

# Number of people that have a known email address
num_email_addresses = 0
for key in enron_data.keys():
    if enron_data[key]['email_address'] != 'NaN':
        num_email_addresses += 1

print "Number of known email addresses:", num_email_addresses

# Percentage of people who have "NaN" total_payments
num_nan_total_payments = 0

for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN':
        num_nan_total_payments += 1

print "Number of sample population that has NaN as total_payments:", num_nan_total_payments
print "Percentage of sample population that has NaN total payments:", num_nan_total_payments / len(enron_data)

num_poi_nan_total_payments = 0

for key in enron_data.keys():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] == 1:
        num_poi_nan_total_payments += 1


print "Number of sample POIs that have NaN total payments:", num_poi_nan_total_payments

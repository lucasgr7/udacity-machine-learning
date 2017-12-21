#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("final_project/final_project_dataset.pkl", "r"))
count = filter(lambda x: enron_data[x]['poi'] == 1, enron_data)


print("there is: " + str(len(count)))
known_salary = 0
knwon_mail = 0
k_poi_payments = 0
t_poi = 0
k_payments = 0
for p in enron_data:
    if 'FASTOW' in p:
        fastow_stock = enron_data[p]['total_stock_value']
    if 'LAY' in p:
        lay_stock = enron_data[p]['total_stock_value']
        print(enron_data[p])
    if enron_data[p]['salary'] != None and enron_data[p]['salary'] != 'NaN':
        known_salary += 1
    if enron_data[p]['email_address'] != None and enron_data[p]['email_address'] != 'NaN':
        knwon_mail += 1
    if enron_data[p]['poi']:
        t_poi += 1    
        if enron_data[p]['total_payments'] != None and enron_data[p]['total_payments'] != 'NaN':
            k_poi_payments += 1
    if enron_data[p]['total_payments'] != None and enron_data[p]['total_payments'] != 'NaN':
        k_payments += 1
pct_k_payments = (k_poi_payments * 100) / t_poi
print('emails: ' + str(knwon_mail) + ', known salaries: ' + str(known_salary) + ', list size: ' + str(len(enron_data)) + ' knwon total payments ' +str(pct_k_payments) + '%')
skilling_stock = enron_data['SKILLING JEFFREY K']['total_stock_value']

if fastow_stock > skilling_stock and fastow_stock > lay_stock:
    print('fastow ' + fastow_stock)
elif skilling_stock > fastow_stock and skilling_stock > lay_stock:
    print('skilling: ' + skilling_stock)
else:
    print('lay : ' + str(lay_stock))

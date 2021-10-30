'''
    ** This program checks if we can read the input and if each Text and Class 
    labels can be read via csv reader without error.
'''

import os
import csv
from os import listdir
from os.path import isfile, join


def read_csv(file_name):
    '''This function reads the csv file given by the file_name parameter'''
    try:
        file = open(file_name, 'r', newline='')
    except IOError:
        print('Cannot open the file <{}>'.format(file_name))
        raise SystemExit

    # csv_read will be a dataframe
    csv_read = csv.reader(file)
    
    return csv_read


def process_data(data,type):
    '''This function check if we are getting the same number of comments and the right text/labels
     and also separates the reports and labels into two different lists'''

    # reports and class labels will be stored here
    reports = []
    labels = []

    data = list(data)


    print(len(data))
    #print(data[28])

    if type=='pos':
        count = 0
        for line in data[0:]:

            try:
                report = line
                s = ""
                report_join = s.join(report)

                label ='positive'
                count += 1
            except:
                print('Data Parsing Error at line = {}'.format(count))
                raise SystemExit

            reports.append(report_join)
            labels.append(label)
        #print(reports[28])

    elif (type=='neg'):
        count = 0
        for line in data[0:]:

            # each line in the categorical 'data' is of 2 elements -> UM, REPORT
            try:
                report = line
                s=""
                report_join=s.join(report)
                label = 'negative'
                count += 1
            except:
                print('Data Parsing Error at line = {}'.format(count))
                raise SystemExit
            reports.append(report_join)
            labels.append(label)



    return reports, labels







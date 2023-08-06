import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.model_selection import train_test_split # will be used for data split
from sklearn.preprocessing import LabelEncoder # for preprocessing
from sklearn.ensemble import RandomForestClassifier # for training the algorithm
from sklearn.ensemble import ExtraTreesClassifier # for training the algorithm
import joblib # for saving algorithm and preprocessing objects
from .models import Guardian, Patient, Question, Answer, Result, Category
from functools import reduce
import csv
import os
from django.http import HttpResponse

def generateData (data):
    # guardianid = data.guardianid
    # patientid = data.patientid
    # return print(data)
    guardianemail = data['guardianemail']
    patient_fname = data['patient_fname']
    patient_lname = data['patient_lname']
    category = data['category']
    # categoryid = data.category_id
    negative_length=data['negative_length']
    positive_length=data['positive_length']
    answer_timestamp=data['answer_timestamp']

    # result = Guardian.objects.get(guardian_id=guardianid, patient_id=patientid, category_id=categoryid)

    numbering = "1"

    patient_id_part1 = "PASD"

    patient_id = patient_id_part1 + numbering

    ml = {
        "id": [patient_id],
        "category": [category],
        "first_name": [patient_fname],
        "last_name": [patient_lname],
        "guardian": [guardianemail],
        "negative": [negative_length],
        "positive": [positive_length],
        "timestamp": [answer_timestamp],
        "asd_status": [0],
    }

    # return ml

    # df = pd.DataFrame([ml['category'], ml['first_name'], ml['last_name'], ml['guardian'], ml['negative'], ml['positive'], ml['timestamp'], ml['asd_status']], columns=list("category", "first_name", "last_name", "guardian", "negative", "positive", "timestamp", "asd_status"))


    df = pd.DataFrame(ml)

    outfile = 'asd.csv'

    outdir = './csv'

    patient_id_arr = []

    df.set_index('id')

    if os.path.exists(outdir) != True:
        os.mkdir(outdir)
    else:
        fullpath = os.path.join(outdir, outfile)

        # check if file exists and create it if it does not

        if not os.path.isfile(fullpath):
            df.index = [1]
            df.to_csv(fullpath)
        else:
            open_file = open(fullpath, 'r')

            last_index = 0
            first_index = []
            index_status = False

            cols = []

            global last_item

            with open_file as asd:
                next(asd, None) # skip header
                read_csv = csv.reader(asd, delimiter=',')
                # last_item_index = read_csv.index(row[-1])
                for index, row in enumerate(read_csv):
                    get_index = row[1]
                    f_index = row[0]
                    int_to_str = get_index # ('').join(get_index)
                    patient_id_arr.append(int_to_str)
                    first_index.append(f_index)

            open_file.close()
            
            delimeter = ''

            # get the last index in a row
            last_index = patient_id_arr[-1]
            first_index_last_item = first_index[-1]
            extract_int = delimeter.join([str(i) for i in last_index if i.isdigit()])

            # return extract_int

            last_item = int(extract_int) + 1

            new_first_index_col = int(first_index_last_item) + 1

            new_patient_index = patient_id_part1 + str(last_item)

            df.id = [new_patient_index]
            df.index = [new_first_index_col]

            # return last_item
            # if type(last_item) is int:
            # df.index = last_item + df.index
            df.to_csv(fullpath, mode='a', header=False)
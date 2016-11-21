import csv
import numpy as np
import uuid
import hashlib
import time
import math
from random import randint

## Parameters
train_to_read = 'negated_train.csv'
test_to_read = 'negated_test.csv'
##

matrix = []
matrix_cross_validation = []
amount_of_reviews_for_prediction = [0 for x in range(5)]
word_presence = [0 for x in range(6)]
word_presence[0] = {'' : 0}
word_presence[1] = {'' : 0}
word_presence[2] = {'' : 0}
word_presence[3] = {'' : 0}
word_presence[4] = {'' : 0}
word_presence[5] = {}
word_presence[5]['1'] = 0
word_presence[5]['2'] = 0
word_presence[5]['3'] = 0
word_presence[5]['4'] = 0
word_presence[5]['5'] = 0

with open(train_to_read) as csvReadfile:
    reader = csv.DictReader(csvReadfile)

    for row in reader:
        number_to_predict = int(row['Prediction'].split()[0])

        for word in row['Text'].split():
            if word in word_presence[number_to_predict - 1]:
                word_presence[number_to_predict - 1][word] += 1
            else:
                word_presence[number_to_predict - 1][word] = 1

        word_presence[5][str(number_to_predict)] += 1

        amount_of_reviews_for_prediction[number_to_predict - 1] += 1

with open(test_to_read) as csvReadfile2:
    with open('prediction.csv', 'w') as csvWritefile:
        fieldnames = ['Id', 'Prediction']
        writer = csv.DictWriter(csvWritefile, fieldnames=fieldnames)
        writer.writeheader()
        reader = csv.DictReader(csvReadfile2)
        for row in reader:
            probability_of_one_star = 1
            probability_of_two_stars = 1
            probability_of_three_stars = 1
            probability_of_four_stars = 1
            probability_of_five_stars = 1

            for word in row['Text'].split():
                if word in word_presence[0]:
                    probability_of_one_star = probability_of_one_star * (float(word_presence[0][word]) / word_presence[5]['1'])
                if word in word_presence[1]:
                    probability_of_two_stars = probability_of_two_stars * (float(word_presence[1][word]) / word_presence[5]['2'])
                if word in word_presence[2]:
                    probability_of_three_stars = probability_of_three_stars * (float(word_presence[2][word]) / word_presence[5]['3'])
                if word in word_presence[3]:
                    probability_of_four_stars = probability_of_four_stars * (float(word_presence[3][word]) / word_presence[5]['4'])
                if word in word_presence[4]:
                    probability_of_five_stars = probability_of_five_stars * (float(word_presence[4][word]) / word_presence[5]['5'])

            probability_of_one_star = float(probability_of_one_star * amount_of_reviews_for_prediction[0])
            probability_of_two_stars = float(probability_of_two_stars * amount_of_reviews_for_prediction[1])
            probability_of_three_stars = float(probability_of_three_stars * amount_of_reviews_for_prediction[2])
            probability_of_four_stars = float(probability_of_four_stars * amount_of_reviews_for_prediction[3])
            probability_of_five_stars = float(probability_of_five_stars * amount_of_reviews_for_prediction[4])

            if probability_of_one_star > probability_of_two_stars and probability_of_one_star > probability_of_three_stars and probability_of_one_star > probability_of_four_stars and probability_of_one_star > probability_of_five_stars:
                predicted = 1
            if probability_of_two_stars > probability_of_one_star and probability_of_two_stars > probability_of_three_stars and probability_of_two_stars > probability_of_four_stars and probability_of_two_stars > probability_of_five_stars:
                predicted = 2
            if probability_of_three_stars > probability_of_one_star and probability_of_three_stars > probability_of_two_stars and probability_of_three_stars > probability_of_four_stars and probability_of_three_stars > probability_of_five_stars:
                predicted = 3
            if probability_of_four_stars > probability_of_one_star and probability_of_four_stars > probability_of_two_stars and probability_of_four_stars > probability_of_three_stars and probability_of_four_stars > probability_of_five_stars:
                predicted = 4
            if probability_of_five_stars > probability_of_one_star and probability_of_five_stars > probability_of_two_stars and probability_of_five_stars > probability_of_three_stars and probability_of_five_stars > probability_of_four_stars:
                predicted = 5

            csvWritefile.write('%s,' % row['Id'])
            csvWritefile.write('%s' % predicted)
            csvWritefile.write('\n')

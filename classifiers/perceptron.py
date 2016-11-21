import csv
import numpy as np
import uuid
import hashlib
import time
import math
from random import randint

## Activation Functions
def tanh(x):
    return np.tanh(x)

def dtanh(x):
    y = tanh(x)
    return 1 - y*y

def sigmoid(gamma):
    return (1 - 1 / (1 + math.exp(gamma))) if gamma < 0 else (1 / (1 + math.exp(-gamma)))

def softmax(x):
    e = np.exp(x - np.amax(x))
    out = []
    for e1 in e:
        out.append(e1 / np.sum(e1))
    return np.array(out)

def sigv2(x):
    return (1 / (1 + np.exp(x))) if x < 0 else (1 / (1 + np.exp(-x)))
##

## Parameters
train_to_read = 'sparktrain2.csv'
prime_number = 7
number_of_laps = 10

def function(x):
    return sigmoid(x)

def calculate_discrete_value_for_continue_value(x):
    return 1 if x >= 0 else 0
##

matrix = []
weights = []
predictions = []
number_of_dimension = prime_number

print ('start reading csv file')
start_time = time.time()
with open(train_to_read) as csvReadfile:
    reader = csv.DictReader(csvReadfile)

    row_count = 0
    for row in reader:
        hash_array = [0] * prime_number

        text = row['Text']
        for word in text.split():
            hashed_number = int(hash(word.encode()) % prime_number)
            hash_array[hashed_number] += 1

        matrix.append([0 for x in range(3)])
        matrix[row_count][0] = row['Id'].split()[0]
        number_to_predict = int(row['Prediction'].split()[0])
        if number_to_predict == 1 or number_to_predict == 2:
            matrix[row_count][1] = 0
        else:
            matrix[row_count][1] = 1
        matrix[row_count][2] = hash_array

        row_count += 1

end_time = time.time()
hours, rem = divmod(end_time - start_time, 3600)
minutes, seconds = divmod(rem, 60)
print("finished reading csv file in {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

weights = [0 for col in range(number_of_dimension)]
predictions = [0 for col in range(row_count)]

weights = np.array(weights)

print ('start predicting')
start_time = time.time()

for i in range(number_of_laps):
    for row in range(row_count):
        y = function(weights.dot(matrix[row][2]))
        predictions[row] = y

        for col in range(prime_number):
            weights[col] = weights[col] + (matrix[row][1] - y) * matrix[row][2][col]

end_time = time.time()
hours, rem = divmod(end_time - start_time, 3600)
minutes, seconds = divmod(rem, 60)
print("finished predicting in {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))

predicted_correctly = 0
for row in range(row_count):
    if matrix[row][1] == calculate_discrete_value_for_continue_value(predictions[row]):
        predicted_correctly += 1
#    print ('to predict %s predicted %s \n' % (matrix[row][1], predictions[row]))

print ('predict correctamente %s' % predicted_correctly)
print ('total %s'% row_count)
print ('total %s porciento'% (predicted_correctly * 1.0 / row_count * 100))

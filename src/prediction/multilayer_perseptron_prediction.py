from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

import csv

clf = joblib.load('newral_network.pkl')

correctPredictions = 0
totalRegisters = 0

# Open the file with the registers
with open("../../matrix_of_word_frequency.csv", "r") as csvfile:
    firstValue = True
    for row in csv.reader(csvfile):
        if firstValue:
            firstValue = False
            continue

        register = [[float(x) for x in row[2::]]]
        prediction = float(row[1])

        totalRegisters += 1
        if prediction == clf.predict(register):
            correctPredictions +=1

print correctPredictions, totalRegisters

from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

import csv

# Matrix of registers
registers = []

# Array of predictions in the same order that the matrix of registers
predictions = []

# Open the file with the registers
with open("../../matrix_of_word_frequency.csv", "r") as csvfile:
    firstValue = True
    for row in csv.reader(csvfile):
        if firstValue:
            firstValue = False
            continue

        register = [float(x) for x in row[2::]]
        prediction = float(row[1])

        registers.append(register)
        predictions.append(prediction)


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 75, 50), random_state=1)

clf.fit(registers, predictions)

joblib.dump(clf, 'newral_network.pkl')

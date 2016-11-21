from sklearn.neural_network import MLPClassifier
from sklearn.externals import joblib

import csv
import random as rd

# Matrix of registers
registers = []

# Array of predictions in the same order that the matrix of registers
predictions = []

# Open the file with the registers
with open("../../data/matrixtrainsummarytextshin2.csv", "r") as csvfile:
    firstValue = True
    for row in csv.reader(csvfile):
        if firstValue:
            firstValue = False
            continue

        register = [float(x) for x in row[2::]]
        prediction = float(row[1])

        registers.append(register)
        predictions.append(prediction)



activations = ['identity', 'logistic', 'tanh']
solvers = ['lbfgs', 'sgd', 'adam']
learning_rates = ['constant', 'invscaling', 'adaptive']


for i in xrange(1):
    activation = activations[rd.randrange(len(activations))]
    solver = solvers[rd.randrange(len(solvers))]
    learning_rate = learning_rates[rd.randrange(len(learning_rates))]

    layers = tuple([rd.randrange(10, 100) for x in xrange(rd.randrange(1, 10))])
    alpha = 1 / float(rd.randrange(1, 100000))
    momentum = 900 / float(rd.randrange(901, 1400))
    beta_1 = 900 / float(rd.randrange(901, 1400))
    beta_2 = 900 / float(rd.randrange(901, 1000)) #Closer to 0.999

    activation = activations[1]
    solver = solvers[2]
    learning_rate = learning_rates[2]

    layers = tuple([45 for x in xrange(4)])
    alpha = 0.0001
    momentum = 0.9
    beta_1 = 0.9
    beta_2 = 0.999 #Closer to 0.999
    max_iter = 25

    print "Start training net", i, "params : "
    print "activation :", activation
    print "solver :", solver
    print "learning_rate :", learning_rate
    print "layers :", layers
    print "alpha :", alpha
    print "momentum :", momentum
    print "beta_1 :", beta_1
    print "beta_2 :", beta_2


    clf = MLPClassifier(activation=activation, solver=solver, alpha=alpha, hidden_layer_sizes=layers, \
    learning_rate=learning_rate, momentum=momentum, beta_1=beta_1, beta_2=beta_2,\
    random_state=1, verbose=True, max_iter=max_iter)

    clf.fit(registers, predictions)
    joblib.dump(clf, 'newral_networks/newral_network_probably_under_fitted' + '.pkl')

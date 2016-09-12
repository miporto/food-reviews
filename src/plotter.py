import matplotlib.pyplot as plt
import csv


def plot(data):
    values = []

    for key in data:
        values.append(key[1])

    plt.plot(range(len(data)), values)
    plt.ylabel('some numbers')
    plt.show()

with open('../csv/sorted_words_by_prediction_5_stemmed.csv', 'rb') as csvfile:
    

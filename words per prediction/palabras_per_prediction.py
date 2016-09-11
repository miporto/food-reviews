import csv
import operator
import matplotlib.pyplot as plt

# Indexes
IdIndex = 0
ProductIdIndex = 1
UserIdIndex = 2
ProfileNameIndex = 3
HelpfulnessNumeratorIndex = 4
HelpfulnessDenominatorIndex = 5
PredictionIndex = 6
TimeIndex = 7
SummaryIndex = 8
TextIndex = 9

# IdIndex = 0
# SummaryIndex = 1
# TextIndex = 2
# PredictionIndex = 3

def plot(data):
    values = []

    for key in data:
        values.append(key[1])

    plt.plot(range(len(data)), values)
    plt.ylabel('some numbers')
    plt.show()

with open('food-reviews/csv/train.csv', 'rb') as csvfile:
    # Read csv file
    reader = csv.reader(csvfile)

    # Final dictionary with word ranking
    wordsByPrediction = {1 : {}, 2 : {}, 3 : {}, 4 : {}, 5 : {}}

    # First line is of labels
    reader.next()

    # Iteration of all reviews
    for review in reader:
        # prediction of review
        prediction = int(review[PredictionIndex])

        reviewWordsInText = review[TextIndex].split()

        for word in reviewWordsInText:
            if wordsByPrediction[prediction].has_key(word):
                wordsByPrediction[prediction][word] = wordsByPrediction[prediction][word] + 1
            else:
                wordsByPrediction[prediction][word] = 1

    sortedPrediction1 = reversed(sorted(wordsByPrediction[1].items(), key=operator.itemgetter(1)))
    sortedPrediction2 = reversed(sorted(wordsByPrediction[2].items(), key=operator.itemgetter(1)))
    sortedPrediction3 = reversed(sorted(wordsByPrediction[3].items(), key=operator.itemgetter(1)))
    sortedPrediction4 = reversed(sorted(wordsByPrediction[4].items(), key=operator.itemgetter(1)))
    sortedPrediction5 = reversed(sorted(wordsByPrediction[5].items(), key=operator.itemgetter(1)))

    with open('sorted_words_by_prediction_1.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in sortedPrediction1:
            spamwriter.writerow(row)

    with open('sorted_words_by_prediction_2.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in sortedPrediction2:
            spamwriter.writerow(row)

    with open('sorted_words_by_prediction_3.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in sortedPrediction3:
            spamwriter.writerow(row)

    with open('sorted_words_by_prediction_4.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in sortedPrediction4:
            spamwriter.writerow(row)

    with open('sorted_words_by_prediction_5.csv', 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in sortedPrediction5:
            spamwriter.writerow(row)




    # plot(sortedPrediction5)

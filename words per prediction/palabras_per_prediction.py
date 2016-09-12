import csv
import operator

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

# Writes data into a csv with a name
def writeDataAsCSV(data, name):
    with open(name, 'w') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for row in data:
            spamwriter.writerow(row)


with open('../csv/train.csv', 'rb') as csvfile:
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

    writeDataAsCSV(sortedPrediction1, 'hola.csv')
    # writeDataAsCSV(sortedPrediction2, 'sorted_words_by_prediction_2.csv')
    # writeDataAsCSV(sortedPrediction3, 'sorted_words_by_prediction_3.csv')
    # writeDataAsCSV(sortedPrediction4, 'sorted_words_by_prediction_4.csv')
    # writeDataAsCSV(sortedPrediction5, 'sorted_words_by_prediction_5.csv')


    # plot(sortedPrediction5)

#reverse the order of a list
def reverseData(data):
    return  reversed(sorted(data.items(), key=operator.itemgetter(1)))

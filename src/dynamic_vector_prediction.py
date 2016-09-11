
import csv
import preprocess
from scipy import spatial


# Constants
testTextIndex = 8

# Vector prediction charges all the word ranking per prediction in memory
# and

# Make a Dictionary from csv files with key, value, format
def getDictionaryWithCsvName(name):
    with open(name, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        wordRanking = {}

        for row in reader:
            wordRanking[row[0]] = int(row[1])

        return wordRanking

def dynamicVectorWithText(text):
    preprocessSplittedText = preprocess.preprocess_text(text).split()

    dynamicVectorReference = []
    dynamicVector = []
    auxDictionary = {}

    for word in preprocessSplittedText:
        if word in auxDictionary:
            auxDictionary[word] = auxDictionary[word] + 1
        else :
             auxDictionary[word] = 1
             dynamicVectorReference.append(word)

    totalWords = len(preprocessSplittedText)
    for word in dynamicVectorReference:
        wordValue = auxDictionary[word] / float(totalWords)

        dynamicVector.append(wordValue)


    return (dynamicVectorReference, dynamicVector)

def dynamicVectorWithReferenceAndWordRanking(reference, wordRanking):
    dynamicVector = []

    totalRankingValues = 0

    for word in reference:
        if word in wordRanking:
            dynamicVector.append(wordRanking[word])
            totalRankingValues = totalRankingValues + wordRanking[word]
        else :
            dynamicVector.append(0)

    for index in range(len(dynamicVector)):
        # If any word is in my ranking, then is imposible to predict
        # a random vecotr would be a better solution
        if (totalRankingValues == 0):
            dynamicVector.append(0)

        dynamicVector[index] = dynamicVector[index] / float(totalRankingValues)

    return dynamicVector

# Excecute the prediction
def main():
    wordRankingPrediction1 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_1_stemmed.csv')
    wordRankingPrediction2 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_2_stemmed.csv')
    wordRankingPrediction3 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_3_stemmed.csv')
    wordRankingPrediction4 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_4_stemmed.csv')
    wordRankingPrediction5 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_5_stemmed.csv')

    with open('../csv/test.csv') as testCsv:
        reader = csv.reader(testCsv)
        reader.next()

        predictions = []

        i = 0

        for review in reader:
            reviewText = review[testTextIndex]

            dynamicVector = dynamicVectorWithText(reviewText)

            dynamicVectorFromPrediction1 = dynamicVectorWithReferenceAndWordRanking(dynamicVector[0], wordRankingPrediction1)
            dynamicVectorFromPrediction2 = dynamicVectorWithReferenceAndWordRanking(dynamicVector[0], wordRankingPrediction2)
            dynamicVectorFromPrediction3 = dynamicVectorWithReferenceAndWordRanking(dynamicVector[0], wordRankingPrediction3)
            dynamicVectorFromPrediction4 = dynamicVectorWithReferenceAndWordRanking(dynamicVector[0], wordRankingPrediction4)
            dynamicVectorFromPrediction5 = dynamicVectorWithReferenceAndWordRanking(dynamicVector[0], wordRankingPrediction5)

            distanceToPrediction1 = spatial.distance.cosine(dynamicVector[1], dynamicVectorFromPrediction1)
            distanceToPrediction2 = spatial.distance.cosine(dynamicVector[1], dynamicVectorFromPrediction2)
            distanceToPrediction3 = spatial.distance.cosine(dynamicVector[1], dynamicVectorFromPrediction3)
            distanceToPrediction4 = spatial.distance.cosine(dynamicVector[1], dynamicVectorFromPrediction4)
            distanceToPrediction5 = spatial.distance.cosine(dynamicVector[1], dynamicVectorFromPrediction5)

            distances = [distanceToPrediction1, distanceToPrediction2, distanceToPrediction3, distanceToPrediction4, distanceToPrediction5]
            minDistance = min(distances)
            indexOfMinDistance = distances.index(minDistance) + 1
            predictions.append(indexOfMinDistance)

            print("pregress", i, "prediction", indexOfMinDistance)
            i = i + 1


        with open("dynamic_predictions.csv", 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

            writer.writerow(["Id", "Prediction"])

            for index in range(len(predictions)):
                writer.writerow([index, predictions[index]])


if __name__ == "__main__":
    main()

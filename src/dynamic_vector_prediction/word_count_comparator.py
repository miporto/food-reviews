import csv


def getDictionaryWithCsvName(name):
    with open(name, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        wordRanking = {}

        for row in reader:
            wordRanking[row[0]] = int(row[1])

        return wordRanking

def normalizedWordWithDataAndWord(data, word):
        total = 0

        for key in data:
            total += data[word]

        print(data[word], total)

def main():
    wordRankingPrediction1 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_1_stemmed.csv')
    wordRankingPrediction2 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_2_stemmed.csv')
    wordRankingPrediction3 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_3_stemmed.csv')
    wordRankingPrediction4 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_4_stemmed.csv')
    wordRankingPrediction5 = getDictionaryWithCsvName('../csv/sorted_words_by_prediction_5_stemmed.csv')

    word = 'tast'

    normalizedWordWithDataAndWord(wordRankingPrediction1, word)
    normalizedWordWithDataAndWord(wordRankingPrediction2, word)
    normalizedWordWithDataAndWord(wordRankingPrediction3, word)
    normalizedWordWithDataAndWord(wordRankingPrediction4, word)
    normalizedWordWithDataAndWord(wordRankingPrediction5, word)



if __name__ == "__main__":
    main()

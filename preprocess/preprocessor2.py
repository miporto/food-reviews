import csv
import numpy as np

train_to_read = 'sparktrain.csv'

with open(train_to_read) as csvReadfile:
    with open('sparktrain2.csv', 'w') as csvWritefile:
        fieldnames = ['ProductId', 'Prediction', 'Text']
        writer = csv.DictWriter(csvWritefile, fieldnames=fieldnames)
        writer.writeheader()
        reader = csv.DictReader(csvReadfile)

        for row in reader:
            csvWritefile.write('%s,' % row['ProductId'])
            csvWritefile.write('%s,' % row['Prediction'])
            text = row['Summary'] + ' ' +row['Text']
            text = text.replace("n't", " not").replace(".", " . ")
            csvWritefile.write('%s,' % text)
            csvWritefile.write('\n')

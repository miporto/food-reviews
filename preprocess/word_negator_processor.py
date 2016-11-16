import csv

train_to_read = 'train.csv'

with open(train_to_read) as csvReadfile:
    with open('negated_train.csv', 'w') as csvWritefile:
        fieldnames = ['ProductId', 'Prediction', 'Summary', 'Text']
        writer = csv.DictWriter(csvWritefile, fieldnames=fieldnames)
        writer.writeheader()
        reader = csv.DictReader(csvReadfile)

        for row in reader:
            should_negate_word = False
            text = ''
            text_to_read = row['Summary'] + ' . ' + row['Text']
            for word in text_to_read.split():
                if word == 'not' or word == 'no' or word == 'n\'t':
                    should_negate_word = not should_negate_word
                elif word == '.':
                    should_negate_word = False
                elif should_negate_word:
                    text += 'not_' + word + ' '
                else:
                    text += word + ' '

            csvWritefile.write('%s,' % row['ProductId'])
            csvWritefile.write('%s,' % row['Prediction'])
            for word in text:
                csvWritefile.write('%s' % word)
            csvWritefile.write('\n')

import csv
import uuid
import hashlib

train_to_read = 'train.csv'
prime_number = 127
salt = uuid.uuid4().hex

with open(train_to_read) as csvReadfile:
    with open('matrix_of_word_frequency.csv', 'w') as csvWritefile:
        fieldnames = ['ProductId', 'Prediction']
        writer = csv.DictWriter(csvWritefile, fieldnames=fieldnames)

        writer.writeheader()
        reader = csv.DictReader(csvReadfile)

        for row in reader:
            hash_array = [0] * prime_number

            text = row['Summary'] + row['Text']
            for word in text.split():
                hashed_number = (int(hashlib.sha256(salt.encode() + word.encode()).hexdigest(), 16) % prime_number)
                hash_array[hashed_number] += 1

            csvWritefile.write('%s,' % row['ProductId'].split()[0])
            csvWritefile.write('%s' % row['Prediction'].split()[0])

            for i in range(0, prime_number):
                csvWritefile.write(',%s' % str(hash_array[i]))
            csvWritefile.write('\n')

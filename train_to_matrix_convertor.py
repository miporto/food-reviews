import csv
import uuid

def word2matrix(train_to_read, output, test=False):
	prime_number = 127
	salt = uuid.uuid4().hex

	with open(train_to_read) as csvReadfile:
		with open(output, 'w') as csvWritefile:
			if (test):
				fieldnames = ['Id']	
			else:
				fieldnames = ['Id', 'Prediction']
			writer = csv.DictWriter(csvWritefile, fieldnames=fieldnames)

			writer.writeheader()
			reader = csv.DictReader(csvReadfile)

			for row in reader:
				hash_array = [0] * prime_number

				text = row['Summary'] + row['Text']
				for word in text.split():
					hashed_number = int(hash(word.encode()) % prime_number)
					hash_array[hashed_number] += 1

				csvWritefile.write('%s' % row['Id'].split()[0])
				
				if (not test):
					csvWritefile.write(',%s' % row['Prediction'].split()[0])

				for i in range(0, prime_number):
					csvWritefile.write(',%s' % str(hash_array[i]))
				csvWritefile.write('\n')

word2matrix("data/sparktest.csv", "data/matrixtest.csv", test=True)

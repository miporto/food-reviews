# WORD2MATRIX
# test example: python word2matrix.py testinput.csv testoutput.csv test
# train example: python word2matrix.py traininput.csv trainoutput.csv train

import sys
import csv

import uuid

SUMMARY_W = 2
def hashing_trick_summarytext(train_to_read, output, test=False):
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

def hashing_trick_summary2_text(train_to_read, output, test=False):
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

				for word in row['Summary'].split():
					hashed_number = int(hash(word.encode()) % prime_number)
					hash_array[hashed_number] += SUMMARY_W

				for word in row['Text'].split():
					hashed_number = int(hash(word.encode()) % prime_number)
					hash_array[hashed_number] += 1

				csvWritefile.write('%s' % row['Id'].split()[0])
				
				if (not test):
					csvWritefile.write(',%s' % row['Prediction'].split()[0])

				for i in range(0, prime_number):
					csvWritefile.write(',%s' % str(hash_array[i]))
				csvWritefile.write('\n')
input_file = sys.argv[1]
output_file = sys.argv[2]
if sys.argv[3] == "test":
	test = True
else:
	test = False

hashing_trick_summarytext(input_file, output_file, test=test)

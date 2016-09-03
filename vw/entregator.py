with open("rotten.preds.txt") as f:
	with open('preds.csv', 'w') as p:
		p.write("Id,Prediction\n")
		content = f.readlines()
			
		for line in content:
			row = line.split()
			p.write((",").join(row[::-1]) + "\n")

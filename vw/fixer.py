with open("csv2vwtest.vw") as f:
	with open('test.vw', 'w') as new_f:
		content = f.readlines()
		
		for line in content:
			line = line.replace("Summary:","")
			line = line.replace("Text:","| ")
			new_f.write(line)

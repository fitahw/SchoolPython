with open('log_file_zad8.1.txt', 'r+').readlines() as f:
	names = []
	for lineNum in range(0, len(f)):
		line = f[lineNum]
		if '[INFO]' in line:
			names.append(line.split("'")[1::2])
print(names)

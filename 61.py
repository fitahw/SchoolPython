import os

def fileTree(path):
	for folder, subfolder, files in os.walk(path):
		level = folder.count(os.sep) - path.count(os.sep)
		indent = '	' * level
		print(f'{indent}[{os.path.basename(folder)}]')
		for file in files:
			print(f"{indent}	-{file}")

fileTree(input(print("Podaj sciezke do folderu: ")))
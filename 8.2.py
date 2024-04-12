class Adder:

	def add(self, list1, list2):
		return list1 + list2

class Saver:

	def save(self, filename, listAdded):
		# Skrypt otwiera i nadpisuje dane, jesli chcemy zachowac dane powinnismy
		# wczytac plik txt (open(-, 'r')).readlines() a potem dodac do tych linii nasze listy
		with open(filename, 'w+') as f:
			for line in listAdded:
				f.write(f'{line}\n')

class Kalkulator:
	def __init__(self):
		self.adder = Adder()
		self.saver = Saver()

	def kalkuluj(self, list1, list2, filename):
		self.saver.save(filename, self.adder.add(list1, list2))

kalkulator = Kalkulator()
lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'g']
kalkulator.kalkuluj(lista, lista2, 'listy.txt')
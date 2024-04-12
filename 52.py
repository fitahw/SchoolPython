class Osoba:
	def __init__(self, name, surname, birth, ID):
		self.name = name
		self.surname = surname
		self.birth = birth
		self.ID = ID

	def displayInfo(self):
		print(f"""Imie: {self.name} {self.surname}
Data urodzenia: {self.birth}
Numer dowodu: {self.ID}""")

class Student(Osoba):
	def __init__(self, name, surname, birth, ID, uniStartYear, uniEndYear, uniCurrentYear, active, course):
		super().__init__(name, surname, birth, ID)
		self.uniStartYear = uniStartYear
		self.uniEndYear = uniEndYear
		self.uniCurrentYear = uniCurrentYear
		self.active = active
		self.course = course
		self.listaOcen = ListaOcen()

	def displayInfoStudent(self):
		self.displayInfo()
		print(f"""Rok rozpoczecia: {self.uniStartYear}
Rok zakonczenia: {self.uniEndYear}
Rok Studiow: {self.uniCurrentYear}
Aktywny: {self.active}
Kierunek studiow: {self.course}""")
		{self.listaOcen.wyswietlOceny()}

	def setListaOcen(self, lista):
		self.listaOcen = lista

class Pracownik(Osoba):
	def __init__(self, name, surname, birth, ID, workStartYear, jobTime, jobPosition, sickLeave):
		super().__init__(name, surname, birth, ID)
		self.workStartYear = workStartYear
		self.jobTime = jobTime
		self.jobPosition = jobPosition
		self.sickLeave = sickLeave

	def displayInfoPracownik(self):
		self.displayInfo()
		print(f"""Start zatrudnienia: {self.workStartYear}
			Staz pracy: {self.jobTime}
			Stanowisko: {self.jobPosition}
			Zwolnienie lekarskie: {self.sickLeave}""")

class Menager(Pracownik):
	def __init__(self, name, surname, birth, ID, workStartYear, jobTime, jobPosition, sickLeave, oddzial, workerCount):
		super().__init__(workStartYear, jobTime, jobPosition, sickLeave)
		self.oddzial = oddzial
		self.workerCount = workerCount

	def displayInfoMenager(self):
		self.displayInfoPracownik()
		print(f"""Oddzial: {self.oddzial}
			Ilosc pracownikow: {self.workerCount}""")

class ListaOcen(dict):
	def dodajPrzedmiot(self, nazwa_przedmiotu):
		self[f'{nazwa_przedmiotu}'] = input(f"Podaj ocene dla przedmiotu {nazwa_przedmiotu}") 
	def usunPrzedmiot(self, nazwa_przedmiotu):
		del self[f'{nazwa_przedmiotu}']
	def szukajPrzedmiot(self, nazwa_przedmiotu):
		self.get(f'{nazwa_przedmiotu}')
	def wyswietlOceny(self):
		print(self)

class ListaStudentow(dict):
	def dodajStudenta(self, index, studentParam):
		self[index] = studentParam
	def usunStudenta(self, index):
		del self[index]
	def znajdzStudenta(self, index):
		print(f'{self.get(index)}')
	def pokazStudentow(self):
		for indeks, student in self.items():
			student.displayInfoStudent()
	def pokazOceny(self, index):
		print(f"{self[index].listaOcen}")

listaSt = ListaStudentow({})
oceny = {'polski': 3, 'angielski': 5, 'matematyka': 4}
lista = ListaOcen(oceny)
student = Student('Adrian', 'Nowak', '20000', '1000000', '2010', '2014', '2', 'aktywny', 'informatyka')
listaSt.dodajStudenta(1, student)
student.setListaOcen(lista)
listaSt.pokazStudentow()

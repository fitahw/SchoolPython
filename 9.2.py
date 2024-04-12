students = [
    {'imie': 'Artur', 'nazwisko': 'Kowalczyk', 'matematyk': 5.0, 'fizyka': 4.5, 'informatyka': 4.0, 'elektryka': 3.0, 'egzamin koncowy': 4.0, 'obrona': 3.0},
    {'imie': 'Joanna', 'nazwisko': 'Sikora', 'matematyk': 3.0, 'fizyka': 3.5, 'informatyka': 4.0, 'elektryka': 4.0, 'egzamin koncowy': 3.0, 'obrona': 5.0},
    {'imie': 'Janusz', 'nazwisko': 'Adamczyk', 'matematyk': 3.5, 'fizyka': 4.0, 'informatyka': 3.5, 'elektryka': 3.0, 'egzamin koncowy': 4.0, 'obrona': 4.0},
    {'imie': 'Ewa', 'nazwisko': 'Siwinska', 'matematyk': 4.5, 'fizyka': 3.5, 'informatyka': 4.5, 'elektryka': 4.5, 'egzamin koncowy': 5.0, 'obrona': 5.0},
    {'imie': 'Radek', 'nazwisko': 'Smalec', 'matematyk': 4.0, 'fizyka': 4.5, 'informatyka': 3.0, 'elektryka': 5.0, 'egzamin koncowy': 4.0, 'obrona': 4.0},
    {'imie': 'Wiktoria', 'nazwisko': 'Kaszka', 'matematyk': 5.0, 'fizyka': 5.0, 'informatyka': 4.5, 'elektryka': 4.0, 'egzamin koncowy': 3.0, 'obrona': 3.0},
]

sortedStudents = sorted(students, key=lambda a: 0.2 * a['egzamin koncowy'] + 0.2 * a['obrona'] + 0.6 * ((a['matematyk'] + a['fizyka'] + a['informatyka'] + a['elektryka']) / 4), reverse=True)

for student in sortedStudents:
	print(student)
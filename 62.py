from datetime import datetime, timedelta

date = datetime.now()
print("Dzisiejsza data i czas:", date)

print("Format 1:", date.strftime("%Y/%m/%d %H:%M:%S"))
print("Format 2:", date.strftime("%y/%B/%d %I:%M:%S %p"))

koniecRoku = datetime(date.year, 12, 31)
dni_do_konca_roku = (koniecRoku - date).days
print("Ilość dni do końca roku:", dni_do_konca_roku)

dni_od_poczatku_roku = (date - datetime(date.year, 1, 1)).days
print("Ilość dni od początku roku:", dni_od_poczatku_roku)

print("Dzień tygodnia:", date.strftime("%A"))
print("Miesiąc:", date.strftime("%B"))
print("Rok:", date.year)

tydzien = date.isocalendar()[1]
print("Numer tygodnia w roku:", tydzien)

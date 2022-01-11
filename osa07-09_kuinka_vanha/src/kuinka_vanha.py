# tee ratkaisu tänne
from datetime import datetime

paiva = int(input("Päivä:"))
kk = int(input("Kuukausi:"))
vuosi = int(input("Vuosi:"))

hetki = datetime(1999,12,31)

aika = datetime(vuosi, kk, paiva)

ika = hetki - aika


if vuosi > 1999:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")
else:

    print(f"Olit {ika.days} päivää vanha, kun vuosituhat vaihtui.")


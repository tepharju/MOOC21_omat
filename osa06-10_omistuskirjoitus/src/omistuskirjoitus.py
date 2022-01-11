# tee ratkaisu tänne
nimi = input("Kenelle teos omistetaan:")

tiedosto_nimi = input("Mihin kirjoitetaan:")

with open(tiedosto_nimi, "w") as tied:
    tied.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")

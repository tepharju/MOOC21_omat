def viiva(luku, merkki):
    if merkki == "":
        print(luku*"*")
    else:
        tuloste = merkki[0]
        print(luku * tuloste)

# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "")

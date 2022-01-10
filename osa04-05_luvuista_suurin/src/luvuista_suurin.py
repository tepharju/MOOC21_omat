# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
def luvuista_suurin(eka,toka,kol):
    if eka >= toka and eka >= kol:
        return eka
    if toka >= eka and toka >= kol:
        return toka
    if kol >= eka and kol >= toka:
        return kol


if __name__ == "__main__":
    suurin = luvuista_suurin(5, 4, 8)
    print(suurin)
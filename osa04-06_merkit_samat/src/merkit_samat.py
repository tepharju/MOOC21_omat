# tee ratkaisu tänne
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti

def samat(sana,n,k):
    if n >= (len(sana)) or k >= (len(sana)):
        return False

    if sana[n] == sana[k]:
        return True
    else:
        return False

if __name__ == "__main__":
    print(samat("abc", 0, 3)) 
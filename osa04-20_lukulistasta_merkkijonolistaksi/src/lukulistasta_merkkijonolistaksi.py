# tee ratkaisu tänne

def muotoile(lista):
    uusi = []
    for alkio in lista:
        uusi.append(f"{alkio:.2f}")
    return uusi
    

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)
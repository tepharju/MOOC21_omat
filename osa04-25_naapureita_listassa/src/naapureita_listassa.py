# tee ratkaisu tänne
def pisin_naapurijono(list):
    n = 0
    naapurit = []

    for i in range(len(list)):
        if (list[-i-1] - list[-i]) == 1:
            naapurit.append(i+1)
            naapurit.append(i)

    for alkio in naapurit:
        if alkio == 0:
            naapurit.remove(alkio)    
    n = len(naapurit)


    return n



if __name__ == "__main__":
    lista = [1, 2, 3, 5, 6, 9, 10]
    #lista = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(pisin_naapurijono(lista))
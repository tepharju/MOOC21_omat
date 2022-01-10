# tee ratkaisu tänne
def kumpi_voitti(pelilauta):
    n0 = 0
    n1 = 0
    n2 = 0

    for i in range(len(pelilauta)):
        for k in range(len(pelilauta[i])):
            if pelilauta[i][k] == 1:
                n1 = n1 + 1
            if pelilauta[i][k] == 2:
                n2 = n2 + 1
            else:
                n0 = n0 + 1
    if n1 > n2:

        return 1
    if n2 > n1:
        return 2
    else:
        return 0





if __name__ == "__main__":
    lauta = [[1,1,1],[0,0,1],[2,2,2]]
    print(kumpi_voitti(lauta))
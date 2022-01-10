# tee ratkaisu tänne
def transponoi(matriisi: list):

    [*zip(*matriisi)]
    
    #return matriisi

if __name__ == "__main__":
    luvut = [[1,2,3],[1,2,3],[1,2,3]]
    print(luvut)
    transponoi(luvut)
    print(luvut)
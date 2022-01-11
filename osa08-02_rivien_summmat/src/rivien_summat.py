# tee ratkaisu tänne
def rivien_summat(matriisi:list):

    #print(len(matriisi))
    #print(sum(matriisi[0]))
    #for i in range(len(matriisi[0])):

    for i in range(0,(len(matriisi))):
        matriisi[i].append(sum(matriisi[i]))   






if __name__ == "__main__":
    matriisi = [[1, 2], [3, 4]]
    rivien_summat(matriisi)
    print(matriisi)  

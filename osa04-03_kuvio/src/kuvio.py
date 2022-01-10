
def viiva(n,merkki,k,merkki2):
    for i in range(1,n+1):
        print(i*merkki)
    
    for j in range(k):
        print(n*merkki2)

def kuvio(koko1, merkki1, koko2, merkki2):
    viiva(koko1, merkki1, koko2, merkki2)



if __name__ == "__main__":
    kuvio(5, "x", 3, "*")

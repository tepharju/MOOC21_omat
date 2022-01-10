# tee ratkaisu tänne
def kertoma(k:int):
    ker = 1
    for i in range (1,k+1):
        ker = ker * i
    return ker

def kertomat(n:int):
    if n == 1:
        d = {1:1}
        return d
    if n == 2:
        d = {1:1, 2:2}
        return d
    else:
        d = {}
        toka = 1

        for i in range(1,n+1):
            
            d[i] =  kertoma(i)
        return d


if __name__ == "__main__":
    d = kertomat(4)
    print(d)
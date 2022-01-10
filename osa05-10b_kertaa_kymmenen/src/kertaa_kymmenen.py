# tee ratkaisu tänne
def kertaa_kymmenen(eka: int, vika: int):

    d = {}

    #{x: x**2 for x in (2, 4, 6)}

    for i in range(eka,vika+1):
        toka = int(i*10)
        d[i] =  toka

    return d


if __name__ == "__main__":
    d = kertaa_kymmenen(3, 6)
    print(d)
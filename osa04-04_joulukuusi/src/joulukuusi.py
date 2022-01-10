def joulukuusi(n):
    pisin = n*"*"
    for i in range (1,n,2):
        print((-1)*(n-i)*" "+(i*"*")+((-1)*(n-i)*" ")) 
    jalka = ((n//2)*" " + "*" + (n//2)*" ")
    print(pisin)
    print(jalka)

if __name__ == "__main__":
    joulukuusi(5)
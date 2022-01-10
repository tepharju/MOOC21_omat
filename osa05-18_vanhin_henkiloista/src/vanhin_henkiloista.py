# tee ratkaisu tänne
def vanhin(henkilot:list):

    #vanhin = 2021

    x = min(henkilot, key=lambda student: student[1])
    return(x[0])
    #for i in range(len(henkilot)):
    #    if henkilot[i][i] < vanhin:
    #        vanhin = henkilot[i][i]
    #return vanhin


if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    hlista = [h1, h2, h3, h4]

    print(vanhin(hlista))
    #print(min(hlista[0]))

#L = [('Sam', 35),
#    ('Tom', 25),
#    ('Bob', 30)]


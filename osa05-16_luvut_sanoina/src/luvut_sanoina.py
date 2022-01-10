# tee ratkaisu tänne
def lukukirja():

    #ykkoset = {"1":"yksi","2":"kaksi","3":"kolme","4":"neljä","5":"viisi","6":"kuusi", "7":"seitsemän","8":"kahdeksan","9":"yhdeksän", "10":"kymmenen"}
    ykkoset = ["yksi", "kaksi", "kolme","neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen"]
    
    s = {0:"nolla"}
    i = 1

    for sana in ykkoset:
        s[i] = sana
        i = i + 1

    for sana in ykkoset:
        s[i] = sana + "toista"
        i = i +1

    s[20] = "kaksikymmentä"

    for sana in ykkoset:
        s[i] = "kaksikymmentä" + sana 
        i = i +1

    s[30] = "kolmekymmentä"

    for sana in ykkoset:
        s[i] = "kolmekymmentä" + sana 
        i = i +1

    s[40] = "neljäkymmentä"

    for sana in ykkoset:
        s[i] = "neljäkymmentä" + sana 
        i = i +1

    s[50] = "viisikymmentä"

    for sana in ykkoset:
        s[i] = "viisikymmentä" + sana 
        i = i +1

    s[60] = "kuusikymmentä"

    for sana in ykkoset:
        s[i] = "kuusikymmentä" + sana 
        i = i +1

    s[70] = "seitsemänkymmentä"

    for sana in ykkoset:
        s[i] = "seitsemänkymmentä" + sana 
        i = i +1

    s[80] = "kahdeksankymmentä"

    for sana in ykkoset:
        s[i] = "kahdeksankymmentä" + sana 
        i = i +1

    s[90] = "yhdeksänkymmentä"

    for sana in ykkoset:
        s[i] = "yhdeksänkymmentä" + sana 
        i = i +1

    del s[100]
    return s

#for k in range(11,21):
    #s[k] = ykkoset[j] + "toista"
    #j = j +1  
if __name__ == "__main__":
    ykkoset = ["yksi", "kaksi", "kolme","neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen"]



    

    

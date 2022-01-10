# tee ratkaisu tänne


def kaanna(sanakirja: dict):

    
    
    for key, value in sanakirja.items():
        if not value in result_dict.keys():
            result_dict[value] = []
        result_dict[value].append(key)
    
    result_dict = sanakirja 
    #return result_dict, print(result_dict)

    #uusi ={}

    #for key, value in sanakirja.items():
    #    uusi[value] = key
    
    #sanakirja = uusi

    #return uusi
    #uusi = {v: k for k,v in sanakirja.items()}
    #print(uusi)

    #uusi = sanakirja
    #print(sa)

    #return sa

if __name__ == "__main__":
    #s = {1: "eka", 2: "toka", 3: "kolmas", 4: "neljas"}
    #kaanna(s)
    #s = {v: k for k,v in s.items()}
    #print(s)
    result_dict = {}
    k = {1: 10, 2: 20, 3: 30}

    kaanna(k)
    print(k)
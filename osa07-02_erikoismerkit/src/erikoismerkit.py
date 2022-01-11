# tee ratkaisu tänne
#import string
import string

def jaa_merkkeihin(merkkijono:str):

    kirjaimet = ""
    asciit = str(string.ascii_letters)

    merkit = ""
    punc = str(string.punctuation)

    muut = ""
    tyhjat = str(string.whitespace)



    for merkki in merkkijono:
        if merkki in asciit:
            kirjaimet += merkki
        if merkki in punc:
            merkit += merkki
        if merkki in tyhjat:
            merkki +=muut
        if merkki not in asciit:
            merkki += muut
    
    print(kirjaimet)
    print(merkit)
    print(muut)

    
    
    #print string.letters(merkkijono)
    #print(kirjaimet)


if __name__ == "__main__":
    jaa_merkkeihin("TämäonTesti!!%&%&äää")
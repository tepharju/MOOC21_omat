# tee ratkaisu tänne
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
# if __name__ == "__main__":
# sisälle!
def kaanna(sana :str):
    return sana[::-1]

def palindromi(sana1):
    if sana1 != kaanna(sana1):
        return False

        #print("ei ollut palindromi")
    else:
        return True
        #print(f"{sana1} on palindromi!")

while True:
    s = input("Anna sana:")

    if palindromi(s):
        print(f"{s} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
        


        
    

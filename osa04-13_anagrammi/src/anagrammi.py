# Tee ratkaisu tänne
def anagrammi(eka, toka):
    #lista1 = list(eka)
    #lista2 = list(toka)
    
    if sorted(eka) == sorted(toka):
        return True
    else:
        return False
    
    if __name__ == "__main__":
        print(anagrammi("talo", "olat"))

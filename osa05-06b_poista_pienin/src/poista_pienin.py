# tee ratkaisu tänne
def poista_pienin(luvut: list):
    luvut.remove(min(luvut))





if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    print(luvut)
    poista_pienin(luvut)
    print(luvut)
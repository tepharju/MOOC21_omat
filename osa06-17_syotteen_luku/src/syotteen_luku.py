# tee ratkaisu tänne
def lue(sana: str, ala:int,yla:int):
    
    while True:
        
        try:
            luku = int(input(sana))
            if luku < yla and luku > ala:
                return luku
                #print(f"syötit luvun:{luku}")
                break
            else:
                print(f"Syötteen on oltava kokonaisluku väliltä {ala}...{yla}")
        
        except ValueError:
            print(f"Syötteen on oltava kokonaisluku väliltä {ala}...{yla}")


if __name__ == "__main__":
    luku = lue("Anna luku: ", 5, 10)
    print("syötit luvun:", luku)
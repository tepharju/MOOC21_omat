# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    
    for i in "aeiouyäöå":
        mjono = mjono.replace(i,"")

    return mjono




if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))
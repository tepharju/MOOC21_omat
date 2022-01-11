# tee ratkaisu tänne
from math import *

def hypotenuusa(kateetti1: float, kateetti2: float):

    return (sqrt(kateetti1 ** 2 +kateetti2**2))

if __name__ == "__main__":
    print(hypotenuusa(3,4)) # 5.0
    print(hypotenuusa(5,12)) # 13.0 
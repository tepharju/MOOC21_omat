# tee ratkaisu tänne
# tee ratkaisu tänne
def sarake_oikein(sudoku: list, sarake_nro: int):
  luvut = []
  sarake = []

  for i in range(len(sudoku)):
    sarake.append(sudoku[i][sarake_nro])
  i = 0

  while i <= 9:
    for luku in sarake:
      if sarake > 0 and luku in luvut:
        return False
      luvut.append(luku)
      i += 1




if __name__ == "__main__":
  sudoku = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sarake_oikein(sudoku, 0))
print(sarake_oikein(sudoku, 1))
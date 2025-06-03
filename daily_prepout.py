import random
import csv
from generator import get_2_judges 

def get_two_debaters():
    debaters = []
    with open("prepsheet.csv", "r") as prepsheet:
        csvreader = csv.reader(prepsheet)
        csvreader.__next__()

        for row in csvreader:
            debaters.append(row[3])
    random.shuffle(debaters)
    return debaters[:2]

def print_presets():
   d1, d2 = get_two_debaters()
   j1, j2 = get_2_judges()
   sides = ["AFF", "NEG"]
   random.shuffle(sides)
   s1, s2 = sides
   print(f"{d1}, {j1}, {s1}")
   print(f"{d2}, {j2}, {s2}") 

if __name__ == "__main__":
    for i in range(3):
        print_presets()
        print()
import random
import csv


def get_2_debaters():
    debaters = []
    with open("entries.csv", "r") as entries:
        csvreader = csv.reader(entries)
        csvreader.__next__()

        for row in csvreader:
            debaters.append(row[2])
    random.shuffle(debaters)
    return debaters[:2]

def get_2_judges():
    judgespool = []
    with open("judges.csv", "r") as judges:
        csvreader = csv.reader(judges)
        csvreader.__next__()

        for row in csvreader:
            judgename = row[1] + " " + row[2]
            judgespool.append(judgename)

    random.shuffle(judgespool)
    return judgespool[:2]

if __name__ == "__main__":
    d1, d2 = get_2_debaters()
    j1, j2 = get_2_judges()
    sides = ["AFF", "NEG"]
    random.shuffle(sides)
    s1, s2 = sides
    print(f"{d1} {j1} {s1}")
    print(f"{d2} {j2} {s2}")
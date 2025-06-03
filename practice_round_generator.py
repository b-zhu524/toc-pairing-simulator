import random
import csv

def get_pairing(d1, d2, elim, randomize):
    debaters = [d1, d2]
    judges = []
    if randomize:
        random.shuffle(debaters)
    if elim:
        judges = get_judges()[:3]
    else:
        judges = get_judges()[0]
    
    return f"AFF {d1} vs NEG {d2} | Judges: {judges}"



def get_judges():
    judgespool = []
    with open("judges.csv", "r") as judges:
        csvreader = csv.reader(judges)
        csvreader.__next__()

        for row in csvreader:
            judgename = row[1] + " " + row[2]
            judgespool.append(judgename)

    random.shuffle(judgespool)
    return judgespool


if __name__ == "__main__":
    d1 = input("First debater: ")
    d2 = input("Second debater: ")
    elim = input("Elimination round? (y/n): ").lower() == 'y'
    randomize = input("Randomize debaters? (y/n): ").lower() == 'y'
    pairing = get_pairing(d1, d2, elim, randomize)
    print(pairing)
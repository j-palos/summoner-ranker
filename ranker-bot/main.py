# /usr/bin/env python
from RiotAPI import RiotAPI
import RiotConsts as Consts
from Player import Player
import operator
def main():


    lines = [line.strip() for line in open('players.txt', encoding='utf-16')]
        # for line in f:
        #     print(line)
    ppl = {}
    for name in lines:
        ppl[name] = Player(name)
    place = 1
    with open('sorted-players.txt', encoding='utf-16', mode='w') as f:
        sortedppl = sorted(ppl.values(), key=operator.attrgetter('rank'), reverse=True)
        for x in sortedppl:
            f.write(str(place) + ". ")
            f.write((str(x) + "\n"))
            place += 1
            if place == 11:
                f.write("--------------------------------------------------------\n")


if __name__ == "__main__":
    main()

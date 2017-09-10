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
        # print(name)
        ppl[name] = Player(name)
        # print(ppl['name'])
    # for player in ppl:
    #     print(ppl[player])
    # for player in (sorted(ppl.values(), key=operator.attrgetter('rank'))):
    #     print(player)

    with open('sorted-players.txt', encoding='utf-16', mode='w') as f:
        sortedppl = sorted(ppl.values(), key=operator.attrgetter('rank'), reverse=True)
        for x in sortedppl:
            f.write((str(x) + "\n"))

if __name__ == "__main__":
    main()

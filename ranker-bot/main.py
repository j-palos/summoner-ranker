from RiotAPI import RiotAPI
import RiotConsts as Consts

def main():
    api = RiotAPI(Consts.TEMPKEY['key'])
    r = api.get_summoner_by_name('elo daddy')
    print(r)

if __name__ == "__main__":
    main()

import RiotConsts as Consts
from RiotAPI import RiotAPI

class Player(object):

    def __init__(self, name):
        self.name = name
        apiSumm = RiotAPI(Consts.TEMPKEY['key'])
        summID = apiSumm.get_summoner_by_name(name)['id']
        # print("summoner id is " + str(summID))
        apiRank =  RiotAPI(Consts.TEMPKEY['key'])
        ranking = apiRank.get_summoner_rank(summID)
        # self.tier = soloTier
        # self.div = soloDiv
        # self.lp = soloLP
        for thing in ranking:
            if( thing['queueType'] == 'RANKED_SOLO_5x5'):
                self.soloTier = thing['tier']
                self.soloDiv = thing['rank']
                self.soloLP = thing['leaguePoints']
        self.rank = 0
        if( self.soloTier == "BRONZE"):
            self.rank += 1000
        elif( self.soloTier == "SILVER"):
            self.rank += 2000
        elif( self.soloTier == "GOLD"):
            self.rank += 3000
        elif( self.soloTier == "PLATINUM"):
            self.rank += 4000
        elif( self.soloTier == "DIAMOND"):
            self.rank += 5000
        elif( self.soloTier == "MASTER"):
            self.rank += 6000
        elif( self.soloTier == "CHALLENGER"):
            self.rank += 7000
        if( self.soloDiv == "V"):
            self.rank += 100
        elif(self.soloDiv == "IV"):
            self.rank += 200
        elif(self.soloDiv == "III"):
            self.rank += 300
        elif(self.soloDiv == "II"):
            self.rank += 400
        elif(self.soloDiv == "I"):
            self.rank += 500
        self.rank += self.soloLP


    # def assignRank(self):
    #     self.rank = 0
    #     if( self.soloTier == "BRONZE"):
    #         self.rank += 1000
    #     elif( self.soloTier == "SILVER"):
    #         self.rank += 2000
    #     elif( self.soloTier == "GOLD"):
    #         self.rank += 3000
    #     elif( self.soloTier == "PLATINUM"):
    #         self.rank += 4000
    #     elif( self.soloTier == "DIAMOND"):
    #         self.rank += 5000
    #     elif( self.soloTier == "MASTER"):
    #         self.rank += 6000
    #     elif( self.soloTier == "CHALLENGER"):
    #         self.rank += 7000
    #     if( self.soloDiv == "V"):
    #         self.rank += 100
    #     elif(self.soloDiv == "IV"):
    #         self.rank += 200
    #     elif(self.soloDiv == "III"):
    #         self.rank += 300
    #     elif(self.soloDiv == "II"):
    #         self.rank += 400
    #     elif(self.soloDiv == "I"):
    #         self.rank += 500
    #     self.rank += self.soloLP
    #     return self.rank

    def __str__(self):
        return self.name + " is " + str(self.soloTier) + " " + str(self.soloDiv) + " " + str(self.soloLP)

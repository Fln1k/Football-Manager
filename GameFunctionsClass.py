from PlayerClass import Player
from TeamClass import Team
from LeagueClass import League
from MatchClass import Game
from PlayerClass import PoolPlayers


def LoadPlayers(Players):
    counter=0
    file = open('PlayersDatabase.dat','r')
    cont = file.readlines()
    try:
        while 1:
            cont1 = cont[counter].split()
            Players.append(Player(cont1))
            counter+=1
    except:
        Players.pop()
        Pool = PoolPlayers(Players)
        return Pool

        
def LoadTeams(Teams):
    Players=[]
    Pool = LoadPlayers(Players)
    counter=0
    reservcounter=0
    superreservcounter=0
    megareservcounter=0
    TeamPlayers = []
    TeamsPlayers =[]
    TeamName=''
    Chelsea = Team('Chelsea','Blue',70000000,'Mouricio','Sari',433,Pool.Request('Chelsea'))
    Arsenal = Team('Arsenal','Red',50000000,'Emry','Unai',442,Pool.Request('Arsenal'))
    Chelsea.FillStartSquad()
    Arsenal.FillStartSquad()
    for Player in Chelsea.StartPlayers:
        print('{} {} {}'.format(Player.Surname, Player.Position, Player.Club))
    print('-------------')

def LoadLeagues(Leagues):
    Teams=[]
    LoadTeams(Teams)
    EPL = League('EPL',Teams)
    Leagues.append(EPL)


Leagues=[]
LoadLeagues(Leagues)

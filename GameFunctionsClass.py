from PlayerClass import Player
from TeamClass import Team
from LeagueClass import League
from MatchClass import Game
from PlayerClass import PoolPlayers
from CoachClass import Coach

def PointsKey(Team):
    return Team.Points

def LoadPlayers(Players):
    counter = 0
    file = open('PlayersDatabase.dat', 'r')
    cont = file.readlines()
    try:
        while 1:
            cont1 = cont[counter].split()
            Players.append(Player(cont1))
            counter += 1
    except:
        Players.pop()
        Pool = PoolPlayers(Players)
        return Pool


def LoadTeams(Teams):
    Players = []
    Pool = LoadPlayers(Players)
    counter = 0
    reservcounter = 0
    superreservcounter = 0
    megareservcounter = 0
    TeamPlayers = []
    TeamsPlayers = []
    TeamName = ''
    Teams.append(Team('Chelsea','CHE',[0,0,1,1], 70000000,Coach('Mauricio','Sari',52,'Italian','Chelsea'), 433, Pool.Request('Chelsea')))
    Teams.append(Team('Arsenal','ARS',[1,0,0,1], 50000000,Coach('Unai','Emery',40,'Spanish','Arsenal'), 442, Pool.Request('Arsenal')))


def LoadLeagues(Leagues):
    Teams = []
    LoadTeams(Teams)
    EPL = League('EPL', Teams)
    Leagues.append(EPL)

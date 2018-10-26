from PlayerClass import Player
from TeamClass import Team
from LeagueClass import League
from MatchClass import Game
from PlayerClass import PoolPlayers
from CoachClass import Coach
from CoachClass import CoachPool
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from random import randint as rand
from kivy.clock import Clock
from MatchClass import MatchTeam


class AllFunctions:
    _PlayersPool=0
    _ManagersPool=0
    _Leagues=[]
    _timer=0
    
    def __init__(self):
        self.PlayersPool=self.LoadPlayers()
        self.ManagersPool=self.LoadManagers()
        self.Leagues=self.LoadLeagues()

        
    def PointsKey(self,Team):
        return Team.Points


    def findminratingplayer(self,amount):
        min = 101
        minindex = 0
        for counter in amount:
            if min > counter.Rating:
                min = counter.Rating
                minindex = counter
        return amount.index(minindex)


    def findmaxratingplayer(self,amount):
        max = 0
        maxindex = 0
        for counter in amount:
            if max < counter.Rating:
                max = counter.Rating
                maxindex = counter
        return amount.index(maxindex)


    def LoadPlayers(self):
        Players=[]
        counter = 0
        file = open('PlayersDatabase.dat', 'r')
        cont = file.readlines()
        try:
            while 1:
                cont1 = cont[counter].split()
                Players.append(Player(cont1))
                counter += 1
        except:
            Pool = PoolPlayers(Players)
            return Pool


    def LoadManagers(self):
        Managers=[]
        counter = 0
        file = open('ManagersDatabase.dat', 'r')
        cont = file.readlines()
        try:
            while 1:
                cont1 = cont[counter].split()
                Managers.append(Coach(cont1))
                counter += 1
        except:
            Pool = CoachPool(Managers)
            return Pool


    def LoadTeams(self):
         Teams = []
         Teams.append(Team('Chelsea','CHE',[0,0,1,1],70000000,self.ManagersPool.RequestCoach('Chelsea'), self.PlayersPool.Request('Chelsea')))
         Teams.append(Team('Arsenal','ARS',[1,0,0,1], 50000000,self.ManagersPool.RequestCoach('Arsenal'), self.PlayersPool.Request('Arsenal')))
         return Teams

        
    def LoadLeagues(self):
        Leagues=[]
        Teams=self.LoadTeams()
        EPL = League('EPL', Teams)
        Leagues.append(EPL)
        return Leagues


    def MatchSimulation(self):
        MatchTeam1=MatchTeam(self.Leagues[0].Teams[0])
        MatchTeam2=MatchTeam(self.Leagues[0].Teams[1])
        activeteam = MatchTeam1
        notactiveteam = MatchTeam2
        additionaltime = 90
        attackpointer = 0
        if activeteam.Goals < notactiveteam.Goals and rand(0,200) < 100 and activeteam.Team.Tactic != activeteam.Team.Tactic1 and timer > 100:
            if activeteam.Substitution > 0:
                if int(int(activeteam.Team.Tactic / 10) % 10) == 4 and int(int(activeteam.Team.Tactic1 / 10) % 10) == 3:
                    Middefenders = []
                    for counter in activeteam.Team.StartPlayers:
                        if counter.Position == 'MD':
                            Middefenders.append(counter)
                    Strikers = []
                    for counter in activeteam.Team.ReservePlayers:
                        if counter.Position == 'ST':
                            Strikers.append(counter)
                    f = int(int(activeteam.Team.Tactic / 10) % 10) + self.findminratingplayer(Middefenders)
                    while f < int(int(int(activeteam.Team.Tactic / 10) / 10) % 10) + int(int(activeteam.Team.Tactic / 10) % 10):
                        activeteam.Team.StartPlayers[f], activeteam.Team.StartPlayers[f + 1] = activeteam.Team.StartPlayers[f + 1], activeteam.Team.StartPlayers[f]
                        f += 1
                        activeteam.Team.StartPlayers[8] = activeteam.Team.ReservePlayers[6 - self.findmaxratingplayer(Strikers)]
            activeteam.Team.Tactic = activeteam.Team.Tactic1
        time = int(self.timer / 2)
        activeteam.addProssession()
        if time == 45 or time == 90:
            additionaltime = rand(0, 5)
        chance = rand(0, 100)
        if chance <= 20:
            player = rand(1, 10)
            activeplayer = notactiveteam.Team.StartPlayers[player]
            while activeplayer.RedCard == 1:
                player = rand(1, 10)
                activeplayer = notactiveteam.Team.StartPlayers[player]
            if rand(0, 150) == 75:
                notactiveteam.addRed(player)
            elif rand(0, 100) <= 10:
                notactiveteam.addYellow(player)
            if rand(0, 200) <= 2 and activeteam.Substitution > 0:
                activeplayer = activeteam.Team.StartPlayers[rand(1, 10)]
                for Player in activeteam.Team.ReservePlayers:
                    if Player.Position == activeplayer.Position and Player.IsSubstitution == 0:
                        Player.IsSubstitution = 1
                        Player, activeplayer = activeplayer, Player
                        activeteam.Substitution -= 1
                        break
        if ((time >= 60 and rand(0, 100) <= 5) or rand(0, 200 <= 4)) and activeteam.Substitution > 0:
            activeplayer = activeteam.Team.StartPlayers[rand(1, 10)]
            for Player in activeteam.Team.ReservePlayers:
                if Player.Position == activeplayer.Position:
                    Player.IsSubstitution = 1
                    Player, activeplayer = activeplayer, Player
                    activeteam.Substitution -= 1
                    break
        if attackpointer < 4:
            chance = rand(0, 100)
            activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
            while activeplayer.RedCard == 1:
                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
            if chance < activeplayer.Rating:
                attackpointer += 1
                activeteam.addSecsessfulPass()
            else:
                attackpointer = 0
                activeteam.addPass()
                activeteam, notactiveteam = notactiveteam, activeteam
        else:
            chance = rand(0, 100)
            if chance <= 50:
                chance = rand(0, 100)
                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                while activeplayer.RedCard == 1:
                    activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                if chance < activeplayer.Rating:
                    attackpointer += 1
                    activeteam.addSecsessfulPass()
                else:
                    attackpointer = 0
                    activeteam.addPass()
                    activeteam, notactiveteam = notactiveteam, activeteam
            else:
                chance = rand(0, 100)
                if chance < 30:
                    activeplayer = activeteam.Team.StartPlayers[
                        rand(activeteam.Team.Defenders, 10 - activeteam.Team.Strikers)]
                    while activeplayer.RedCard == 1:
                        activeplayer = activeteam.Team.StartPlayers[
                            rand(activeteam.Team.Defenders, 10 - activeteam.Team.Strikers)]
                else:
                    activeplayer = activeteam.Team.StartPlayers[rand(10 - activeteam.Team.Strikers, 10)]
                    while activeplayer.RedCard == 1:
                        activeplayer = activeteam.Team.StartPlayers[
                            rand(activeteam.Team.Defenders, 10 - activeteam.Team.Strikers)]
                chance = rand(0, 100)
                if chance <= activeplayer.Rating / 2:
                    activeteam.addShoot()
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
                elif rand(0, activeplayer.Shoot) > notactiveteam.Team.StartPlayers[0].Rating / 2:
                    activeteam.addGoal()
                    activeteam.Team.GoalsScore += 1
                    notactiveteam.Team.GoalsLose += 1
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
                else:
                    activeteam.addSecsessfilShoot()
                    notactiveteam.addSave()
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
        self.timer += 1
        if time == additionaltime + 45 or time == additionaltime + 90:
            self.timer -= additionaltime * 2
            additionaltime = 90
            if time == 45:
                pass
            self.timer += 1
        if self.timer == 180:
            activeteam.Prossession = int(activeteam.Prossession / (activeteam.Prossession + notactiveteam.Prossession) * 100)
            notactiveteam.Prossession = 100 - activeteam.Prossession
            activeteam.AllPass *= 2
            activeteam.SecsessfulPass *= 2
            notactiveteam.AllPass *= 2
            notactiveteam.SecsessfulPass *= 2
            if activeteam.Goals > notactiveteam.Goals:
                activeteam.Team.Points += 3
                activeteam.Team.WinGames += 1
                notactiveteam.Team.LoseGames += 1
            elif notactiveteam.Goals > activeteam.Goals:
                notactiveteam.Team.Points += 3
                activeteam.Team.LoseGames += 1
                notactiveteam.Team.WinGames += 1
            else:
                activeteam.Team.Points += 1
                activeteam.Team.DrawGames += 1
                notactiveteam.Team.DrawGames += 1
                notactiveteam.Team.Points += 1
            activeteam.Team.Games += 1
            notactiveteam.Team.Games += 1
    FootballManager=AllFunctions
    FootballManager.start_timer(FootballManager)

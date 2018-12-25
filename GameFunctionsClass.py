from classmodels import Player
from classmodels import Team
from classmodels import League
from classmodels import Coach
from classmodels import DataPool
from classmodels import PoolPlayers
from classmodels import CoachPool
from random import randint as rand
from MatchClass import MatchTeam
import sqlite3


class AllFunctions:
    PlayersPool = 0
    ManagersPool = 0
    Leagues = 0
    timer = 0
    Teams = [0, 0]
    UpdateArgs = 0
    counter = 0
    activeteam = 0
    notactiveteam = 0
    MatchTeam1 = 0
    MatchTeam2 = 0
    additionaltime = 90
    attackpointer = 0

    def __init__(self, UpdateArgs):
        self.UpdateArgs = UpdateArgs
        self.PlayersPool = self.load_players()
        self.ManagersPool = self.load_managers()
        self.Leagues = self.load_leagues()

    def load_team(self, team1, team2, updateargs):
        self.Teams[0], self.Teams[1] = team1, team2
        self.UpdateArgs = updateargs

    def update(self, arg1, arg2, arg3, arg4, arg5, arg6, arg7):
        self.UpdateArgs.UpdateArgs[0], self.UpdateArgs.UpdateArgs[1], self.UpdateArgs.UpdateArgs[2], self.UpdateArgs.UpdateArgs[3], self.UpdateArgs.UpdateArgs[4], self.UpdateArgs.UpdateArgs[5], self.UpdateArgs.UpdateArgs[6] = arg1, arg2, arg3, arg4, arg5, arg6, arg7

    def load_data(self):
        conn = sqlite3.connect('match.db')
        sql = """SELECT * from matches"""
        cursor = conn.cursor()
        cursor.execute(sql)
        cont = cursor.fetchall()
        line = 0
        database = []
        try:
            while 1:
                row = 0
                matchday = []
                counter = 0
                matchday.append(cont[line][row].split(' '))
                matchday.append(cont[line][1])
                while counter<cont[line][1]:
                    matchday.append(cont[line][counter+2])
                    counter += 1
                database.append(matchday)
                line += 1
        except:
           return database

    def PointsKey(self, team):
        return team.Points

    def find_min_rating_player(self, amount):
        min = 101
        minindex = 0
        for counter in amount:
            if min > counter.Rating:
                min = counter.Rating
                minindex = counter
        return amount.index(minindex)

    def find_max_rating_player(self,amount):
        max = 0
        maxindex = 0
        for counter in amount:
            if max < counter.Rating:
                max = counter.Rating
                maxindex = counter
        return amount.index(maxindex)

    def load_players(self):
        Players = []
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

    def load_managers(self):
        Managers = []
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

    def load_teams(self):
        Teams = []
        Teams.append(Team('Chelsea', 'CHE', [0, 0, 1, 1], 70000000, self.ManagersPool.RequestCoach('Chelsea'), self.PlayersPool.Request('Chelsea')))
        Teams.append(Team('Arsenal', 'ARS', [1, 0, 0, 1], 50000000, self.ManagersPool.RequestCoach('Arsenal'), self.PlayersPool.Request('Arsenal')))
        Teams.append(Team('Liverpool', 'LIV',[1, 0, 0, 1], 70000000,self.ManagersPool.RequestCoach('Liverpool'),self.PlayersPool.Request('Liverpool')))
        Teams.append(Team('Manchester City', 'MCI', [135, 206, 250, 1], 100000000, self.ManagersPool.RequestCoach('Manchester_City'),self.PlayersPool.Request('Manchester_City')))
        return Teams

    def load_leagues(self):
        """
        loads data from league
        :return: league
        """
        leagues = []
        teams = self.load_teams()
        leagues.append(League('EPL', teams))
        return leagues

    def match_simulation(self, dt):
        if self.UpdateArgs.UpdateArgs[7]==0:
            self. MatchTeam1 = MatchTeam(self.Teams[0])
            self.MatchTeam2 = MatchTeam(self.Teams[1])
            self.activeteam = self.MatchTeam1
            self.notactiveteam = self.MatchTeam2
            self.UpdateArgs.UpdateArgs[7] += 1
        active = ' '
        if self.activeteam.Goals < self.notactiveteam.Goals and rand(0,200) < 100 and self.activeteam.Team.Tactic != self.activeteam.Team.Tactic1 and self.timer > 100:
            if self.activeteam.Substitution > 0:
                if int(int(self.activeteam.Team.Tactic / 10) % 10) == 4 and int(int(self.activeteam.Team.Tactic1 / 10) % 10) == 3:
                    Middefenders = []
                    for counter in self.activeteam.Team.StartPlayers:
                        if counter.Position == 'MD':
                            Middefenders.append(counter)
                    Strikers = []
                    for counter in self.activeteam.Team.ReservePlayers:
                        if counter.Position == 'ST':
                            Strikers.append(counter)
                    f = int(int(self.activeteam.Team.Tactic / 10) % 10) + self.find_min_rating_player(Middefenders)
                    while f < int(int(int(self.activeteam.Team.Tactic / 10) / 10) % 10) + int(int(self.activeteam.Team.Tactic / 10) % 10):
                        self.activeteam.Team.StartPlayers[f], self.activeteam.Team.StartPlayers[f + 1] = \
                            self.activeteam.Team.StartPlayers[f + 1], self.activeteam.Team.StartPlayers[f]
                        f += 1
                        self.activeteam.Team.StartPlayers[8] = self.activeteam.Team.ReservePlayers[
                            6 - self.find_max_rating_player(Strikers)]
                        self.activeteam.Team.Tactic = self.activeteam.Team.Tactic1
        self.time = int(self.timer / 2)
        self.activeteam.add_prossession()
        if self.time == 45 or self.time == 90:
            self.additionaltime = rand(0, 5)
        chance = rand(0, 100)
        if chance <= 20:
            player = rand(1, 10)
            activeplayer = self.notactiveteam.Team.StartPlayers[player]
            while activeplayer.RedCard == 1:
                player = rand(1, 10)
                activeplayer = self.notactiveteam.Team.StartPlayers[player]
            if rand(0, 150) == 75:
                self.notactiveteam.add_red(player)
            elif rand(0, 100) <= 10:
                self.notactiveteam.add_yellow(player)
            if rand(0, 200) <= 2:
                activeplayer = self.activeteam.Team.StartPlayers[rand(1, 10)]
                for Player in self.activeteam.Team.ReservePlayers:
                    if Player.Position == activeplayer.Position and Player.IsSubstitution == 0:
                        Player.IsSubstitution = 1
                        Player, activeplayer = activeplayer, Player
                        self.activeteam.Substitution -= 1
                        break
        if ((self.time >= 60 and rand(0, 100) <= 5) or rand(0, 200 <= 4)) and self.activeteam.Substitution == 0:
            activeplayer = self.activeteam.Team.StartPlayers[rand(1, 10)]
            for Player in self.activeteam.Team.ReservePlayers:
                if Player.Position == activeplayer.Position:
                    Player.IsSubstitution = 1
                    Player, activeplayer = activeplayer, Player
                    self.activeteam.Substitution -= 1
                    break
        if self.attackpointer < 4:
            chance = rand(0, 100)
            activeplayer = self.activeteam.Team.StartPlayers[rand(self.activeteam.Team.Defenders, 10)]
            while activeplayer.RedCard == 1:
                activeplayer = self.activeteam.Team.StartPlayers[rand(self.activeteam.Team.Defenders, 10)]
            if chance < activeplayer.Rating:
                active = "Secsessful pass by:"
                self.attackpointer += 1
                self.activeteam.add_secsessful_pass()
            else:
                self.attackpointer = 0
                active = "Loosing ball by: "
                self.activeteam.add_pass()
                self.activeteam, self.notactiveteam = self.notactiveteam, self.activeteam

        else:
            chance = rand(0, 100)
            if chance <= 50:
                chance = rand(0, 100)
                activeplayer = self.activeteam.Team.StartPlayers[rand(self.activeteam.Team.Defenders, 10)]
                while activeplayer.RedCard == 1:
                    activeplayer = self.activeteam.Team.StartPlayers[rand(self.activeteam.Team.Defenders, 10)]
                if chance < activeplayer.Rating:
                    active = 'Secsessful pass by:'
                    self.attackpointer += 1
                    self.activeteam.add_secsessful_pass()
                else:
                    self.attackpointer = 0
                    self.activeteam.add_pass()
                    self.activeteam, self.notactiveteam = self.notactiveteam, self.activeteam
            else:
                chance = rand(0, 100)
                if chance < 30:
                    activeplayer = self.activeteam.Team.StartPlayers[
                        rand(self.activeteam.Team.Defenders, 10 - self.activeteam.Team.Strikers)]
                    while activeplayer.RedCard == 1:
                        activeplayer = self.activeteam.Team.StartPlayers[
                            rand(self.activeteam.Team.Defenders, 10 - self.activeteam.Team.Strikers)]
                else:
                    activeplayer = self.activeteam.Team.StartPlayers[rand(10 - self.activeteam.Team.Strikers, 10)]
                    while activeplayer.RedCard == 1:
                        activeplayer = self.activeteam.Team.StartPlayers[
                            rand(self.activeteam.Team.Defenders, 10 - self.activeteam.Team.Strikers)]
                chance = rand(0, 100)
                if chance <= activeplayer.Rating / 2:
                    self.activeteam.add_shoot()
                    active = 'Missing Shoot by:'
                    self.activeteam, self.notactiveteam = self.notactiveteam, self.activeteam
                    self.attackpointer = 0
                elif rand(0, activeplayer.Shoot) > self.notactiveteam.Team.StartPlayers[0].Rating / 2:
                    self.activeteam.add_goal()
                    active = 'Gol by:'
                    self.activeteam, self.notactiveteam = self.notactiveteam,self.activeteam
                    self.attackpointer = 0
                else:
                    self.activeteam.add_secsessfull_shoot()
                    self.notactiveteam.add_save()
                    active = 'Save by:'
                    self.activeteam, self.notactiveteam = self.notactiveteam, self.activeteam
                    self.attackpointer = 0
        self.timer += 1
        if self.time == self.additionaltime + 45 or self.time == self.additionaltime + 90:
            self.timer -= self.additionaltime * 2
            self.additionaltime = 90
            if self.time == 45:
                active='Half Time'
            self.timer += 1
        self.activeteam.Prossession = int(
            self.activeteam.Prossession / (self.activeteam.Prossession + self.notactiveteam.Prossession) * 100)
        self.notactiveteam.Prossession = 100 - self.activeteam.Prossession
        self.activeteam.AllPass *= 2
        self.activeteam.SecsessfulPass *= 2
        self.notactiveteam.AllPass *= 2
        self.notactiveteam.SecsessfulPass *= 2
        if self.activeteam.Goals >self.notactiveteam.Goals:
            self.activeteam.Team.Points += 3
            self.activeteam.Team.WinGames += 1
            self.notactiveteam.Team.LoseGames += 1
        elif self.notactiveteam.Goals > self.activeteam.Goals:
            self.notactiveteam.Team.Points += 3
            self.activeteam.Team.LoseGames += 1
            self.notactiveteam.Team.WinGames += 1
        else:
            self.activeteam.Team.Points += 1
            self.activeteam.Team.DrawGames += 1
            self.notactiveteam.Team.DrawGames += 1
            self.notactiveteam.Team.Points += 1
            self.activeteam.Team.Games += 1
            self.notactiveteam.Team.Games += 1
        self.update(self.activeteam, self.notactiveteam, activeplayer, active, self.MatchTeam1, self.MatchTeam2,self.timer)
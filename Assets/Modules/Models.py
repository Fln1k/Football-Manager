import sys
import pygame
from pygame.locals import *
from random import randint as rand
import sqlite3


class AllFunctions:
    PlayersPool = None
    ManagersPool = None
    Leagues = None
    counter = 0
    pass_counter = 0
    time = 0

    def __init__(self,):
        self.ManagersPool = self.load_managers()
        self.PlayersPool = self.load_players()
        self.Leagues = self.load_leagues()

    def load_data(self):
        conn = sqlite3.connect("Assets/Modules/match.db")
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
        file = open('Assets/Modules/PlayersDatabase.dat', 'r')
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
        file = open('Assets/Modules/ManagersDatabase.dat', 'r')
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
        Teams.append(Team('Chelsea', 'CHE', [0, 0, 1, 1], 70000000, self.ManagersPool.RequestCoach('Chelsea'),
                          self.PlayersPool.Request('Chelsea')))
        Teams.append(Team('Arsenal', 'ARS', [1, 0, 0, 1], 50000000, self.ManagersPool.RequestCoach('Arsenal'),
                          self.PlayersPool.Request('Arsenal')))
        Teams.append(Team('Liverpool', 'LIV',[1, 0, 0, 1], 70000000,self.ManagersPool.RequestCoach('Liverpool'),
                          self.PlayersPool.Request('Liverpool')))
        Teams.append(Team('Manchester City', 'MCI', [135, 206, 250, 1], 100000000,
                          self.ManagersPool.RequestCoach('Manchester_City'),self.PlayersPool.Request('ManchesterCity')))
        Teams.append(Team('Manchester United', 'MCU', [1, 0, 0, 1], 100000000,
                          self.ManagersPool.RequestCoach('Manchester_United'),
                          self.PlayersPool.Request('ManchesterUnited')))
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

    def match_simulation(self,team1,team2,playerteam,time,attackpointer):
        if time == 0:
            activeteam = MatchTeam(team1)
            notactiveteam = MatchTeam(team2)
        else:
            activeteam = team1
            notactiveteam = team2
        active = ' '
        if activeteam.Goals < notactiveteam.Goals and rand(0,200) < 100 and activeteam.Team.Tactic\
                != activeteam.Team.Tactic1 and time > 100 and activeteam.Team.Name != playerteam.Name:
            if activeteam.Substitution > 0:
                if int(int(activeteam.Team.Tactic / 10) % 10) == 4 and int(
                        int(activeteam.Team.Tactic1 / 10) % 10) == 3:
                    Middefenders = []
                    for counter in activeteam.Team.StartPlayers:
                        if counter.Position == 'MD':
                            Middefenders.append(counter)
                    Strikers = []
                    for counter in activeteam.Team.ReservePlayers:
                        if counter.Position == 'ST':
                            Strikers.append(counter)
                    f = int(int(activeteam.Team.Tactic / 10) % 10) + self.find_min_rating_player(Middefenders)
                    while f < int(int(int(activeteam.Team.Tactic / 10) / 10) % 10) + int(
                            int(activeteam.Team.Tactic / 10) % 10):
                        activeteam.Team.StartPlayers[f], activeteam.Team.StartPlayers[f + 1] = \
                            activeteam.Team.StartPlayers[f + 1], activeteam.Team.StartPlayers[f]
                        f += 1
                        activeteam.Team.StartPlayers[8] = activeteam.Team.ReservePlayers[
                            6 - self.find_max_rating_player(Strikers)]
                        activeteam.Team.Tactic = activeteam.Team.Tactic1
        activeteam.add_prossession()
        chance = rand(0, 100)
        if chance <= 20:
            player = rand(1, 10)
            activeplayer = notactiveteam.Team.StartPlayers[player]
            while activeplayer.RedCard == 1:
                player = rand(1, 10)
                activeplayer = notactiveteam.Team.StartPlayers[player]
            if rand(0, 150) == 75:
                notactiveteam.add_red(player)
            elif rand(0, 100) <= 10:
                notactiveteam.add_yellow(player)
            if rand(0, 200) <= 2:
                activeplayer = activeteam.Team.StartPlayers[rand(1, 10)]
                for Player in activeteam.Team.ReservePlayers:
                    if Player.Position == activeplayer.Position and Player.IsSubstitution == 0:
                        Player.IsSubstitution = 1
                        Player, activeplayer = activeplayer, Player
                        activeteam.Substitution -= 1
                        break
        elif attackpointer < 4:
            chance = rand(0, 100)
            activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
            while activeplayer.RedCard == 1:
                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
            if chance < activeplayer.Rating:
                active = "Secsessful pass by:"
                attackpointer += 1
                activeteam.add_secsessful_pass()
            else:
                attackpointer = 0
                active = "Loosing ball by: "
                activeteam.add_pass()
                activeteam, notactiveteam = notactiveteam, activeteam

        else:
            chance = rand(0, 100)
            if chance <= 50:
                chance = rand(0, 100)
                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                while activeplayer.RedCard == 1:
                    activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                if chance < activeplayer.Rating:
                    active = 'Secsessful pass by:'
                    attackpointer += 1
                    activeteam.add_secsessful_pass()
                else:
                    attackpointer = 0
                    activeteam.add_pass()
                    activeteam, notactiveteam = notactiveteam, activeteam
            else:
                chance = rand(0, 100)
                if chance < 30:
                    activeplayer = activeteam.Team.StartPlayers[
                        rand(activeteam.Team.Defenders, 10 -activeteam.Team.Strikers)]
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
                    activeteam.add_shoot()
                    active = 'Missing Shoot by:'
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
                elif rand(0, activeplayer.Shoot) > notactiveteam.Team.StartPlayers[0].Rating / 2:
                    activeteam.add_goal()
                    active = 'Gol by:'
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
                else:
                    activeteam.add_secsessful_shoot()
                    notactiveteam.add_save()
                    active = 'Save by:'
                    activeteam, notactiveteam = notactiveteam, activeteam
                    attackpointer = 0
        time += 1
        if time == 180:
            activeteam.Prossession = int(
                activeteam.Prossession / (activeteam.Prossession + notactiveteam.Prossession) * 100)
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
        return [activeteam, notactiveteam, playerteam, time,attackpointer]


def get_play_teams(data,DataPool,GameFuncs):
    str_data = [str(data[0]), str(data[1]), str(data[2])]
    if len(DataPool.get_match_day(str_data)) == 0:
        return []
    array = []
    for team in DataPool.get_match_day(str_data):
        teamname = team.split()
        testname1 = ''
        testname2 = ''
        counter = 0
        while teamname[counter] != '-':
            testname1 += teamname[counter]
            counter += 1
            if teamname[counter] != '-':
                testname1 += ' '
        counter += 1
        while counter < len(teamname):
            testname2 += teamname[counter]
            counter += 1
            if counter < len(teamname):
                testname2 += ' '
        for teams in GameFuncs.Leagues[0].Teams:
            if teams.Name == testname1:
                for teamss in GameFuncs.Leagues[0].Teams:
                    if teamss.Name == testname2:
                        array.append(teams)
                        array.append(teamss)
    return array


def skip(Data):
    Data[0] += 1
    if Data[0] == 31:
        Data[0] = 1
        Data[1] += 1
        if Data[1] == 13:
            Data[1] = 1
            Data[2] += 1
    return Data


class table:
    table = None

    def __init__(self,teams):
        self.table = teams

    def sort(self):
        self.table = sorted(self.table, key=lambda k: k.Points,reverse=True)

    def update(self,teams):
        self.table = teams

def findmin(amount):
    min = 101
    for counter in amount:
        if  min>counter:
             min=counter
    return amount.index(min)


def FillStartSquad(AllPlayers, Tactic):
    StartPlayers = []
    Tactic1 = Tactic
    Strikers = int(Tactic1 % 10)
    Tactic = int(Tactic / 10)
    Middefenders = int(Tactic % 10)
    Tactic = int(Tactic / 10)
    Defenders = int(Tactic % 10)
    GKRATING = 0
    DefendersRating = []
    while Defenders > 0:
        DefendersRating.append(0)
        Defenders -= 1
    MiddefendersRating = []
    while Middefenders > 0:
        MiddefendersRating.append(0)
        Middefenders -= 1
    StrikersRating = []
    while Strikers > 0:
        StrikersRating.append(0)
        Strikers -= 1
    Strikers = int(Tactic1 % 10)
    Tactic = int(Tactic1 / 10)
    Middefenders = int(Tactic % 10)
    Tactic = int(Tactic / 10)
    Defenders = int(Tactic % 10)
    for Player in AllPlayers:
        if Player.Position == 'GK' and Player.Rating>GKRATING:
            if len(StartPlayers) > 0:
                StartPlayers.pop(0)
            StartPlayers.append(Player)
            GKRATING = Player.Rating
        if Player.Position == 'DF' and Player.Rating > DefendersRating[findmin(DefendersRating)]:
            if len(StartPlayers) > Defenders:
                StartPlayers.pop(1+findmin(DefendersRating))
            StartPlayers.append(Player)
            DefendersRating[findmin(DefendersRating)] = Player.Rating
        elif Player.Position == 'MD' and Player.Rating > MiddefendersRating[findmin(MiddefendersRating)]:
            if len(StartPlayers) > Defenders+Middefenders:
                StartPlayers.pop(1+Defenders+findmin(MiddefendersRating))
            StartPlayers.append(Player)
            MiddefendersRating[findmin(MiddefendersRating)] = Player.Rating
        elif Player.Position == 'ST' and Player.Rating>StrikersRating[findmin(StrikersRating)]:
            if len(StartPlayers) > Defenders+Middefenders+Strikers:
                StartPlayers.pop(1+Defenders+Middefenders+findmin(StrikersRating))
            StartPlayers.append(Player)
            StrikersRating[findmin(StrikersRating)] = Player.Rating
    return StartPlayers


def FillReserve(allplayers, startplayers):
    Reserve = []
    GKRating = 0
    DFRating = [0,0]
    MDRating = [0,0,0]
    STRating = 0
    for Player in allplayers:
        Start = False
        for Player1 in startplayers:
            if Player.Surname == Player1.Surname:
                Start = True
        if Start == False:
            if Player.Position == 'GK' and (len(Reserve) == 0 or Player.Rating > GKRating):
                if len(Reserve) == 1:
                    Reserve.pop(0)
                Reserve.append(Player)
            if Player.Position == 'DF' and (len(Reserve) < 3 or Player.Rating > findmin(DFRating)):
                if len(Reserve) > 2:
                    Reserve.pop(1 + findmin(DFRating))
                Reserve.append(Player)
                DFRating[findmin(DFRating)] = Player.Rating
            if Player.Position == 'MD' and (len(Reserve) < 5 or Player.Rating > findmin(MDRating)):
                if len(Reserve) > 5:
                    Reserve.pop(3 + findmin(MDRating))
                Reserve.append(Player)
                MDRating[findmin(MDRating)] = Player.Rating
            if Player.Position == 'ST' and (len(Reserve) < 7 or Player.Rating > STRating):
                if len(Reserve) == 7:
                    Reserve.pop(6)
                Reserve.append(Player)
                STRating = Player.Rating
    return Reserve


def check_numeric(test):
    if test == "0" or test == "1" or test == "2" or test == "3" or test == "4" or test == "5" or test == "6"\
            or test == "7" or test == "8" or test == "9" or test == "0":
        return True
    return False


def display_box(screen, message,pos):
    font = pygame.font.Font(None, 50)
    rect = pygame.Rect([pos[0], pos[1], 300 , 50])
    offset = (3, 3)
    pygame.draw.rect(screen, (0, 0, 0), rect, 0)
    pygame.draw.rect(screen, (255, 255, 255), rect, 1)
    rect.left += offset[0]
    rect.top += offset[1]
    if len(message) != 0:
        screen.blit(font.render(message, 1, (255,255,255)), rect.topleft)
    pygame.display.flip()


def ask(screen,text,pos,ask):
    pygame.font.init()
    display_box(screen,text,pos)
    while True:
        pygame.time.wait(0)
        event = pygame.event.poll()
        if event.type == QUIT:
            sys.exit()
        if event.type != KEYDOWN:
            continue
        if event.key == K_BACKSPACE:
            if ask == "age" and text[len(text) - 1] == ".":
                text = text[0:-2]
            else:
                text = text[0:-1]
        elif event.key == K_RETURN:
            break
        else:
            text += event.unicode
            if ask == "age":
                if len(text) == 2 or len(text) == 5:
                    text += "."
        display_box(screen, text, pos)
    return text


class DataPool:
    data = []

    def __init__(self, data):
        self.data = data

    def get_match_day(self, data):
        daily_teams = []
        pointer = 0
        while pointer < 32:
            check_data = self.data[pointer][0]
            if check_data == data:
                amount = self.data[pointer][1] + 2
                counter = 2
                while counter < amount:
                    daily_teams.append(self.data[pointer][counter])
                    counter += 1
            pointer += 1
        return daily_teams


class League:
    _Name = ''
    _Positions = []
    _Teams = []

    def __init__(self, Name, Teams):
        self.Name = Name
        self.Teams = Teams


class MatchTeam:
    Substitution = 0
    Team = 0
    AllPass = 0
    SecsessfulPass = 0
    AllShoots = 0
    SecsessfulShoots = 0
    Save = 0
    Prossession = 0
    Goals = 0
    YellowCards = 0
    RedCards = 0

    def __init__(self, Team):
        self.Team = Team
        self.Substitution = 3

    def add_goal(self):
        self.AllShoots += 1
        self.SecsessfulShoots += 1
        self.Goals += 1

    def add_shoot(self):
        self.AllShoots += 1

    def add_secsessful_shoot(self):
        self.SecsessfulShoots += 1
        self.AllShoots += 1

    def add_pass(self):
        self.AllPass += 1

    def add_secsessful_pass(self):
        self.SecsessfulPass += 1

    def add_save(self):
        self.Save += 1

    def add_prossession(self):
        self.Prossession += 1

    def add_yellow(self, player):
        self.YellowCards += 1
        self.Team.StartPlayers[player].YellowCard += 1
        if self.Team.StartPlayers[player].YellowCard == 2:
            self.add_red(player)

    def add_red(self, player):
        self.RedCards += 1
        self.Team.StartPlayers[player].YellowCard = 0
        self.Team.StartPlayers[player].RedCard = 1


class PoolPlayers:
    _AllPlayers = []

    def __init__(self, Players):
        self.AllPlayers = Players

    def Request(self, Club):
        RequestedPlayers = []
        for Player in self.AllPlayers:
            if Player.Club == Club:
                RequestedPlayers.append(Player)
        return RequestedPlayers


class Player:
    _Name = ''
    _Surname = ''
    _Position = ''
    _Club = ''
    _Cost = 0
    _Contract = 0
    _Age = 0
    _Rating = 0
    _Shoot = 0
    _Pass = 0
    _Speed = 0
    _Strenght = 0
    _Dribbling = 0
    _Defense = 0
    _Fall = 0
    _Reaction = 0
    _Hand = 0
    _GkPos = 0
    _Leg = 0
    RedCard = 0
    YellowCard = 0
    IsSubstitution = 0

    def __init__(self, information):
        self.Name = information[0]
        self.Surname = information[1]
        self.Position = information[2]
        self.Club = information[3]
        self.Age = int(information[4])
        self.Contract = information[5]
        self.Speed = int(information[6])
        self.Dribbling = int(information[7])
        self.Shoot = int(information[8])
        self.Pass = int(information[9])
        self.Defense = int(information[10])
        self.Strenght = int(information[11])
        self.Fall = int(information[12])
        self.Reaction = int(information[13])
        self.Hand = int(information[14])
        self.GkPos = int(information[15])
        self.Leg = int(information[16])
        if self.Position == 'GK':
            self.Rating = int((self.Fall + self.Reaction + self.Hand + self.GkPos + self.Leg) / 5)
        if self.Position == 'DF':
            self.Rating = int((self.Defense + self.Pass + self.Speed + self.Strenght) / 4)
        if self.Position == 'MD':
            self.Rating = int((self.Pass + self.Speed + self.Shoot / 2 + self.Dribbling / 2 + self.Speed) / 4)
        if self.Position == 'ST':
            self.Rating = int((self.Shoot + self.Speed + self.Strenght + self.Dribbling + self.Pass / 2) / 4.5)
        self.Cost = self.Rating * 500000


class Team:
    _Name = ''
    _Color = []
    _Teg = 0
    _Points = 0
    _Coach = 0
    _Tactic = 0
    _Tactic1 = 0
    _Tactic2 = 0
    _AllPlayers = []
    _StartPlayers = []
    _ReservePlayers = []
    _Defenders = 0
    _Middefenders = 0
    _Strikers = 0
    Points = 0
    WinGames = 0
    LoseGames = 0
    DrawGames = 0
    Games = 0
    GoalsScore = 0
    GoalsLose = 0

    def __init__(self, Name, Teg, Color, Money, Coach, TeamPlayers):
        self.Teg = Teg
        self.Name = Name
        self.Color = Color
        self.Money = Money
        self.Coach = Coach
        self.Tactic1 = Coach.AttackTactic
        self.Tactic2 = Coach.DefendTactic
        if self.Coach.Style == 'Attack':
            self.Tactic = self.Tactic1
        else:
            self.Tactic = self.Tactic2
        self.AllPlayers = TeamPlayers
        self.StartPlayers = FillStartSquad(self.AllPlayers, self.Tactic)
        self.ReservePlayers = FillReserve(self.AllPlayers, self.StartPlayers)
        self.Strikers = self.Tactic1 % 10
        Tactic = int(self.Tactic1 / 10)
        self.Middefenders = Tactic % 10
        Tactic = int(Tactic / 10)
        self.Defenders = Tactic % 10


class CoachPool:
    Coaches = 0

    def __init__(self, Coaches):
        self.Coaches = Coaches

    def RequestCoach(self, ClubName):
        for Coach in self.Coaches:
            if Coach.Club == ClubName:
                return Coach


class Coach:
    Name = ''
    Surname = ''
    Age = 0
    Nationality = ''
    Club = ''
    AttackTactic = 0
    DefendTactic = 0
    Style = ''

    def __init__(self, information):
        self.Name = information[0]
        self.Club = information[4]
        self.Surname = information[1]
        self.Nationality = information[2]
        self.Age = information[3]
        self.AttackTactic = int(information[5])
        self.DefendTactic = int(information[6])
        self.Style = information[7]
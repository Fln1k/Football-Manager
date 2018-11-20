from TeamClass import FillStartSquad
from TeamClass import FillReserve

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

    def addGoal(self):
        self.AllShoots += 1
        self.SecsessfulShoots += 1
        self.Goals += 1

    def addShoot(self):
        self.AllShoots += 1

    def addSecsessfilShoot(self):
        self.SecsessfulShoots += 1
        self.AllShoots += 1

    def addPass(self):
        self.AllPass += 1

    def addSecsessfulPass(self):
        self.SecsessfulPass += 1

    def addSave(self):
        self.Save += 1

    def addProssession(self):
        self.Prossession += 1

    def addYellow(self, player):
        self.YellowCards += 1
        self.Team.StartPlayers[player].YellowCard += 1
        if self.Team.StartPlayers[player].YellowCard == 2:
            self.addRed(player)

    def addRed(self, player):
        self.RedCards += 1
        self.Team.StartPlayers[player].YellowCard = 0
        self.Team.StartPlayers[player].RedCard = 1


class PoolPlayers:
    _AllPlayers=[]
    def __init__(self,Players):
        self.AllPlayers=Players
    def Request(self,Club):
        RequestedPlayers=[]
        for Player in self.AllPlayers:
            if Player.Club==Club:
                RequestedPlayers.append(Player)
        return RequestedPlayers



class Player:
    _Name=''
    _Surname=''
    _Position=''
    _Club=''
    _Cost=0
    _Contract=0
    _Age=0
    _Rating=0
    _Shoot=0
    _Pass=0
    _Speed=0
    _Strenght=0
    _Dribbling=0
    _Defense=0
    _Fall=0
    _Reaction=0
    _Hand=0
    _GkPos=0
    _Leg=0
    RedCard=0
    YellowCard=0
    IsSubstitution=0
    def __init__(self,information):
        self.Name= information[0]
        self.Surname=information[1]
        self.Position=information[2]
        self.Club=information[3]
        self.Age=int(information[4])
        self.Contract=information[5]
        self.Speed=int(information[6])
        self.Dribbling=int(information[7])
        self.Shoot=int(information[8])
        self.Pass=int(information[9])
        self.Defense=int(information[10])
        self.Strenght=int(information[11])
        self.Fall=int(information[12])
        self.Reaction=int(information[13])
        self.Hand=int(information[14])
        self.GkPos=int(information[15])
        self.Leg=int(information[16])
        if self.Position=='GK':
            self.Rating=int((self.Fall+self.Reaction+self.Hand+self.GkPos+self.Leg)/5)
        if self.Position=='DF':
            self.Rating=int((self.Defense+self.Pass+self.Speed+self.Strenght)/4)
        if self.Position=='MD':
            self.Rating=int((self.Pass+self.Speed+self.Shoot/2+self.Dribbling/2+self.Speed)/4)
        if self.Position=='ST':
            self.Rating=int((self.Shoot+self.Speed+self.Strenght+self.Dribbling+self.Pass/2)/4.5)
        self.Cost=self.Rating*500000

class Team:
    _Name=''
    _Color=[]
    _Points=0
    _Coach=0
    _Tactic=0
    _Tactic1=0
    _Tactic2=0
    _AllPlayers=[]
    _StartPlayers=[]
    _ReservePlayers=[]
    _Defenders=0
    _Middefenders=0
    _Strikers=0
    Points=0
    WinGames=0
    LoseGames=0
    DrawGames=0
    Games=0
    GoalsScore=0
    GoalsLose=0
    def __init__(self,Name,Color,Money,Coach,TeamPlayers):
        self.Name=Name
        self.Color=Color
        self.Money=Money
        self.Coach=Coach
        self.Tactic1 = Coach.AttackTactic
        self.Tactic2 = Coach.DefendTactic
        if self.Coach.Style=='Attack':
            self.Tactic=self.Tactic1
        else:
            self.Tactic=self.Tactic2
        self.AllPlayers=TeamPlayers
        self.StartPlayers=FillStartSquad(self.AllPlayers,self.Tactic)
        self.ReservePlayers=FillReserve(self.AllPlayers,self.StartPlayers)
        self.Strikers=self.Tactic1%10
        Tactic=int(self.Tactic1/10)
        self.Middefenders=Tactic%10
        Tactic=int(Tactic/10)
        self.Defenders=Tactic%10

class CoachPool:
    _Coaches=[]
    def __init__(self,Coaches):
        self.Coaches=Coaches
    def RequestCoach(self,ClubName):
        for Coach in self.Coaches:
            if Coach.Club==ClubName:
                return Coach

class Coach:
    _Name=''
    _Surname=''
    _Age=0
    _Nationality=''
    _Club=''
    _AttackTactic=0
    _DefendTactic=0
    _Style=''
    def __init__(self,information):
        self.Name=information[0]
        self.Club=information[4]
        self.Surname=information[1]
        self.Nationality=information[2]
        self.Age=information[3]
        self.AttackTactic=int(information[5])
        self.DefendTactic=int(information[6])
        self.Style=information[7]

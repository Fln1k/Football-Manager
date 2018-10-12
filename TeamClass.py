<<<<<<< HEAD
def findmin(amount):
    min = 101
    minindex=0
    counter = 0
    for counter in amount:
        if  min>counter:
             min=counter
    return amount.index(min)

def FillStartSquad(AllPlayers,Tactic):
    StartPlayers=[]
    Tactic1=Tactic
    Strikers = int(Tactic1 % 10)
    Tactic = int(Tactic / 10)
    Middefenders = int(Tactic % 10)
    Tactic = int(Tactic / 10)
    Defenders = int(Tactic % 10)
    GKRATING=0
    DefendersRating=[]
    while Defenders>0:
        DefendersRating.append(0)
        Defenders-=1
    MiddefendersRating=[]
    while Middefenders>0:
        MiddefendersRating.append(0)
        Middefenders-=1
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
        if Player.Position=='GK' and Player.Rating>GKRATING:
            if len(StartPlayers)>0:
                StartPlayers.pop(0)
            StartPlayers.append(Player)
            GKRATING=Player.Rating
        if Player.Position=='DF' and Player.Rating>DefendersRating[findmin(DefendersRating)]:
            if len(StartPlayers)>Defenders:
                StartPlayers.pop(1+findmin(DefendersRating))
            StartPlayers.append(Player)
            DefendersRating[findmin(DefendersRating)]=Player.Rating
        elif Player.Position=='MD' and Player.Rating>MiddefendersRating[findmin(MiddefendersRating)]:
            if len(StartPlayers)>Defenders+Middefenders:
                StartPlayers.pop(1+Defenders+findmin(MiddefendersRating))
            StartPlayers.append(Player)
            MiddefendersRating[findmin(MiddefendersRating)] = Player.Rating
        elif Player.Position=='ST' and Player.Rating>StrikersRating[findmin(StrikersRating)]:
            if len(StartPlayers)>Defenders+Middefenders+Strikers:
                StartPlayers.pop(1+Defenders+Middefenders+findmin(StrikersRating))
            StartPlayers.append(Player)
            StrikersRating[findmin(StrikersRating)] = Player.Rating
    return StartPlayers

class Team:
    _Name=''
    _Color=''
    _Points=0
    _Coach=0
    _Tactic=0
    _AllPlayers=[]
    _StartPlayers=[]
    _ReservePlayers=[]
    _Defenders=0
    _Middefenders=0
    _Strikers=0
    def __init__(self,Name,Color,Money,Coach,Tactic,TeamPlayers):
        self.Name=Name
        self.Color=Color
        self.Money=Money
        self.Coach=Coach
        self.Tactic=Tactic
        self.AllPlayers=TeamPlayers
        self.StartPlayers=FillStartSquad(self.AllPlayers,self.Tactic)
        self.Strikers=self.Tactic%10
        Tactic=int(self.Tactic/10)
        self.Middefenders=Tactic%10
        Tactic=int(Tactic/10)
        self.Defenders=Tactic%10
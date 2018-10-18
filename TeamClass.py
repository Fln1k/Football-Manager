def findmin(amount):
    min = 101
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

def FillReserve(AllPlayers,StartPlayers):
    Reserve=[]
    GKRating=0
    DFRating=[0,0]
    MDRating=[0,0,0]
    STRating=0
    for Player in AllPlayers:
        Start=False
        for Player1 in StartPlayers:
            if Player.Surname==Player1.Surname:
                Start=True
        if Start==False:
            if Player.Position=='GK' and (len(Reserve)==0 or Player.Rating>GKRating):
                if len(Reserve)==1:
                    Reserve.pop(0)
                Reserve.append(Player)
            if Player.Position=='DF' and (len(Reserve)<3 or Player.Rating>findmin(DFRating)):
                if len(Reserve) > 2:
                    Reserve.pop(1 + findmin(DFRating))
                Reserve.append(Player)
                DFRating[findmin(DFRating)] = Player.Rating
            if Player.Position=='MD' and (len(Reserve)<5 or Player.Rating>findmin(MDRating)):
                if len(Reserve) > 5:
                    Reserve.pop(3 + findmin(MDRating))
                Reserve.append(Player)
                MDRating[findmin(MDRating)] = Player.Rating
            if Player.Position=='ST' and (len(Reserve)<7 or Player.Rating>STRating):
                if len(Reserve) == 7:
                    Reserve.pop(6)
                Reserve.append(Player)
                STRating = Player.Rating
    return Reserve


class Team:
    _Name=''
    _Color=''
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
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

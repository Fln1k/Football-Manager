class MatchTeam:
        Substitution=0
        Team=0
        AllPass = 0
        SecsessfulPass = 0
        AllShoots = 0
        SecsessfulShoots = 0
        Save = 0
        Prossession = 0
        Goals = 0
        YellowCards=0
        RedCards=0
        def __init__(self,Team):
                self.Team=Team
                self.Substitution=3
        def addGoal(self):
                self.AllShoots+=1
                self.SecsessfulShoots+=1
                self.Goals+=1
        def addShoot(self):
                self.AllShoots+=1
        def addSecsessfilShoot(self):
                self.SecsessfulShoots+=1
                self.AllShoots+=1
        def addPass(self):
                self.AllPass+=1
        def addSecsessfulPass(self):
                self.SecsessfulPass+=1
        def addSave(self):
                self.Save+=1
        def addProssession(self):
                self.Prossession+=1
        def addYellow(self,player):
                self.YellowCards+=1
                self.Team.StartPlayers[player].YellowCard+=1
                if self.Team.StartPlayers[player].YellowCard==2:
                        self.addRed(player)
        def addRed(self,player):
                self.RedCards+=1
                self.Team.StartPlayers[player].YellowCard=0
                self.Team.StartPlayers[player].RedCard=1

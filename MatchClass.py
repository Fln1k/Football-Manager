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

    def __init__(self, team):
        self.Team = team
        self.Substitution = 3

    def add_goal(self):
            self.AllShoots += 1
            self.SecsessfulShoots += 1
            self.Goals += 1

    def add_shoot(self):
            self.AllShoots += 1

    def add_secsessfull_shoot(self):
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
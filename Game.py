from Assets.Modules.Models import *


class Game:
    WindowHeight = 1280
    WindowWidth = 720
    WindowDefaultHeight = 1280
    WindowDefaultWidth = 720
    Ratio = WindowHeight / WindowDefaultHeight
    screen = pygame.display.set_mode((WindowDefaultHeight, WindowDefaultWidth))
    current_function = None
    font = None
    font_color = None
    kind = None
    ImageFolder = None
    player_team = "EPL"
    Done = False
    current_date=[0,0,0]
    GameFunc=None
    Manager = None
    DataPool = None
    Match = False
    table = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Football Manager")
        self.main_menu()
        self.GameFunc = AllFunctions()
        self.DataPool = DataPool(self.GameFunc.load_data())

    def run(self):
        self.kind = "MainMenu"
        while True:
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.kind == "MainMenu":
                            if event.pos[0] >= 160 and event.pos[0] <= 400 and event.pos[1] >= 200\
                                    and event.pos[1] <= 240:
                                self.create_coach()
                                self.kind="CreateCoach"
                            if event.pos[0] >= 120 and event.pos[0] <= 510 and event.pos[1] >= 300\
                                    and event.pos[1] <= 340:
                                self.current_function = 0
                            if event.pos[0] >= 80 and event.pos[0] <= 320 and event.pos[1] >= 400\
                                    and event.pos[1] <= 440:
                                self.current_function = 0
                            if event.pos[0] >= 40 and event.pos[0] <= 160 and event.pos[1] >= 500\
                                    and event.pos[1] <= 540:
                                self.current_function = sys.exit
                        elif self.kind == "CreateCoach":
                            if event.pos[0] >= 1010 and event.pos[1] >= 655:
                                self.ImageFolder = "Assets/Images/EPL Info.jpg"
                                self.team_menu()
                                self.kind = "team_menu"
                        elif self.kind == "team_menu":
                            if event.pos[1] >= 200 and event.pos[1] <= 230 and event.pos[0] >= 10 \
                                    and event.pos[0] <= 220:
                                self.player_team = "Chelsea"
                                self.team_menu()
                                self.Done = True
                            elif event.pos[1] >= 300 and event.pos[1] <= 330 and event.pos[0] >= 10 \
                                    and event.pos[0] <= 370:
                                self.player_team="Manchester City"
                                self.team_menu()
                                self.Done = True
                            elif event.pos[1] >= 400 and event.pos[1] <= 430 and event.pos[0] >= 10 \
                                    and event.pos[0] <= 410:
                                self.player_team = "Manchester United"
                                self.team_menu()
                                self.Done = True
                            elif event.pos[1] >= 500 and event.pos[1] <= 530 and event.pos[0] >= 10 \
                                    and event.pos[0] <= 280:
                                self.player_team = "Liverpool"
                                self.team_menu()
                                self.Done = True
                            elif event.pos[1] >= 600 and event.pos[1] <= 630 and event.pos[0] >= 10 \
                                    and event.pos[0] <= 220:
                                self.player_team = "Arsenal"
                                self.team_menu()
                                self.Done = True
                            self.ImageFolder = "Assets/Images/"+self.player_team+" Info.jpg"
                            if self.Done:
                                if event.pos[0] >= 1010 and event.pos[1] >= 655:
                                    self.kind = "GameMenu"
                                    self.ImageFolder = "Assets/Images/GameMenu.jpg"
                                    self.game_menu()
                                    self.update_table()
                                    self.Done=False
                        elif self.kind == "WAIT":
                            if event.pos[0] >= 1010 and event.pos[1] >= 655:
                                match_array=[]
                                playermatch = False
                                while not playermatch:
                                    counter = 0
                                    while counter<len(match_array):
                                        if match_array[counter].Name != self.player_team.Name\
                                                and match_array[counter+1].Name != self.player_team.Name:
                                            time = 0
                                            match_info = self.GameFunc.match_simulation(match_array[0],match_array[1],self.player_team,time,0)
                                            while time<180:
                                                match_info = self.GameFunc.match_simulation(match_info[0],match_info[1],match_info[2],match_info[3],match_info[4])
                                                time = match_info[4]
                                            self.update_table()
                                        else:
                                            playermatch = True
                                        counter+=2
                                    if playermatch:
                                        break
                                    skip(self.current_date)
                                    self.game_menu()
                                    pygame.time.delay(1000)
                                    match_array = get_play_teams(self.current_date,self.DataPool,self.GameFunc)
                                if playermatch:
                                    counter = 0
                                    while counter < len(match_array):
                                        if (match_array[counter].Name == self.player_team.Name
                                                or match_array[counter + 1].Name == self.player_team.Name):
                                            self.Match = True
                                        counter+=2
                                if self.Match:
                                    self.screen.blit(self.font.render("Match", True, self.font_color), (1010, 655))
            pygame.display.update()

    def update_table(self):
        x,y=880,120
        self.font = pygame.font.Font(None, 30)
        self.screen.blit(self.font.render("Name", True, self.font_color), (x, y))
        self.screen.blit(self.font.render("G  W  D  L  P", True, self.font_color), (1120, y))
        for team in self.table.table:
            y += 35
            self.screen.blit(self.font.render(team.Name, True, self.font_color), (x, y))
            self.screen.blit(self.font.render(str(team.Games) +"   "+ str(team.WinGames) +"   "+\
                                              str(team.DrawGames) +"   "+ str(team.LoseGames) +"   "+\
                                              str(team.Points), True, self.font_color), (1120, y))
        pygame.display.update()

    def main_menu(self):
        self.font = pygame.font.Font(None, 64)
        self.font_color = (255, 255, 255)
        self.ImageFolder = "Assets/Images/MainMenu.jpg"
        self.screen.blit(pygame.image.load(self.ImageFolder).convert(), (0, 0))
        self.screen.blit(self.font.render("New Game", True, self.font_color), (160, 200))
        self.screen.blit(self.font.render("Continue", True, self.font_color), (120, 300))
        self.screen.blit(self.font.render("Settings", True, self.font_color), (80, 400))
        self.screen.blit(self.font.render("Quit", True, self.font_color), (40, 500))

    def create_coach(self):
        self.current_date=[1,8,2018]
        text = ""
        self.ImageFolder = "Assets/Images/CreateCoach.jpg"
        self.screen.blit(pygame.image.load(self.ImageFolder).convert(), (0, 0))
        name = ask(self.screen, text, (350,200), "name")
        surname = ask(self.screen, text, (350, 290), "surname")
        age = ""
        mistake = True
        while mistake:
            text=""
            while len(age) != 10:
                age = ask(self.screen, text, (350, 380), "age")
            counter=0
            while counter < len(age):
                if counter == 2 or counter == 5:
                    counter += 1
                if check_numeric(age[counter]):
                    counter += 1
                if counter == len(age):
                    mistake = False
                    if int(age[0] + age[1]) > 31 or age[0] == "-" or int(age[3] + age[4]) > 12 or int(
                            age[6] + age[7] + age[8] + age[9]) > 2000 or int(
                            age[6] + age[7] + age[8] + age[9]) <= 1950:
                        mistake = True
        nationality = ask(self.screen, text, (350, 470), "nationality")
        self.screen.blit(self.font.render("Continue", True, self.font_color), (1010,655))
        self.current_function=None
        self.Manager = Coach([name,surname,nationality,2018-int(age[6] + age[7] + age[8] + age[9]),None,433,442,"Defend"])

    def team_menu(self):
        if self.ImageFolder == "Assets/Images/EPL Info.jpg":
            self.screen.blit(pygame.image.load(self.ImageFolder).convert(), (0, 0))
        else:
            self.screen.blit(pygame.image.load(self.ImageFolder).convert(), (229, 105))
            if self.Done:
                self.font = pygame.font.Font(None, 64)
                self.screen.blit(self.font.render("Continue", True, self.font_color), (1010, 655))
        self.font = pygame.font.Font(None, 30)
        self.screen.blit(self.font.render("Chelsea", True, self.font_color), (10, 200))
        self.screen.blit(self.font.render("Manchester City", True, self.font_color), (10, 300))
        self.screen.blit(self.font.render("Manchester United", True, self.font_color), (10, 400))
        self.screen.blit(self.font.render("Liverpool", True, self.font_color), (10, 500))
        self.screen.blit(self.font.render("Arsenal", True, self.font_color), (10, 600))
        self.table = table(self.GameFunc.Leagues[0].Teams)

    def game_menu(self):
        for team in self.GameFunc.Leagues[0].Teams:
            if team.Name == self.player_team:
                self.player_team = team
                self.player_team.Coach = self.Manager
                break
        self.table.sort()
        self.font = pygame.font.Font(None, 60)
        self.screen.blit(pygame.image.load(self.ImageFolder).convert(), (0, 0))
        self.screen.blit(pygame.image.load("Assets/Images/"+self.player_team.Name+" Top.jpg").convert(), (0, 0))
        self.Manager.Club=self.player_team.Name
        self.screen.blit(self.font.render(self.Manager.Name +" "+ self.Manager.Surname, True, self.font_color), (0, 30))
        self.font = pygame.font.Font(None, 30)
        self.screen.blit(self.font.render("Messages", True, self.font_color), (10, 150))
        self.screen.blit(self.font.render("Finances", True, self.font_color), (10, 200))
        self.screen.blit(self.font.render("Squad", True, self.font_color), (10, 250))
        self.screen.blit(self.font.render("Transfers", True, self.font_color), (10, 300))
        self.screen.blit(self.font.render("Coach", True, self.font_color), (10, 350))
        self.screen.blit(self.font.render("Settings", True, self.font_color), (10, 400))
        self.screen.blit(pygame.image.load("Assets/Images/Field.jpg").convert(), (210, 120))
        self.update_table()
        self.font = pygame.font.Font(None, 30)
        x=210
        pygame.draw.circle(self.screen, (0, 255, 0), (540 , 640), 20)
        self.screen.blit(self.font.render(self.player_team.StartPlayers[0].Surname, True, self.font_color),
                         (540-len(self.player_team.StartPlayers[0].Surname)*6, 675))
        counter = 0
        x=300
        while counter<self.player_team.Defenders:
            pygame.draw.circle(self.screen, (0, 255, 0), (x, 530),20)
            self.screen.blit(self.font.render(self.player_team.StartPlayers[1+counter].Surname, True, self.font_color),
                             (x+10-len(self.player_team.StartPlayers[1+counter].Surname)*6, 565))
            x += int((880 - 220) / self.player_team.Defenders)
            counter+=1
        x = 320
        while counter<self.player_team.Defenders+self.player_team.Middefenders:
            pygame.draw.circle(self.screen, (0, 255, 0), (x, 420),20)
            self.screen.blit(self.font.render(self.player_team.StartPlayers[1+counter].Surname, True, self.font_color),
                             (x+10-len(self.player_team.StartPlayers[1+counter].Surname)*6,
                              455))
            x += int((880 - 220) / self.player_team.Middefenders)
            counter+=1
        x = 320
        while counter < 10:
            pygame.draw.circle(self.screen, (0, 255, 0), (x, 250), 20)
            self.screen.blit(
                self.font.render(self.player_team.StartPlayers[1 + counter].Surname, True, self.font_color),
                (x + 10 - len(self.player_team.StartPlayers[1 + counter].Surname) * 6,
                 286))
            x += int((880 - 220) / self.player_team.Strikers)
            counter += 1
        self.font = pygame.font.Font(None, 50)
        self.screen.blit(self.font.render(
            str(self.current_date[0]) + "." + str(self.current_date[1]) + "." + str(self.current_date[2]), True,
            self.font_color), (1100, 30))
        self.font = pygame.font.Font(None, 64)
        self.kind = "WAIT"
        if not self.Match:
            self.screen.blit(self.font.render("Continue", True, self.font_color),
                             (1010, 655))
        pygame.display.update()

    def match(self):
        pass

game = Game()
game.run()
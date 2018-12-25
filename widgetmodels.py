from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.uix.videoplayer import Video
from kivy.clock import Clock
from GameFunctionsClass import AllFunctions
from classmodels import Update
import weakref


def matchday(data):
    if data[0] == 10:
        if data[1] == 8:
            if data[2] == 2018:
                return True
    return False


class FootballManagerApp(App):
    table = []
    PlayerTeam = 0
    Data = [0, 0, 0]
    WindowHight = 1280
    WindowWidth = 720
    WindowDefaultHight = 1280
    WindowDefaultWidth = 720
    Ratio = WindowHight / WindowDefaultHight
    Window.size = (WindowHight, WindowWidth)
    Widget = 0
    Widgetarray = 0
    MainClass = 0
    GameFuncs = 0
    UpdateArgs = 0
    skipdays=0
    coach_label = ((Label(markup = True,color=[1,1,1,1], pos=(Ratio * 30, Ratio * (WindowWidth - Ratio * 100)),size=(Ratio * 200, Ratio * 100),font_size='40sp')))
    name = TextInput(foreground_color=[255, 255, 255, 1], focus=False, multiline=False,size=(Ratio * 250,Ratio * 48), background_color=(0.400, 0.400, 0.400, 1),pos=(320, 465))
    surname = TextInput(foreground_color=[255, 255, 255, 1], focus=False, multiline=False,size=(Ratio * 250,Ratio * 48), background_color=(0.400, 0.400, 0.400, 1),pos=(320, 373))
    nationality_button = Button(size=(Ratio * 250, Ratio * 48),pos=(Ratio * 320, Ratio * 190))
    day_button = Button(size=(Ratio * 60,Ratio * 50), pos=(Ratio * 320, Ratio * 283))
    month_button = Button(size=(Ratio * 60,Ratio * 50), pos=(Ratio * 390,Ratio * 283))
    year_button = Button(size=(Ratio * 110, Ratio * 50), pos=(Ratio * 460,Ratio * 283))
    main_menu_background = (Image(allow_stretch=True, keep_ratio=False, size=(WindowHight, WindowWidth)))
    match_background = (Image(allow_stretch=True, keep_ratio=False, size=(WindowHight, WindowWidth), source='Images\Match.jpg'))
    time_label = (Label(markup=True, color=[1, 1, 1, 1], pos=(Ratio * 0, Ratio * (WindowWidth - Ratio * 48)),size=(Ratio * 100, Ratio * 48), font_size='30sp'))
    data_label=(Label(markup=True, color=[0, 1, 1, 1], pos=(Ratio * (WindowHight - Ratio * 1070), Ratio * (WindowWidth - Ratio * 720)),size=(Ratio * 200, Ratio * 48), font_size='30sp'))
    name_team_label = (Label(markup=True, color=[1, 1, 1, 1], pos=(Ratio * (WindowHight - Ratio * 1120), Ratio * (WindowWidth - Ratio * 48)),size=(Ratio * 100, Ratio * 48), font_size='30sp'))
    activ_team_label = (Label(markup=True, color=[0, 1, 1, 1], pos=(Ratio * (WindowHight - Ratio * 1240), Ratio * (WindowWidth - Ratio * 100)),size=(Ratio * 200, Ratio * 48), font_size='30sp'))
    activ_player_label = (Label(markup=True, color=[0, 1, 1, 1], pos=(Ratio * (WindowHight - Ratio * 1140), Ratio * (WindowWidth - Ratio * 150)),size=(Ratio * 200, Ratio * 48), font_size='30sp'))
    epl_background = (Image(allow_stretch=True, keep_ratio=False, size=(WindowHight, WindowWidth), source='Images\EPL.jpg'))


    def build(self):
        array = [0, 0, 0, 0, 0, 0, 0, 0]
        self.UpdateArgs=Update(array)
        self.GameFuncs=AllFunctions(weakref.ref(self.UpdateArgs))
        self.Widget = Widget()
        background = (Image(allow_stretch=True, keep_ratio=False, size=(self.WindowHight, self.WindowWidth), source='Images\StartGame.jpg'))
        Widgetarraycontinue_button = (Button(text="Continue", font_size=self.Ratio * 34, on_press=self.continue_the_game,background_color=[45, 100, 0, 0], pos=(self.Ratio * 63, self.Ratio * 416),size=(self.Ratio * 300, self.Ratio * 48)))
        settings_button = (Button(text="Settings", font_size=self.Ratio * 34, on_press=self.game_settings,background_color=[45, 100, 0, 0], pos=(self.Ratio * 18, self.Ratio * 356),size=(self.Ratio * 300, self.Ratio * 48)))
        quit_button = (Button(text="Quit", font_size=self.Ratio * 34, on_press=self.exit_the_game,background_color=[45, 100, 0, 0], pos=(self.Ratio * -52, self.Ratio * 296),size=(self.Ratio * 300, self.Ratio * 48)))
        new_game_button = (Button(text="New Game",on_press=self.create_coach, font_size=self.Ratio * 34, background_color=[45, 100, 0, 0],pos=(self.Ratio * 116, self.Ratio * 476), size=(self.Ratio * 300, self.Ratio * 48)))
        self.Widget.add_widget(background)
        self.Widget.add_widget(new_game_button)
        self.Widget.add_widget(Widgetarraycontinue_button)
        self.Widget.add_widget(settings_button)
        self.Widget.add_widget(quit_button)
        return self.Widget
    

    def continue_the_game(self, instance):
        pass


    def game_settings(self, instance):
        pass
    

    def exit_the_game(self):
        exit()
    

    def create_coach(self, instance):
        self.Data = [1, 8, 2018]
        background = (Image(allow_stretch=True, keep_ratio=False, size=(self.WindowHight, self.WindowWidth),source='Images\Coach.png'))
        continue_button = Button(text="Continue", font_size=self.Ratio * 34,on_press=self.save_coach,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        dropdown = DropDown()
        countries = ["Austrian", "Belgian", "Dutch", "England", "French", "German"]
        for country in countries:
            countries = Button(text='%r' % country, size_hint_y=None, height=30)
            countries.bind(on_release=lambda countries: dropdown.select(countries.text))
            dropdown.add_widget(countries)
        self.nationality_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.nationality_button, 'text', x))

        day = DropDown()
        date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                28, 29, 30]
        for daj in date:
            days = Button(text='%r' % daj, size_hint_y=None, height=30)
            days.bind(on_release=lambda days: day.select(days.text))
            day.add_widget(days)
        self.day_button.bind(on_release=day.open)
        day.bind(on_select=lambda instance, x: setattr(self.day_button, 'text', x))

        curmonth = DropDown()
        month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month_ in month:
            months = Button(text='%r' % month_, size_hint_y=None, height=30)
            months.bind(on_release=lambda months: curmonth.select(months.text))
            curmonth.add_widget(months)
        self.month_button.bind(on_release=curmonth.open)
        curmonth.bind(on_select=lambda instance, x: setattr(self.month_button, 'text', x))

        curyear = DropDown()
        year = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001]
        for year_ in year:
            years = Button(text='%r' % year_, size_hint_y=None, height=30)
            years.bind(on_release=lambda years: curyear.select(years.text))
            curyear.add_widget(years)
        self.year_button.bind(on_release=curyear.open)
        curyear.bind(on_select=lambda instance, x: setattr(self.year_button, 'text', x))
        self.Widget.add_widget(background)
        self.Widget.add_widget(self.name)
        self.Widget.add_widget(self.surname)
        self.Widget.add_widget(self.nationality_button)
        self.Widget.add_widget(self.day_button)
        self.Widget.add_widget(self.month_button)
        self.Widget.add_widget(self.year_button)
        self.Widget.add_widget(continue_button)
        return self.Widget
    

    def save_coach(self,instance):
        self.coach_label.text = str(self.name.text+" "+self.surname.text)
        if self.name.text == "" or self.surname.text == "" or self.nationality_button.text == "" or self.day_button.text == "" or self.month_button.text == "" or self.year_button.text == "":
            self.Widget.add_widget(Label(markup = True,color=[1,1,1,1],text = 'enter all parameters ',pos=(self.Ratio*200,self.Ratio*550),size=(self.Ratio*300,self.Ratio*48),font_size='50sp'))
        else:
            self.enter_league(self)
        return self.Widget
    

    def enter_league(self,instance):
        create_team_background = (Image(allow_stretch=True, keep_ratio=False, size=(self.WindowHight, self.WindowWidth),source='Images\TeamMenu.jpg'))
        self.Widget.add_widget(create_team_background)
        epl_button = (Button(text="EPL", font_size=self.Ratio * 34, on_press=self.enter_team, background_color=[1, 1, 1, 0],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 195)),size=(self.Ratio * 236, self.Ratio * 105)))
        self.Widget.add_widget(self.coach_label)
        self.Widget.add_widget(epl_button)
        return self.Widget
    

    def enter_team(self,instance):
        self.Widget.remove_widget(self.coach_label)
        self.Widget.add_widget(self.epl_background)
        ARSENAL_button = (Button(text="ARSENAL", font_size=self.Ratio * 25, on_press=self.arsenal, background_color=[1, 1, 1, 0],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 300)),size=(self.Ratio * 236, self.Ratio * 105)))
        CHELSEA_button = (Button(text="CHELSEA", font_size=self.Ratio * 25, on_press=self.chelsea, background_color=[1, 1, 1, 0],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 405)),size=(self.Ratio * 236, self.Ratio * 105)))
        LIVERPOOL_button = (Button(text="LIVERPOOL", font_size=self.Ratio * 25,on_press=self.liverpool, background_color=[1, 1, 1, 0],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 510)),size=(self.Ratio * 236, self.Ratio * 105)))
        MANCHESTER_CITY_button = (Button(text="MANCHESTER CITY", font_size=self.Ratio * 25,on_press=self.manchester_city, background_color=[1, 1, 1, 0],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 615)),size=(self.Ratio * 236, self.Ratio * 105)))
        self.Widget.add_widget(ARSENAL_button)
        self.Widget.add_widget(CHELSEA_button)
        self.Widget.add_widget(LIVERPOOL_button)
        self.Widget.add_widget(MANCHESTER_CITY_button)
        self.Widget.add_widget(self.coach_label)
        for team in self.GameFuncs.Leagues[0].Teams:
            self.table.append(team)
        return self.Widget
    

    def arsenal(self,instance):
        self.epl_background.source='Images\TEAM\ARSENAL\ARSENALINFO.jpg'
        self.main_menu_background.source = 'Images\TEAM\ARSENAL\MainMenuArsenal.jpg'
        continue_button = Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        self.Widget.add_widget(continue_button)
        self.PlayerTeam = 'Arsenal'
        return self.Widget
    

    def chelsea(self,instance):
        self.epl_background.source = 'Images\TEAM\CHELSEA\CHELSEAINFO.jpg'
        self.main_menu_background.source = 'Images\TEAM\CHELSEA\MainMenuChelsea.jpg'
        continue_button = Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        self.Widget.add_widget(continue_button)
        self.PlayerTeam = 'Chelsea'
        return self.Widget
    

    def liverpool(self, instance):
        self.epl_background.source = 'Images\TEAM\LIVERPOOL\LIVERPOOLINFO.jpg'
        self.main_menu_background.source = 'Images\TEAM\LIVERPOOL\MainMenuLiverpool.jpg'
        continue_button = Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        self.Widget.add_widget(continue_button)
        self.PlayerTeam = 'Liverpool'
        return self.Widget
    

    def manchester_city(self, instance):
        self.epl_background.source = 'Images\TEAM\MANCHESTER_CITY\MANCHESTER_CITYINFO.jpg'
        self.main_menu_background.source = 'Images\TEAM\MANCHESTER_CITY\MainMenuManchesterCity.jpg'
        continue_button = Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        self.Widget.add_widget(continue_button)
        self.PlayerTeam = 'Manchester City'
        return self.Widget
    

    def main_menu(self,insatnce):
        self.Widget.remove_widget(self.coach_label)
        mail_button = (Button(text="Mail", font_size=self.Ratio * 34, on_press=self.mail, background_color=[1, 1, 1, 1], pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 195)),size=(self.Ratio * 236, self.Ratio * 105)))
        finance_button = (Button(text="Finance", font_size=self.Ratio * 34, on_press=self.finance, background_color=[1, 1, 1, 1],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 300)),size=(self.Ratio * 236, self.Ratio * 105)))
        transfers_button = (Button(text="Transfers", font_size=self.Ratio * 34, on_press=self.transfers, background_color=[1, 1, 1, 1],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 405)),size=(self.Ratio * 236, self.Ratio * 105)))
        coach_button = (Button(text="Coach", font_size=self.Ratio * 34, on_press=self.coach, background_color=[1, 1, 1, 1],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 510)),size=(self.Ratio * 236, self.Ratio * 105)))
        squad_button = (Button(text="Squad", font_size=self.Ratio * 34, on_press=self.squad, background_color=[1, 1, 1, 1],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 615)),size=(self.Ratio * 236, self.Ratio * 105)))
        settings_button = (Button(text="Settings", font_size=self.Ratio * 34, on_press=self.game_settings,background_color=[1, 1, 1, 1],pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 720)),size=(self.Ratio * 236, self.Ratio * 105)))
        table_lable = (Label(markup=True, color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 215), self.Ratio *(self.WindowWidth - self.Ratio * 150)),size=(self.Ratio * 100, self.Ratio * 48), font_size='20sp'))
        self.data_label.text = str(self.Data[0]) + str(".") + str(self.Data[1]) + str(".") + str(self.Data[2])
        self.table = sorted(self.table, key=lambda k: k.Points)
        max_symbols_amount = 17
        for team in self.table:
            table_lable.text += str(team.Name)
            counter = 0
            while len(team.Name)+counter <= max_symbols_amount:
                table_lable.text += ' '
                counter += 1
            table_lable.text += str(team.WinGames) + ' ' + str(team.DrawGames)+ ' ' + str(team.LoseGames)+ ' ' + str(team.Points) + str('\n')
        self.Widget.add_widget(self.main_menu_background)
        self.Widget.add_widget(mail_button)
        self.Widget.add_widget(finance_button)
        self.Widget.add_widget(transfers_button)
        self.Widget.add_widget(coach_button)
        self.Widget.add_widget(squad_button)
        self.Widget.add_widget(settings_button)
        self.Widget.add_widget(table_lable)
        self.Widget.add_widget(Button(background_normal='Images\Field.jpg', on_press=self.placement, pos=(self.Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),size=(self.Ratio * 768, self.Ratio * 580)))
        self.Widget.add_widget(self.data_label)
        self.Widget.add_widget(self.coach_label)
        if matchday(self.Data):
            match_button = (Button(text="Match", font_size=self.Ratio * 34, on_press=self.match, background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50)))
            self.Widget.add_widget(match_button)
        else:
            continue_button = (Button(text="Skip Days", font_size=self.Ratio * 34, on_press=self.cicle, background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50)))
            self.Widget.add_widget(continue_button)
        return self.Widget
    

    def mail(self, instance):
        self.Widget.remove_widget(self.data_label)
        self.Widget.remove_widget(self.coach_label)
        self.Widget.remove_widget(self.main_menu_background)
        mail_background = (Image(allow_stretch=True, keep_ratio=False, size=(self.WindowHight, self.WindowWidth), source='Images\Mail.jpg'))
        message = Button(text="Welcome Message", font_size=self.Ratio * 34, on_press=self.message, background_color=[1, 1, 1, 0],pos=(self.Ratio * 50, self.Ratio * (self.WindowWidth - self.Ratio * 100)),size=(self.Ratio * 236, self.Ratio * 105))
        self.Widget.add_widget(mail_background)
        self.Widget.add_widget(message)
        mail_back = Button(text="Back", font_size=self.Ratio * 34, on_press=self.main_menu,background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50))
        self.Widget.add_widget(mail_back)
        return self.Widget


    def message(self, instance):
        pass

    def finance(self, instance):
        pass
    

    def transfers(self, instance):
        pass
    

    def coach(self, instance):
        pass
    

    def squad(self, instance):
        pass


    def placement(self, instance):
        pass
    

    def match(self,instance):
        self.Leagues = self.GameFuncs.load_leagues()
        self.start_match()
        return self.Widget


    def start_match(self):
        self.GameFuncs.load_team(self.Leagues[0].Teams[0],self.Leagues[0].Teams[1],self.UpdateArgs)
        Clock.schedule_interval(self.GameFuncs.match_simulation, 1)
        Clock.schedule_interval(self.Update, 1)
        self.Widget.add_widget(self.match_background)
        self.Widget.add_widget(self.time_label)
        self.Widget.add_widget(self.name_team_label)
        self.Widget.add_widget(self.activ_team_label)
        self.Widget.add_widget(self.activ_player_label)
        stat_button = (Button(text="Stats", font_size=self.Ratio*34,on_press=self.stat_match,background_color=[1,1,1,0],pos=(self.Ratio*(self.WindowHight-self.Ratio*256),self.Ratio*(self.WindowWidth-self.Ratio*216)),size=(self.Ratio*236,self.Ratio*50)))
        self.Widget.add_widget(stat_button)
        tactic_button = (Button(text="Tactic", font_size=self.Ratio*34,background_color=[1,1,1,0],pos=(self.Ratio*(self.WindowHight-self.Ratio*256),self.Ratio*(self.WindowWidth-self.Ratio*286)),size=(self.Ratio*236,self.Ratio*50)))
        self.Widget.add_widget(tactic_button)
        arrangement_button = (Button(text="Arrangement", font_size=self.Ratio*34,background_color=[1,1,1,0],pos=(self.Ratio*(self.WindowHight-self.Ratio*256),self.Ratio*(self.WindowWidth-self.Ratio*356)),size=(self.Ratio*236,self.Ratio*50)))
        self.Widget.add_widget(arrangement_button)

    def cicle(self, instance):
        self.skipdays = Clock.schedule_interval(self.skip, 0.5)

    def skip(self, instance):
        self.Data[0] += 1
        if self.Data[0] == 31:
            self.Data[0] = 1
            self.Data[1] += 1
            if self.Data[1] == 13:
                self.Data[1] = 1
                self.Data[2] += 1
        if matchday(self.Data):
            match_button = (Button(text="Match", font_size=self.Ratio * 34, on_press=self.match, background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50)))
            self.Widget.add_widget(match_button)
            Clock.unschedule(self.skipdays)
        else:
            continue_button = (Button(text="Skip Days", font_size=self.Ratio * 34, on_press=self.cicle, background_color=[1, 1, 1, 1],pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),size=(self.Ratio * 236, self.Ratio * 50)))
            self.Widget.add_widget(continue_button)
        self.data_label.text = str(self.Data[0]) + str(".") + str(self.Data[1]) + str(".") + str(self.Data[2])

    def stat_match(self,instance):
        pass

    def tactic_match(self, instance):
        pass

    def arrangment_match(self, instance):
        pass

    def Update(self, dt):
        time = int(self.UpdateArgs.UpdateArgs[6]/2)
        self.time_label.text = str(time)
        if time == 1 or time == 2 or time == 3 or time == 4 or time == 5 or time == 6 or time == 7 or time == 8 or time == 9:
            self.time_label.text = str(0) + str(time) + ':' + str(0) + str(0)
        else:
            self.time_label.text = str(time) + ':' + str(0) + str(0)
        if self.UpdateArgs.UpdateArgs[0].Team.Name == self.UpdateArgs.UpdateArgs[4].Team.Name:
            self.name_team_label.text = str(self.UpdateArgs.UpdateArgs[4].Team.Teg) + " " + str(self.UpdateArgs.UpdateArgs[0].Goals) + " - " + str(self.UpdateArgs.UpdateArgs[1].Goals) + " " + str(self.UpdateArgs.UpdateArgs[5].Team.Teg)
        else:
            self.name_team_label.text = str(self.UpdateArgs.UpdateArgs[4].Team.Teg) + " " + str(self.UpdateArgs.UpdateArgs[1].Goals) + " - " + str(self.UpdateArgs.UpdateArgs[0].Goals) + " " + str(self.UpdateArgs.UpdateArgs[5].Team.Teg)
        if self.UpdateArgs.UpdateArgs[3] == 'Half Time':
            self.activ_team_label.text = str('Half Time')
        else:
            self.activ_team_label.text = str(self.UpdateArgs.UpdateArgs[3])
            self.activ_player_label.text = str(self.UpdateArgs.UpdateArgs[2].Name)+str(" ")+str(self.UpdateArgs.UpdateArgs[2].Club)
            self.activ_player_label.color=self.UpdateArgs.UpdateArgs[0].Team.Color
        return self.Widget

    def play_video(self, instance, football_player):
        player = Video()
        if football_player.Surname == 'Hazard':
            player.source='Assets\Video\chelsea_hazard_goal.mkv'
        elif football_player.Surname == 'Morata':
            player.source='Assets\Video\chelsea_morata_goal.mkv'
        elif football_player.Surname == 'Borges':
            player.source='Assets\Video\chelsea_borges_goal.mkv'
        elif football_player.Surname == 'Aubameyang':
            player.source=r'Assets\Video\arsenal_aubameyang_goal.mkv'
        elif football_player.Surname == 'Lacazette':
            player.source=r'Assets\Video\arsenal_lacazette_goal.mkv'
        elif football_player.Surname == 'Ozil':
            player.source=r'Assets\Video\arsenal_ozil_goal.mkv'
        elif football_player.Club == 'Chelsea':
            player.source = 'Assets\Video\chelsea_goal.mkv'
        elif football_player.Club == 'Arsenal':
            player.source = r'Assets\Video\arsenal_goal.mkv'
        if player.eos:
            player.state = 'play'
        self.Widget.add_widget(player)
        return self.Widget

if __name__ == "__main__":
    FootballManagerApp().run()
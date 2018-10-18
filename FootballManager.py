from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from GameFunctionsClass import LoadPlayers
from GameFunctionsClass import LoadTeams
from GameFunctionsClass import LoadLeagues
from GameFunctionsClass import PointsKey
from MatchClass import Game
from MatchClass import MatchTeam
from CoachClass import Coach


class GameMenu(App):
    WindowHight = 1280
    WindowWidth = 720
    WindowDefaultHight = 1280
    WindowDefaultWidth = 720
    Ratio = WindowHight / WindowDefaultHight

    Manager = Coach['']

    name = TextInput(foreground_color=[255, 255, 255, 1], focus=False, multiline=False, size=(Ratio * 250, Ratio * 48),
                     background_color=(0.400, 0.400, 0.400, 1), pos=(320, 465))
    surname = TextInput(foreground_color=[255, 255, 255, 1], focus=False, multiline=False,
                        size=(Ratio * 250, Ratio * 48), background_color=(0.400, 0.400, 0.400, 1), pos=(320, 373))
    nationality_button = Button(size=(Ratio * 250, Ratio * 48), pos=(Ratio * 320, Ratio * 190))
    day_button = Button(size=(Ratio * 60, Ratio * 50), pos=(Ratio * 320, Ratio * 283))
    month_button = Button(size=(Ratio * 60, Ratio * 50), pos=(Ratio * 390, Ratio * 283))
    year_button = Button(size=(Ratio * 110, Ratio * 50), pos=(Ratio * 460, Ratio * 283))
    team_button = Button(text="Team", font_size=Ratio * 34,
                         pos=(Ratio * (WindowHight - Ratio * 556), Ratio * (WindowWidth - Ratio * 304)),
                         size=(Ratio * 250, Ratio * 48))
    main_menu_background = Image(allow_stretch=True, keep_ratio=False, size=(WindowHight, WindowWidth))

    game = Widget()

    def build(self):
        Window.size = (self.WindowHight, self.WindowWidth)

        self.game.add_widget(Image(allow_stretch=True, keep_ratio=False, size=(self.Ratio*self.WindowHight, self.Ratio*self.WindowWidth),
                                   source='Images\StartGame.jpg'))

        new_game_button = (
            Button(text="New Game", font_size=Ratio * 34, on_press=self.create_coach, background_color=[45, 100, 0, 0],
                   pos=(self.Ratio * 116, self.Ratio * 476), size=(self.Ratio * 300, self.Ratio * 48)))
        continue_button = (Button(text="Continue", font_size=self.Ratio * 34, on_press=self.continue_the_game,
                                  background_color=[45, 100, 0, 0], pos=(self.Ratio * 63, self.Ratio * 416),
                                  size=(self.Ratio * 300, self.Ratio * 48)))
        settings_button = (
            Button(text="Settings", font_size=Ratio * 34, on_press=self.game_settings, background_color=[45, 100, 0, 0],
                   pos=(self.Ratio * 18, self.Ratio * 356), size=(self.Ratio * 300, self.Ratio * 48)))
        quit_button = (
            Button(text="Quit", font_size=self.Ratio * 34, background_color=[45, 100, 0, 0], on_press=self.exit_the_game,
                   pos=(self.Ratio * -52, self.Ratio * 296), size=(self.Ratio * 300, self.Ratio * 48)))

        self.game.add_widget(new_game_button)
        self.game.add_widget(continue_button)
        self.game.add_widget(settings_button)
        self.game.add_widget(quit_button)

        return self.game

    def continue_the_game(self, instance):
        pass

    def game_settings(self, instance):
        pass

    def exit_the_game(self, instance):
        exit()

    def create_coach(self, instance):

        self.game.add_widget(Image(allow_stretch=True, keep_ratio=False, size=(self.WindowHight, self.WindowWidth),
                                   source='Images\Coach.png'))
        dropdown = DropDown()
        countries = ["Austrian", "Belgian", "German", "French", "Dutch"]
        for country in countries:
            countries = Button(text='%r' % country, size_hint_y=None, height=30)
            countries.bind(on_release=lambda countries: dropdown.select(countries.text))
            dropdown.add_widget(countries)
        self.nationality_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.nationality_button, 'text', x))
        self.game.add_widget(self.nationality_button)

        day = DropDown()
        date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30]
        for daj in date:
            days = Button(text='%r' % daj, size_hint_y=None, height=30)
            days.bind(on_release=lambda days: day.select(days.text))
            day.add_widget(days)
        self.day_button.bind(on_release=day.open)
        day.bind(on_select=lambda instance, x: setattr(self.day_button, 'text', x))
        self.game.add_widget(self.day_button)

        curmonth = DropDown()
        month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for month_ in month:
            months = Button(text='%r' % month_, size_hint_y=None, height=30)
            months.bind(on_release=lambda months: curmonth.select(months.text))
            curmonth.add_widget(months)
        self.month_button.bind(on_release=curmonth.open)
        curmonth.bind(on_select=lambda instance, x: setattr(self.month_button, 'text', x))
        self.game.add_widget(self.month_button)

        curyear = DropDown()
        year = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001]
        for year_ in year:
            years = Button(text='%r' % year_, size_hint_y=None, height=30)
            years.bind(on_release=lambda years: curyear.select(years.text))
            curyear.add_widget(years)
        self.year_button.bind(on_release=curyear.open)
        curyear.bind(on_select=lambda instance, x: setattr(self.year_button, 'text', x))
        self.game.add_widget(self.year_button)

        save_information_button = Button(text="Save", font_size=self.Ratio * 34, on_press=self.save_coach,
                                         background_color=[1, 1, 1, 1],
                                         pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),
                                         size=(self.Ratio * 236, self.Ratio * 50))
        league_button = Button(text="League", font_size=self.Ratio * 34, on_press=self.enter_league,
                               pos=(self.Ratio * (self.WindowHight - self.Ratio * 556), self.Ratio * (self.WindowWidth - self.Ratio * 254)),
                               size=(self.Ratio * 250, self.Ratio * 48))

        self.game.add_widget(league_button)
        self.game.add_widget(save_information_button)
        self.game.add_widget(self.name)
        self.game.add_widget(self.surname)

        self.game.add_widget(
            Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * (self.WindowHight - self.Ratio * 472), self.Ratio * 0), size=(self.Ratio * 236, self.Ratio * 50)))

        return self.game

    def enter_league(self, instance):

        epl_button = Button(text="EPL", font_size=self.Ratio * 34, on_press=self.enter_team,
                            pos=(self.Ratio * (self.WindowHight - self.Ratio * 556), self.Ratio * (self.WindowWidth - self.Ratio * 254)),
                            size=(self.Ratio * 250, self.Ratio * 48))

        self.game.add_widget(epl_button)

        return self.game

    def enter_team(self, instance):

        dropdown = DropDown()
        teams = ['CHELSEA', 'ARSENAL']
        for team in teams:
            teams = Button(text='%r' % team, size_hint_y=None, height=30)
            teams.bind(on_release=lambda teams: dropdown.select(teams.text))
            dropdown.add_widget(teams)
        self.team_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.team_button, 'text', x))
        self.game.add_widget(self.team_button)
        if self.team_button.text == 'CHELSEA':
            self.main_menu_background.source = 'Images\MainMenuChelsea.jpg'
        elif self.team_button.text == 'ARSENAL':
            self.main_menu_background.source = 'Images\MainMenuArsenal.jpg'

        return self.game

    def save_coach(self, sinstance):

        continue_button = Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu,
                                 background_color=[1, 1, 1, 1],
                                 pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),
                                 size=(self.Ratio * 236, self.Ratio * 50))

        if self.name.text == "" or self.surname.text == "" or self.nationality_button.text == "" or self.day_button.text == "" or self.month_button.text == "" or self.year_button.text == "" or self.team_button == "Team":
            self.game.add_widget(Label(markup=True, color=[1, 0, 0, 1], text='enter all parameters ',
                                       pos=(self.Ratio * 300, self.Ratio * 130),
                                       size=(self.Ratio * 300, self.Ratio * 48), font_size='30sp'))
        else:
                """
            fob = open('coach.dat', 'w')
            write = fob.write(
                self.name.text + " " + self.surname.text + " " + self.day_button.text + " " + self.month_button.text + " " + self.year_button.text + " " + self.nationality_button.text + " " + self.team_button.text)
                """
                Age = 2018 - int(self.year_button.text)-1
                if int(self.month_button)>=10:
                        if int(self.day_button.text)>17 or int(self.month_button.text)>10:
                                Age = 2018-int(self.year_button.text)
                self.Manager = (self.name.text,self.surname.text,Age,self.nationality_button.text,self.enter_team.text)
                self.game.add_widget(continue_button)

                return self.game

    def main_menu(self, instance):

        self.game.add_widget(self.main_menu_background)

        mail_button = (Button(text="Mail", font_size=self.Ratio * 34, on_press=self.mail, background_color=[1, 1, 1, 1],
                              pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 195)),
                              size=(self.Ratio * 236, self.Ratio * 105)))
        finance_button = (
            Button(text="Finance", font_size=Ratio * 34, on_press=self.finance, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 300)), size=(self.Ratio * 236, self.Ratio * 105)))
        transfers_button = (
            Button(text="Transfers", font_size=self.Ratio * 34, on_press=self.transfers, background_color=[1, 1, 1, 1],
                   pos=(Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 405)), size=(self.Ratio * 236, self.Ratio * 105)))
        coach_button = (Button(text="Coach", font_size=self.Ratio * 34, on_press=self.coach, background_color=[1, 1, 1, 1],
                               pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 510)),
                               size=(self.Ratio * 236, self.Ratio * 105)))
        squad_button = (Button(text="Squad", font_size=Ratio * 34, on_press=self.squad, background_color=[1, 1, 1, 1],
                               pos=(self.Ratio * 0, Ratio * (self.WindowWidth - self.Ratio * 615)),
                               size=(self.Ratio * 236, self.Ratio * 105)))
        settings_button = (
            Button(text="Settings", font_size=Ratio * 34, on_press=self.game_settings, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 720)), size=(self.Ratio * 236, self.Ratio * 105)))

        match_button = (Button(text="Match", font_size=Ratio * 34, on_press=self.match, background_color=[1, 1, 1, 1],
                               pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),
                               size=(self.Ratio * 236, self.Ratio * 50)))
        self.game.add_widget(match_button)

        self.game.add_widget(mail_button)
        self.game.add_widget(finance_button)
        self.game.add_widget(transfers_button)
        self.game.add_widget(coach_button)
        self.game.add_widget(squad_button)
        self.game.add_widget(settings_button)
        self.game.add_widget(Button(text="Time", font_size=Ratio * 34, background_color=[1, 1, 1, 1],
                                    pos=(self.Ratio * (self.WindowHight - Ratio * 1044), self.Ratio * 0),
                                    size=(self.Ratio * 808, self.Ratio * 50)))
        self.game.add_widget(Button(background_normal='Images\Field.jpg', on_press=self.placement, pos=(
        Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                    size=(self.Ratio * 768, self.Ratio * 580)))

        return self.game

    def mail(self, instance):
        pass

    def finance(self, instance):
        pass

    def transfers(self, instance):
        pass

    def coach(self, instance):
        pass

    def squad(self, instance):
        pass

    def match(self, instance):
        Leagues = []
        LoadLeagues(Leagues)
        return Game(self.game, Leagues[0].Teams[0], Leagues[0].Teams[1])

    def placement(self, instance):
        Ratio = self.WindowHight / self.WindowDefaultHight

        placement_2_3_2_3 = (
            Button(text="2-3-2-3", font_size=self.Ratio * 34, on_press=self.placement_2_3_2_3, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 195)), size=(self.Ratio * 236, self.Ratio * 105)))
        placement_3_2_5 = (
            Button(text="3-2-5", font_size=self.Ratio * 34, on_press=self.placement_3_2_5, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 405)), size=(self.Ratio * 236, self.Ratio * 105)))
        placement_2_3_5 = (
            Button(text="2-3-5", font_size=self.Ratio * 34, on_press=self.placement_2_3_5, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * 0, self.Ratio * (self.WindowWidth - self.Ratio * 300)), size=(self.Ratio * 236, self.Ratio * 105)))

        self.game.add_widget(placement_2_3_2_3)
        self.game.add_widget(placement_2_3_5)
        self.game.add_widget(placement_3_2_5)
        self.game.add_widget(
            Button(text="Continue", font_size=self.Ratio * 34, on_press=self.main_menu, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0), size=(self.Ratio * 236, self.Ratio * 50)))
        self.game.add_widget(Button(text="Time", font_size=self.Ratio * 34, background_color=[1, 1, 1, 1],
                                    pos=(self.Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * 0),
                                    size=(self.Ratio * 808, self.Ratio * 50)))

        return self.game

    def placement_2_3_2_3(self, instance):

        self.game.add_widget(Button(background_normal='Images\placement_2_3_2_3.jpg', pos=(
        self.Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                    size=(self.Ratio * 768, self.Ratio * 580)))
        self.game.add_widget(Button(text="Save", on_press=self.save_placement_2_3_2_3, font_size=self.Ratio * 34,
                                    background_color=[1, 1, 1, 1],
                                    pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0),
                                    size=(self.Ratio * 236, self.Ratio * 50)))

        return self.game

    def save_placement_2_3_2_3(self, instance):

        pass

    def placement_2_3_5(self, instance):

        self.game.remove_widget(Button(background_normal='Images\Field.jpg', pos=(
        self.Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                       size=(self.Ratio * 768, self.Ratio * 580)))

        self.game.add_widget(Button(background_normal='Images\placement_2_3_5.jpg', pos=(
        self.Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                    size=(self.Ratio * 768, self.Ratio * 580)))
        self.game.add_widget(
            Button(text="Save", on_press=self.save_placement_2_3_5, font_size=self.Ratio * 34, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0), size=(self.Ratio * 236, self.Ratio * 50)))

        return self.game

    def save_placement_2_3_5(self, instance):

        pass

    def placement_3_2_5(self, instance):

        self.game.remove_widget(Button(background_normal='Images\Field.jpg', pos=(
        Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                       size=(self.Ratio * 768, self.Ratio * 580)))

        self.game.add_widget(Button(background_normal='Images\placement_3_2_5.jpg', pos=(
        Ratio * (self.WindowHight - self.Ratio * 1044), self.Ratio * (self.WindowWidth - self.Ratio * 670)),
                                    size=(self.Ratio * 768, self.Ratio * 580)))
        self.game.add_widget(
            Button(text="Save", on_press=self.save_placement_3_2_5, font_size=self.Ratio * 34, background_color=[1, 1, 1, 1],
                   pos=(self.Ratio * (self.WindowHight - self.Ratio * 236), self.Ratio * 0), size=(self.Ratio * 236, self.Ratio * 50)))

        return self.game

    def save_placement_3_2_5(self, instance):

        pass


class Main(App):
    def build(self):
        return GameMenu().run()


if __name__ == "__main__":
    Main().run()
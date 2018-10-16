
from random import randint as rand
from time import sleep
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label

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


def Game(Widg,Team1,Team2):
        WindowHight = 1280
        WindowWidth = 720
        WindowDefaultHight = 1280
        WindowDefaultWidth = 720
        Ratio = WindowHight/WindowDefaultHight
        
        Widg.add_widget(Image(allow_stretch=True,keep_ratio=False,size =(WindowHight,WindowWidth),source='Images\Match.jpg'))

        time = 0
        MatchTeam1=MatchTeam(Team1)
        MatchTeam2=MatchTeam(Team2)
        activeteam=MatchTeam1
        notactiveteam=MatchTeam2
        timer = 0
        additionaltime=90
        attackpointer=0

        Time =(Label(markup = True,color=[1,1,1,1],pos=(Ratio*0,Ratio*(WindowWidth-Ratio*48)),size=(Ratio*100,Ratio*48),font_size='30sp'))
        Widg.add_widget(Time)
        Name_Team =(Label(markup = True,color=[1,1,1,1],pos=(Ratio*(WindowHight-Ratio*1120),Ratio*(WindowWidth-Ratio*48)),size=(Ratio*100,Ratio*48),font_size='30sp'))
        Widg.add_widget(Name_Team)
        Activ_Team =(Label(markup = True,color=[0,1,1,1],pos=(Ratio*(WindowHight-Ratio*1240),Ratio*(WindowWidth-Ratio*100)),size=(Ratio*200,Ratio*48),font_size='30sp'))
        Widg.add_widget(Activ_Team)
        Activ_Player =(Label(markup = True,color=[0,1,1,1],pos=(Ratio*(WindowHight-Ratio*1140),Ratio*(WindowWidth-Ratio*150)),size=(Ratio*200,Ratio*48),font_size='30sp'))
        Widg.add_widget(Activ_Player)
        Stat_Match =(Button(font_size=Ratio*30,background_color=[1,1,1,1],pos=(Ratio*(WindowHight-Ratio*1040),Ratio*(WindowWidth-Ratio*500)),size=(Ratio*800,Ratio*60)))
        Widg.add_widget(Stat_Match)
        
        while timer<=180:
                time=int(timer/2)
                if time == 1 or time == 2 or time == 3 or time == 4 or time == 5 or time == 6 or time == 7 or time == 8 or time == 9:
                       Time.text=str(0)+str(time)+':'+str(0)+str(0)
                else:
                        Time.text=str(time)+':'+str(0)+str(0)
                activeteam.addProssession()
                if time == 45 or time == 90:
                        additionaltime = rand(0, 5)
                 
                if activeteam.Team.Name==Team1.Name:
                        Name_Team.text=Team1.Teg+" "+str(activeteam.Goals)+" - "+str(notactiveteam.Goals)+" "+Team2.Teg
                else:
                        Name_Team.text=Team1.Teg+" "+str(notactiveteam.Goals)+" - "+str(activeteam.Goals)+" "+Team2.Teg
                chance = rand(0,100)
                if chance <=20:
                        player = rand(1, 10)
                        activeplayer = notactiveteam.Team.StartPlayers[player]
                        while activeplayer.RedCard==1:
                                player=rand(1, 10)
                                activeplayer = notactiveteam.Team.StartPlayers[player]
                        if rand(0,150)==75:
                                notactiveteam.addRed(player)
                        elif rand(0,100)<=10:
                                notactiveteam.addYellow(player)
                        if rand(0,200)<=2:
                                activeplayer=activeteam.Team.StartPlayers[rand(1,10)]
                                for Player in activeteam.Team.ReservePlayers:
                                        if Player.Position==activeplayer.Position and Player.IsSubstitution==0:
                                                Player.IsSubstitution=1
                                                Player,activeplayer=activeplayer,Player
                                                activeteam.Substitution-=1
                                                break
                if ((time>=60 and rand(0,100)<=5) or rand(0,200<=4)) and activeteam.Substitution==0:
                        activeplayer = activeteam.Team.StartPlayers[rand(1, 10)]
                        for Player in activeteam.Team.ReservePlayers:
                                if Player.Position == activeplayer.Position:
                                        Player.IsSubstitution = 1
                                        Player, activeplayer = activeplayer, Player
                                        activeteam.Substitution -= 1
                                        break
                if attackpointer<4:
                        chance = rand(0,100)
                        activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders,10)]
                        while activeplayer.RedCard == 1:
                                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                        if chance<activeplayer.Rating:
                                Activ_Team.text='Secsessful pass by:'
                                Activ_Player.text=activeplayer.Surname+" "+activeplayer.Club
                                if activeplayer.Surname and activeplayer.Club==Team1.Name:
                                        Activ_Player.color=Team1.Color
                                else:
                                        Activ_Player.color=Team2.Color 
                                attackpointer+=1
                                activeteam.addSecsessfulPass()
                else:
                        chance = rand(0,100)
                        if chance<=50:
                                chance = rand(0, 100)
                                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                                while activeplayer.RedCard == 1:
                                        activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                                if chance < activeplayer.Rating:
                                        Activ_Team.text='Secsessful pass by:'
                                        Activ_Player.text=activeplayer.Surname+" "+activeplayer.Club
                                        if activeplayer.Surname and activeplayer.Club==Team1.Name:
                                                Activ_Player.color=Team1.Color
                                        else:
                                                Activ_Player.color=Team2.Color
                                        attackpointer += 1
                                        activeteam.addSecsessfulPass()
                                else:
                                        attackpointer=0
                                        activeteam.addPass()
                                        activeteam, notactiveteam = notactiveteam, activeteam
                        else:
                                chance = rand(0,100)
                                if chance <30:
                                        activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders,10-activeteam.Team.Strikers)]
                                        while activeplayer.RedCard == 1:
                                                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10 - activeteam.Team.Strikers)]
                                else:
                                        activeplayer = activeteam.Team.StartPlayers[rand(10 - activeteam.Team.Strikers,10)]
                                        while activeplayer.RedCard == 1:
                                                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10 - activeteam.Team.Strikers)]
                                chance=rand(0,100)
                                if chance<=activeplayer.Rating/2:
                                        activeteam.addShoot()
                                        Activ_Team.text='Missing Shoot by:'
                                        Activ_Player.text=activeplayer.Surname+" "+activeplayer.Club
                                        if activeplayer.Surname and activeplayer.Club==Team1.Name:
                                                Activ_Player.color=Team1.Color
                                        else:
                                                Activ_Player.color=Team2.Color
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0
                                elif rand(0,activeplayer.Shoot)>notactiveteam.Team.StartPlayers[0].Rating/2:
                                        activeteam.addGoal()
                                        if activeteam.Team.Name==Team1.Name:
                                                Stat_Match.text=Team1.Teg+" "+str(activeteam.Goals)+" - "+str(notactiveteam.Goals)+" "+Team2.Teg
                                        else:
                                                Stat_Match.text=Team1.Teg+" "+str(notactiveteam.Goals)+" - "+str(activeteam.Goals)+" "+Team2.Teg
                                        Activ_Team.text='Gol by:'
                                        Activ_Player.text=activeplayer.Surname+" "+activeplayer.Club
                                        if activeplayer.Surname and activeplayer.Club==Team1.Name:
                                                Activ_Player.color=Team1.Color
                                        else:
                                                Activ_Player.color=Team2.Color
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0

                                else:
                                        activeteam.addSecsessfilShoot()
                                        notactiveteam.addSave()
                                        Activ_Team.text='Save by:'
                                        Activ_Player.text=notactiveteam.Team.StartPlayers[0].Surname+" "+notactiveteam.Team.StartPlayers[0].Club
                                        if notactiveteam.Team.StartPlayers[0].Surname and notactiveteam.Team.StartPlayers[0].Club==Team1.Name:
                                                Activ_Player.color=Team1.Color
                                        else:
                                                Activ_Player.color=Team2.Color
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0
                timer+=1
                if time==additionaltime+45 or time==additionaltime+90:
                        timer-=additionaltime*2
                        additionaltime=90
                        if time==45:
                                pass
                        timer+=1
        activeteam.Prossession=int(activeteam.Prossession/(activeteam.Prossession+notactiveteam.Prossession)*100)
        notactiveteam.Prossession=100-activeteam.Prossession
        activeteam.AllPass*=2
        activeteam.SecsessfulPass*=2
        notactiveteam.AllPass*=2
        notactiveteam.SecsessfulPass*=2
        if activeteam.Goals>notactiveteam.Goals:
                activeteam.Team.Points+=3
                activeteam.Team.WinGames+=1
                notactiveteam.Team.LoseGames+=1
        elif notactiveteam.Goals>activeteam.Goals:
                notactiveteam.Team.Points+=3
                activeteam.Team.LoseGames+=1
                notactiveteam.Team.WinGames+=1
        else:
                activeteam.Team.Points+=1
                activeteam.Team.DrawGames+=1
                notactiveteam.Team.DrawGames+=1
                notactiveteam.Team.Points+=1
        activeteam.Team.Games+=1
        notactiveteam.Team.Games += 1

        return Widg

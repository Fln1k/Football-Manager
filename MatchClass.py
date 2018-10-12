<<<<<<< HEAD
from random import randint as rand
from time import sleep

class MatchTeam:
        Team=0
        AllPass = 0
        SecsessfulPass = 0
        AllShoots = 0
        SecsessfulShoots = 0
        Save = 0
        Prossession = 0
        Goals = 0
        def __init__(self,Team):
                self.Team=Team
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

def Game(Team1,Team2):
        time = 0
        MatchTeam1=MatchTeam(Team1)
        MatchTeam2=MatchTeam(Team2)
        activeteam=MatchTeam1
        notactiveteam=MatchTeam2
        changeteam=0
        action=False
        attackpointer=0
        while time<=90:
                activeteam.addProssession()
                if activeteam.Team.Name==Team1.Name:
                        print('{} {} - {} {}     {} min'.format(activeteam.Team.Name,activeteam.Goals,notactiveteam.Goals,notactiveteam.Team.Name,time))
                else:
                        print('{} {} - {} {}     {} min'.format(notactiveteam.Team.Name, notactiveteam.Goals,activeteam.Goals, activeteam.Team.Name, time))
                if attackpointer<4:
                        chance = rand(0,100)
                        activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders,10)]
                        if chance<activeplayer.Rating:
                                print('secsessful pass by {} {}'.format(activeplayer.Surname,activeplayer.Club))
                                attackpointer+=1
                                activeteam.addSecsessfulPass()
                        else:
                                attackpointer=0
                                activeteam.addPass()
                                activeteam, notactiveteam = notactiveteam, activeteam
                else:
                        chance = rand(0,100)
                        if chance<=50:
                                chance = rand(0, 100)
                                activeplayer = activeteam.Team.StartPlayers[rand(activeteam.Team.Defenders, 10)]
                                if chance < activeplayer.Rating:
                                        print('secsessful pass by {} {}'.format(activeplayer.Surname,activeplayer.Club))
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
                                else:
                                        activeplayer = activeteam.Team.StartPlayers[rand(10 - activeteam.Team.Strikers,10)]
                                if chance<=activeplayer.Rating/2:
                                        activeteam.addShoot()
                                        print('Missing Shoot by {} {}'.format(activeplayer.Surname,activeplayer.Club))
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0
                                elif rand(0,activeplayer.Shoot)>notactiveteam.Team.StartPlayers[0].Rating/2:
                                        activeteam.addGoal()
                                        print('GGGGGGGGOOOOOOOOOOOLLLLLLLLLL by {} {}'.format(activeplayer.Surname,activeplayer.Club))
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0

                                else:
                                        activeteam.addShoot()
                                        notactiveteam.addSave()
                                        print('SSSSSSSSAAAAAAAAVVVVVVEEEEEE by {} {}'.format(notactiveteam.Team.StartPlayers[0].Surname,notactiveteam.Team.StartPlayers[0].Club))
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0
                time+=1
                sleep(1)
=======
import random
from time import sleep

class Statistic:
        Shoots=0
        Save=0
        Prossession=0
        Goals=0

def ShowStatistic(team1,team2,name1,name2,alltime):
        team1.Prossession,team2.Prossession=int((team1.Prossession/alltime)*100),int((team2.Prossession/alltime)*100)              
        print('{} {} - {} {}\n{}   Shoots   {}\n{}   Saves   {}\n{}% Prossession {}%'.format(name1,name2,team1.Goals,team2.Goals,team1.Shoots,team2.Shoots,team1.Save,team2.Save,team1.Prossession,team2.Prossession))
def Game(Team1,Team2):
        team1 = []
        team2 = []
        team1.append(Statistic)
        team1.append(Team1)
        team2.append(Statistic)
        team2.append(Team2)
        print('\n'*100)
        time=0
        Action=False
        pointer=1
        team=1
        alltime=90
        addtime=0
        while time<=90:
                if time==45 or time == 90:
                        addtime=random.randint(0,5)
                        alltime+=addtime
                if time==45+addtime or time == 90+addtime:
                        time-=addtime
                        addtime =90
                        if time==45:
                                print("Half Time")
                                i=input()
                print('{} minute'.format(time))
                print('{} {} - {} {}'.format(team1[1].Name,team1[0].Goals,team2[0].Goals,team2[1].Name))
                if team%2!=0:
                        activeteam=team1
                        notactiveteam=team2
                        team1[0].Prossession+=1
                if team%2==0:
                        activeteam=team2
                        notactiveteam=team1
                        team2[0].Prossession+=1
                if pointer==1:
                        Action=True
                if Action==False:
                        chance = random.randint(0,100)
                        if chance>=50:
                                Action=True
                else:
                        if pointer<4:
                                chance=random.randint(0,100)
                                player=random.randint(2,10)
                                if chance<=activeteam[1].StartPlayers[player].Pass:
                                        print("Secsessful pass by")
                                        print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                        
                                else:
                                        Action=False
                                        team+=1
                                        print("Loosing Ball by ")
                                        print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                pointer+=1
                        else:
                                chance=random.randint(0,100)
                                if chance>=50 and chance <55:
                                        print("---free kick---")
                                        chance = random.randint(0,100)
                                        if chance<=10:
                                                 print("GGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOLLLLLLLLLLLL")
                                                 print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                                 if team%2==0:
                                                         team1[0].Goals+=1
                                                 else:
                                                         team2[0].Goals+=1
                                                 Action=False
                                                 team += 1
                                        else:
                                                team+=1
                                                Action=False
                                elif chance>=55 and chance <60:
                                        print("---PENALTY---")
                                        chance=random.randint(0,100)
                                        player=random.randint(5,10)
                                        if team%2==0:
                                                team1[0].Shoots+=1
                                        else:
                                                team2[0].Shoots+=1
                                        if chance<=activeteam[1].StartPlayers[player].Shoot-notactiveteam[1].StartPlayers[0].Rating/2:
                                                print("GGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOLLLLLLLLLLLL")
                                                print("{} {}".format(activeteam[player][1].StartPlayers.Surname,activeteam[1].StartPlayers[player].Club))
                                                if team%2==0:
                                                        team1[0].Goals+=1
                                                else:
                                                        team2[0].Goals+=1
                                                Action=False
                                                team+=1
                                        else:
                                                print("SSSSSSSAAAAAAAAVVVVVVVVVVEEEEEEEEEEE")
                                                print("{} {}".format(notactiveteam[1].StartPlayers[0].Surname,notactiveteam[1].StartPlayers[1].Club))
                                                if team%2==0:
                                                        team2[0].Save+=1
                                                else:
                                                        team1[0].Save+=1
                                                team+=1
                                                Action=False
                                        pointer = 0
                                elif chance<50:
                                        chance=random.randint(0,100)
                                        player=random.randint(2,11)
                                        if chance<=activeteam[1].StartPlayers[player].Pass:
                                                print("Secsessful pass by")
                                                print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                                        
                                        else:
                                                Action=False
                                                team+=1
                                                print("Loosing Ball by ")
                                                print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                else:
                                        print("Shoot")
                                        chance=random.randint(0,100)
                                        player=random.randint(5,10)
                                        if team%2==0:
                                                team1[0].Shoots+=1
                                        else:
                                                team2[0].Shoots+=1
                                        if chance<=activeteam[1].StartPlayers[player].Shoot-notactiveteam[1].StartPlayers[0].Rating/2:
                                                print("GGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOLLLLLLLLLLLL")
                                                print("{} {}".format(activeteam[1].StartPlayers[player].Surname,activeteam[1].StartPlayers[player].Club))
                                                if team%2==0:
                                                        team1[0].Goals+=1
                                                else:
                                                        team2[0].Goals+=1
                                                Action=False
                                                team+=1
                                        else:
                                                print("SSSSSSSAAAAAAAAVVVVVVVVVVEEEEEEEEEEE")
                                                print("{} {}".format(notactiveteam[1].StartPlayers[0].Surname,notactiveteam[1].StartPlayers[1].Club))
                                                if team%2==0:
                                                        team2[0].Save+=1
                                                else:
                                                        team1[0].Save+=1
                                                team+=1
                                                Action=False
                                        pointer = 0
                if time==90:
                        ShowStatistic(team1[0],team2[0],team1[1].Name,team2[1].Name,alltime)
                sleep(1)
                time+=1
>>>>>>> 6cd63807048648f011132d6b3f30710214940d5f

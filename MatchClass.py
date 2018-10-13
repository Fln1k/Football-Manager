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

def Show(team1,team2):
        print('{} {}\n{} Goals {}\n{} Total Shoots {}\n{} Shoots on Target {}\n{} Pass compleated {}\n{}% Proccesion {}%'.format(team1.Team.Name,team2.Team.Name,team1.Goals,team2.Goals,team1.AllShoots,team2.AllShoots,team1.SecsessfulShoots,team2.SecsessfulShoots,team1.SecsessfulPass,team2.SecsessfulPass,team1.Prossession,team2.Prossession))

def Game(Team1,Team2):
        timer = 0
        MatchTeam1=MatchTeam(Team1)
        MatchTeam2=MatchTeam(Team2)
        activeteam=MatchTeam1
        notactiveteam=MatchTeam2
        changeteam=0
        action=False
        additionaltime=90
        attackpointer=0
        while timer<=180:
                time=int(timer/2)
                activeteam.addProssession()
                if activeteam.Team.Name==Team1.Name:
                        print('{} {} - {} {}     {} min'.format(activeteam.Team.Name,activeteam.Goals,notactiveteam.Goals,notactiveteam.Team.Name,time))
                else:
                        print('{} {} - {} {}     {} min'.format(notactiveteam.Team.Name, notactiveteam.Goals,activeteam.Goals, activeteam.Team.Name, time))
                if time == 45 or time == 90:
                        additionaltime = rand(0, 5)
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
                                chance=rand(0,100)
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
                                        activeteam.addSecsessfilShoot()
                                        notactiveteam.addSave()
                                        print('SSSSSSSSAAAAAAAAVVVVVVEEEEEE by {} {}'.format(notactiveteam.Team.StartPlayers[0].Surname,notactiveteam.Team.StartPlayers[0].Club))
                                        activeteam, notactiveteam = notactiveteam, activeteam
                                        attackpointer=0
                timer+=1
                sleep(0)
                if time==additionaltime+45 or time==additionaltime+90:
                        timer-=additionaltime*2
                        additionaltime=90
                        if time==45:
                                print('------HALF TIME------')
                                sleep(5)
                        timer+=1
        activeteam.Prossession=int(activeteam.Prossession/(activeteam.Prossession+notactiveteam.Prossession)*100)
        notactiveteam.Prossession=100-activeteam.Prossession
        activeteam.AllPass*=2
        activeteam.SecsessfulPass*=2
        notactiveteam.AllPass*=2
        notactiveteam.SecsessfulPass*=2
        if activeteam.Team.Name==Team1.Name:
                Show(activeteam,notactiveteam)
        else:
                Show(notactiveteam,activeteam)

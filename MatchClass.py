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

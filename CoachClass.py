class CoachPool:
    _Coaches=[]
    def __init__(self,Coaches):
        self.Coaches=Coaches
    def RequestCoach(self,ClubName):
        for Coach in self.Coaches:
            if Coach.Club==ClubName:
                return Coach

class Coach:
    _Name=''
    _Surname=''
    _Age=0
    _Nationality=''
    _Club=''
    _AttackTactic=0
    _DefendTactic=0
    _Style=''
    def __init__(self,information):
        self.Name=information[0]
        self.Club=information[4]
        self.Surname=information[1]
        self.Nationality=information[2]
        self.Age=information[3]
        self.AttackTactic=int(information[5])
        self.DefendTactic=int(information[6])
        self.Style=information[7]
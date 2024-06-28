class Person:
    def __init__(self, fam, name, otchestvo, number, days, moneys):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.number = number
        self.days = days
        self.moneys = moneys

   
    def getPerson_forTable(self):
        w = []
        w.append(self.fam)
        w.append(self.name)
        w.append(self.otchestvo)
        w.append(self.number)
        w.append(self.days)
        w.append(self.moneys)
        return w

    def equval_Person(self,B):
    
        return self.fam == B.fam and \
               self.name == B.name and \
               self.otchestvo == B.otchestvo and \
               self.number == B.number and \
               self.days == B.days and \
               self.moneys == B.moneys
class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in range(len(self.A)):  
            if x in self.A: 
                s += f'Person {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s

    def appendPerson(self,List):
        new_Person = Person(*List)
        self.A[self.count] = new_Person

        self.count += 1

    def editPerson(self,x,List):

        P = Person(*List)
        self.A[x] = P

    def Str_Person(self,line):
        if line[-1] == '\n' : line = line[:-1] 
        parts = line.strip().split("&")

        return Person(*parts)


    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
 
                self.A[x] = self.Str_Person(line)

                x += 1
                self.count += 1

    def find_keyPerson(self, List):

        P = Person(*List)
        for x in self.A :
            
            if self.A[x].equval_Person(P) :
               return x

        return -1    



    def delPerson(self, List):
        P = Person(*List)
        for x in self.A :
            if self.A[x].equval_Person(P):
                del self.A[x] 
                self.count = self.count- 1
    
                break


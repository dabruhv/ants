# ants
#ant farm base code!
#written by Dr. Mo, Jan 22

import random

colony=[] #list to hold all the ants

#parent class---------------------------------------
class ant:
    def __init__(self):
        self.age = 0
        self.food = 10
    def eat(self):
        self.food+=2
    def __del__(self): #destructor
        print("ant killed.")
    def food(self):
        self.food+=5

    def update(self):
        self.food-=1
        self.age+=1
        

#child class--------------------------
class worker(ant):
    def __init__(self):
        self.name = "worker"
        ant.__init__(self)
    
    def printInfo(self):
        print("I am a worker and I am ", self.age, " days old. My food level is ", self.food)



class scavenger(ant):
    def __init__(self):
        self.name = "scavenger"
        ant.__init__(self)
    
    def printInfo(self):
        print("I am a scavenger and I am ", self.age, " days old. My food level is ", self.food)

        
        print("scavenger has found food!")
        
        
#child class--------------------------
class larva(ant):
    def __init__(self):
        self.name = "larva"
        ant.__init__(self)
    def printInfo(self):
        print("I am a larva and I am ", self.age, " days old. My food level is ", self.food)
    def metamorphasis(age):
        if age == 2:
            job = random.randrange(1,50)
            if job == 50:
                #makes them a queen
#child class--------------------------
class queen(ant):
    def __init__(self):
        self.name = "queen"
        ant.__init__(self)
        
    def printInfo(self):
        print("I am a queen and I am ", self.age, " days old. My food level is ", self.food)
        
    def egg(self):
        print("queen has laid an egg!")
        BabyLarva = larva()
        colony.append(BabyLarva)
        
#start of "main"########################################
q1 = queen()
colony.append(q1)
w1 = worker()
colony.append(w1)
w2 = worker()
colony.append(w2)
l1 = larva()
colony.append(l1)
s1 = scavenger()
colony.append(s1)

#game loop

doExit = False
hasScav = True
while doExit == False:


#print info for each ant in colony
    i = 0
    while i != len(colony):
        colony[i].printInfo()
        colony[i].update()
        if hasScav:
            colony[i].eat()
        if colony[i].name == "queen":
            colony[i].egg()

        if colony[i].age >5:
            print("A ", colony[i].name, " has died.")
            if colony[i].name == "scavenger":
                hasScav = False
            del colony[i]
            i-=1

        i += 1    
    
    
    
    print("------------")

    userInput = input("press any key to continue, q to quit")
    if userInput == "q":
        doExit = True

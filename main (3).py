import random
import time
import replit

s = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    OKTEST = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Dog:
    def __init__(self, myName, myBreed):
        self.alive = True
        self.name = input("Enter your dog's name ")
        self.breed = input("Enter your dog's breed Shepard|Chihuahua ")        
        self.age = 0.0
        self.health = 100
        self.hunger = 100
        self.hydration = 100
        self.enjoyment = 0
        self.depression = 0
        self.fatigue = 0
        self.play = 1
        self.agepeak = random.randint(4, 25)
        self.switch = False
        if self.age < float(1.2):  
          self.hunger = 15
          self.hydration = 20
          self.health = 25
    def getName(self):  
      return self.__name
    def getAge(self): 
      return self.__age
    def getBreed(self): 
      return self.__breed
    
    def bark(self, n):
        for i in range(n):

            if self.breed == "Shepard":
                print(""" 
     |\_/|                  
     | @ @   ᴮ ᴬ ᴿ ᴷ 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|
      """)
            if self.breed == "Chihuahua":
                print(""" 
                /)-_-(\      
                 (o o)     ᴮ ᴬ ᴿ ᴷ
         .-----__/\o/     
        /  __      /         
    \__/\ /  \_\ |/             
         \      ||             
         //     ||          
         |\     |\ 
        """)

    def sleep(self, x):
        self.health += 15
        if self.health > 100:
            self.health = 100
        for x_s in range(0, 12):
            time.sleep(0.5)
            print(" ")
        self.bark(1)
    def evolve(self):
      if self.age == float(0.2):
        for us in range(0,len(dogs)): 
          if dogs[us].name == self.name:
            print(bcolors.OKGREEN + "YOUR PUPPY HAS GROWN UP" + bcolors.ENDC)  
            dogs.append(Dog(dogs[us].name,dogs[us].breed))
            dogs.remove(dogs[us])
            for lo in range(0,len(dogs)): 
              if dogs[lo].name == dogs[us].name: 
                dogs[lo].age = 1.2
    def dogisalive(self):
        while self.alive != False:
            if self.hunger < 0:
                self.hunger = 0
            if self.hydration < 0:
                self.hydration = 0
            self.age += 0.1
            if self.age >= self.agepeak:
                self.health = -15
            if self.age <= 1.2:  
              print("""
           __
      (___()'`;
      /,    /`
      \ "-- \               
              """)
              print(bcolors.HEADER + self.name + bcolors.ENDC)              
            else:  
              if self.breed == "Shepard":
                  print("""
       |\_/|                  
       | @ @ 
       |   <>              _  
       |  _/\------____   | |
       |               `--' |   
   ____|_       ___|   |___.' 
  /_/_____/____/_______|
        """)
                  print(bcolors.HEADER + self.name + bcolors.ENDC)

              if self.breed == "Chihuahua":
                  print("""
            /)-_-(\      
             (o o)       
     .-----__/\o/     
    /  __      /         
\__/\ /  \_\ |/             
     \      ||             
     //     ||          
     |\     |\               
        """)
                  print(bcolors.HEADER + self.name + bcolors.ENDC)
            print("Age:", round(self.age, 1))
            print(bcolors.WARNING + "Food:", str(self.hunger) + bcolors.ENDC)
            print(bcolors.OKCYAN + "Hydration:",
                  str(self.hydration) + bcolors.ENDC)
            print(bcolors.OKGREEN + "Health:", str(self.health) + bcolors.ENDC)
            print(bcolors.FAIL + "Depression:",
                  str(self.depression) + bcolors.ENDC)

            this = input(bcolors.BOLD + """What now ? 
| Eat | Drink | Sleep | Bark | Play | New Dog | Select Dog | Show Dogs |
""" + bcolors.ENDC)

            if this == "Eat":
                self.hunger += 35
                self.fatigue -= 5
            if this == "Drink":
                self.hydration += 45
                self.fatigue -= 10
            if this == "Sleep":
                self.sleep(15)
                self.fatigue -= 75
            if this == "Bark":
                self.hunger -= 5
                self.hydration -= 15
                self.bark(1)
                self.enjoyment += 5
                self.depression -= 15
                self.fatigue += 50
            if this == "Play":
                self.hunger -= 30
                self.hydration -= 45
                self.enjoyment += 35
                self.depression -= 65
                self.play += 1
                self.fatigue += 75
            if self.fatigue >= 100: 
              self.enjoyment -= 35
              self.health -= 5
              self.hunger -= 10
              self.hydration -= 15
            if this == "Animal Abuse":
                prison = random.randint(0, 100)
                if prison >= 75:
                    self.health = 0
                else:
                    self.health -= 75
                    self.depression = 100
                    self.enjoyment = 0
            if this == "New Dog":
                print("Enter your new dog's details")
                newName = 0
                newBreed = 0
                dogs.append(Puppy(newName, newBreed))
            if this == "Select Dog":
                for i in range(len(dogs)):
                    print(bcolors.HEADER + dogs[i].name + bcolors.ENDC)
                chooseDog = input(bcolors.BOLD + "Choose a Dog " +
                                  bcolors.ENDC)
                for uj in range(len(dogs)):
                    if chooseDog == dogs[uj].name:
                        print("Dog named", chooseDog, "has been chosen.")
                        s = uj
                        time.sleep(3)
                        replit.clear()
                        print(bcolors.FAIL + "!  ATTENTION ! " + bcolors.ENDC)
                        print(
                            """ REMEMBER THAT YOUR OTHER DOGS ARE STILL ALIVE AND NEED ATTENTION 
 EVERY TURN YOU PLAY WILL BE COUNTED AS IDLE FOR OTHER DOGS""")
                        time.sleep(9)
                        replit.clear()
                        dogs[s].dogisalive()
                        if dogs[s].alive == False:
                            dogs.remove(dogs[s])
            if this == "Show Dogs":
                for d in range(0, len(dogs)):
                    print(dogs[d].name, "\n", bcolors.WARNING + "Hunger:",
                          str(dogs[d].hunger) + bcolors.ENDC,
                          bcolors.OKCYAN + "Thirst",
                          str(dogs[d].hydration) + bcolors.ENDC,
                          bcolors.OKGREEN + "Health:",
                          str(dogs[d].health) + bcolors.ENDC)
            if self.play <= (self.enjoyment / self.play * 15):
                self.enjoyment -= 15
                self.depression += 15
            if self.fatigue >= 65:  
              print(bcolors.UNDERLINE + self.name, "feels tired" + bcolors.ENDC)
              self.depression += 15
            if self.depression >= 50:
                print(bcolors.OKTEST + self.name, "feels sad" + bcolors.ENDC)
            if self.depression <= 15:
                print(bcolors.OKBLUE + self.name, "feels happy" + bcolors.ENDC)
            if self.depression >= 100:
                self.depression = 100
                self.health -= 5
            if self.depression <= 0:
                self.depression = 0
            if self.hydration < 15 or self.hunger < 10:
                print(bcolors.UNDERLINE + self.name,
                      "Needs some attention" + bcolors.ENDC)
                if self.hydration <= 0 or self.hunger <= 0:
                    self.health -= 15
            if self.age >= self.agepeak / 2:
                self.illness = random.randint(0, 100)
                if self.illness >= 85:
                    print(self.name, "got ill.")
                    self.health -= 45
                    if self.health == 0:
                        self.health = -5
            if self.health <= 0:
                self.alive = False
                print(self.name, "Died at the age of", round(self.age, 1))
                print("""
        
       _____      
     //  +  \     
    ||  RIP  |    
    ||       |    
    ||       |    
   \||/\/\//\|/           
        
        """)
            self.fatigue -= 15
            self.hunger -= 5
            self.hydration -= 10
            if self.fatigue < 0:  
              self.fatigue = 0
            if self.fatigue >= 100: 
              self.fatigue = 100
            if self.health >= 100:
                self.health = 100
            if self.hunger >= 100 or self.hydration >= 100:
                self.health -= 5    
            self.evolve()      
            time.sleep(3)
            replit.clear()

class Puppy(Dog): 
  def __innit_(self,myName,myBreed,):  
    super().__innit__(myName,myBreed)
    self.name = myName
    self.breed = myBreed

  def bark(self,i): 
    for ki in range(0,i):
      print("""
           __
      (___()'`;  ʏᴀᴘ
      /,    /`
      \ "-- \      
    """) 

dogs = [Puppy(' ', " ")]

if dogs[s].alive == True:
    dogs[s].dogisalive()
else:
  s += 1
class account:
    def __init__(self, name, acct, bal, mobb, odl):
        self.debt = 0
        self.name = name
        self.acct = "Basic bank account"
        self.bal = 5000
        self.mobb = mobb
        if self.acct == "Basic bank account": 
            self.odl = self.bal / 2
        elif self.acct == "Children's bank account":  
            self.odl = 0
        elif self.acct == "Student account":  
            self.odl = self.bal * 0.75
        elif self.acct == "Current account":  
            self.odl = self.bal
        else: 
            self.odl= self.bal * 0.5
    def getname(self):
        return self.name

    def getbalance(self):
        return self.bal

    def transaction(self):
        print("Your balance",self.bal)
        name = input("Enter the name of the person you want to transfer money to ")
        amount = int(input("Enter the amount "))
        if amount > self.bal + self.odl:
            print("Transaction can not be completed Insufficent Funds")
        else:
            found = False
            for x in range(0, len(acc)):
                if acc[x].getname() == name:
                    acc[x].bal += amount
                    self.bal -= amount
                    found = True
                    print("Transaction completed")
            if found == False: 
                print("Person not found")
            else:
                if self.bal < 0:
                      this = self.bal
                      self.bal = 0
                      self.odl += this
                      this = this * -1
                      print("New overdraft limit is", int(self.odl))
                      print("You are in debt for",this)
                      self.debt = this
                print("New balance = ", self.bal)

    def enablemobb(self):
        self.mobb = True
        print("Mobile banking is now enabled")

    def disablemobb(self):  
        self.mobb = False
        print("Mobile banking is now disabled")

    def changeaccounttype(self):
        change = int(input("""
        1. Children’s bank account
        2. Joint bank account
        3. Student account
        4. Packaged bank account
        5. Current account
        6. Basic bank account
        """))
        if change == 1: 
          self.acct = "Children's bank account"
          self.odl = 0
        elif change == 2: 
          self.acct = "Joint bank account"
          self.odl = self.bal / 2
        elif change == 3:
          self.acct = "Student account"
          self.odl = self.bal * 0.75
        elif change == 4: 
          self.acct = "Packaged bank account"
          self.odl = self.odl / 2
        elif change == 5: 
          self.acct = "Current account"
          self.odl = self.bal
        elif change == 6: 
          self.acct = "Basic bank account"
          self.odl = self.bal / 2          
        else: 
          print("Invalid option")

    def menu(self): 
      print(" ")
      print("Your balance:",self.bal)
      print("Your overdraft limit is:",int(self.odl))
      if self.debt > 0: 
        print("You are in debt for",self.debt)
      menu = input("""
      Please choose an option 
      1.Transfer Money
      2.Change account type
      3.Mobile banking   
      """)

      if menu == "1": 
        self.transaction()
      elif menu == "2": 
        self.changeaccounttype()
      elif menu == "3": 
        if self.mobb == False:  
          self.enablemobb()
        else: 
          self.disablemobb()          
      else: 
        self.menu()
acc = [
    account("Ege", "", 5000, True, 5000),
    account("Test", "", 5000, True, 5000)
]
this = True
while this == True:
  acc[0].menu()
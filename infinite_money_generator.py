import os

class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
    def deposit(self):  # infinite money generator
    	os.system("clear")
    	try:
	        print("How much do you want to deposit?\n")
	        amount = int(input())
	        self.money += amount
	        print(f"You have deposited ${amount}")
    	except ValueError:
        	print("Enter a valid number!")

	    	
    def withdraw(self):
        os.system('clear')
        try:
	        print("How much do you want to withdraw?\n")
	        amount = int(input())
	        if self.money > amount:
	            self.money -= amount
	            print(f"You has deposited ${amount}")
	        elif self.money < amount:
	            print("You don't have enough money")
        except ValueError:
        	print("Enter a valid number!")
        	
        	
        
    def transfer(self):
        os.system('clear')
        try:
            print("Who do you want to transfer?\n")
            user = input()
            print("How much do you want to transfer?\n")
            amount = int(input())
            if self.money > amount:
                self.money -= amount
                print(f"You has transferred ${amount} to {user}")
                return
            elif self.money < amount:
                print("You don't have enough money")
                
        except ValueError:
        	print("Enter a valid number!")
        
    def balance(self):
        os.system('clear')
        balance = self.money
        print(f"You have ${balance}")
    
    def start(self):
        while True:
            print("""
            Welcome to bank, what do you want to do?
            [1]Deposit
            [2]Withdraw
            [3]Transfer
            [4]Check Balance
            \n
            """)
            choice = input()
            if choice == "1":
                self.deposit()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.transfer()
            elif choice == "4":
                self.balance()
        
        
account = Bank("Lua", 0)

account.start()

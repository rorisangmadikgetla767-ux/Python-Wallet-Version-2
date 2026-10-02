from Classes import Account, Transaction
Users = []
Transactions = []
from os import path

def Add_Account():
    Id = input("Enter your walletID: ")
    Name = input("Enter your name: ")
    Surname = input("Enter your Surname: ")
    StartingBalance = float(input("Enter your starting balance: "))
    IntRate = float(input("Enter the interest rate applied"))
    
    Details = Account(Id, Name, Surname, StartingBalance, IntRate)
    Users.append(Details)
    
    # first I wrote file.write(",".join(str(d) for d in Details) "\n")
    # But I changed it to the line in line 18, because python could not iterate through my Account object
    
    with open("Accounts.txt", "a") as file:
        line = ",".join([str(Details.WalletID), str(Details.OwnersName), str(Details.OwnerSurname), str(Details._Balance), str(Details.interestRate)])
        file.write(line + "\n")
        
        
    
def Display_Info():
    # Created a search variable
    # Then I opened the .txt file, in read mode
    # I looped through the file
    #I called the varible to see if it matches the values in the .txt file
    
    search = input("Search your name to view the account..: ")
    with open("Accounts.txt", "r")as file:
        for line in file:
            if search in line:
                print(line)
            else:
                print("Value not found")
                
def deposit():
    Amount = float(input("How much do you want to deposit ?"))
    with open("Accounts.txt", "r") as file:
        line = file.readline()
        data = line.strip().split(",")
        balance = float(data[3])
        Deposit = Amount
        balance = balance + Amount
        data[3] = str(balance)
        
        with open("Account.txts", "w") as file:
            file.write(", ".join(data))
        
def withdraw():
    Amount = float(input("How much do you want to withdraw?"))
    with open("Accounts.txt", "r") as file:
        line = file.readline()
        data = line.strip().split(",")
        balance = float(data[3])
        withdrawal = Amount
        balance = balance - Amount
        data[3] = str(balance)
        
        with open("Accounts.txt", "w") as file:
            file.write(", ".join(data))
        
    
    
    
    
while True:
    print("===== DIGITAL WALLET =====\n"+
          "1. Create Wallet \n"+
          "2. View Wallet \n"+
          "3. Deposit\n"+
          "4. Withdraw \n"+
          "5. Transfer \n"+ 
          "7. Exit \n")
    print("===== Pula Bakwena ! =====")
    
    mainMenu = int(input("Enter a number: "))
    if mainMenu == 1:
        Add_Account()
    elif mainMenu == 2:
        Display_Info()
    elif mainMenu == 3:
        deposit()
    elif mainMenu == 4:
        withdraw()
    elif mainMenu == 5:
        deposit()
    elif mainMenu == 6:
        pass
    else:
        print("Closing the program..")
        exit
        
    
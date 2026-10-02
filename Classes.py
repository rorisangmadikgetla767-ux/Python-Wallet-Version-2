class Account:
    def __init__(self, WalletID: int, OwnersName, OwnersSurname,Balance: float, interestRate: float ):
        self.WalletID =WalletID
        self.OwnersName = OwnersName
        self.OwnerSurname = OwnersSurname
        self._Balance = Balance
        self.interestRate = interestRate
        
    def calculateInterestRate(self):
        if self.Balance < 1000:
            self.interestRate = 1.0
        elif self.Balance < 5000:
            self.interestRate = 1.5
        else:
            self.interestRate = 2.0
        
class Transaction:
    def __init__(self, TransactionType: str, Amount: float):
        self.TransactionType = TransactionType
        self.Amount = Amount
        
        
    def deposit(self, balance):
        self.Amount = float(input("How much do you want to deposit: "))
        if self.Amount <0:
            raise ValueError("Sorry you cannot deposit a negative amount..")
        else:
            balance += self.Amount
        History = []
        History.append(self.Amount)
   
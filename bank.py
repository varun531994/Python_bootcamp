#Create Bank Account that has two attributes:
#1.Owner
#2.Balance
  
#and two methods:
#1.deposit
#2.withdraw

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: Rs.{self.balance}'
        
    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


owner = input("Enter owners name:")
balance = int(input("Enter account balance:"))
acct1 = Account(owner,balance)

print(acct1)

deposit = int(input("Enter amount to deposit:"))

print(acct1.deposit(deposit))
print(acct1)

withdraw = int(input("Enter amount to withdraw:"))

print(acct1.withdraw(withdraw))
print(acct1)


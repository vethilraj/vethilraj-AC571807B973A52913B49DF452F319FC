class BankAccount():
  def __init__(self,account_number,account_holder_name,balance=0.0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=balance
    
  def deposit(self,amount):
    if (amount>0):
      self.__account_balance+=amount
      print("Deposit ₹",amount,"New Balance: ₹",self.__account_balance)
      
    else:
      print("Invalid deposit amount. Please deposit a positive amount.")
      
  def withdraw(self,amount):
     if (amount>0 and amount<=self.__account_balance):
       self.__account_balance-=amount
       print("Withdraw ₹",amount,"New balance: ₹",self.__account_balance)     
     else:
       print("Invalid withdraw amount or insufficient balance")
       
  def display_balance(self):
     print("Account balance for {} (Account {}): ₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
     
     
acc=BankAccount("123456789","hari",5000)
acc.display_balance()
acc.deposit(500.0)
acc.withdraw(200.0)
acc.withdraw(20000.0)
acc.display_balance()
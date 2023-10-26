class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited ${amount:.2f} into account {self.__account_number}")
      else:
          print("Invalid deposit amount. Please deposit a positive amount.")

  def withdraw(self, amount):
      if amount > 0:
          if self.__account_balance >= amount:
              self.__account_balance -= amount
              print(f"Withdrew ${amount:.2f} from account {self.__account_number}")
          else:
              print("Insufficient balance. Cannot withdraw.")
      else:
          print("Invalid withdrawal amount. Please withdraw a positive amount.")

  def display_balance(self):
      print(f"Account {self.__account_number} balance: ${self.__account_balance:.2f}")


# Testing the BankAccount class
if _name_ == "__main__":
  # Create a BankAccount instance
  account1 = BankAccount("123456", "John Doe", 1000.0)

  # Deposit money
  account1.deposit(500.0)

  # Withdraw money
  account1.withdraw(200.0)

  # Display balance
  account1.display_balance()
23
Reply


Answers dotcom
·

16 replies
@satheeshsatheesh5724
@satheeshsatheesh5724
1 month ago
Unit 2 challenge 2
Question 
Implement a class called Player that represents a cricket player. The Player class should have a method called play() which prints "The player is playing cricket. Derive two classes, Batsman and Bowler, from the Player class. Override the play() method in each derived class to print "The batsman is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the Batsman and Bowler classes and call the play() method for each object.
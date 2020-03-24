#create the account class
class Account():
    def __init__(self,acc_nmbr,balance=0):
        self.acc_nmbr = acc_nmbr
        self.balance = balance

    def __str__(self):
        return f'${self.balance:.2f}'

    def credit(self,value):
        self.balance += value

    def debit(self,value):
        self.balance -= value

    def report_balance(self):
        print(f"The current account balance is: {Account.__str__(self)}")

#create the various account types: checking, savings and business
class Checking(Account):
    def __init__(self,acc_nmbr,balance=0):
        super().__init__(acc_nmbr,balance)

    def __str__(self):
        return f"Checking account #{self.acc_nmbr}\nBalance: {Account.__str__(self)}"

class Savings(Account):
    def __init__(self,acc_nmbr,balance=0):
        super().__init__(acc_nmbr,balance)

    def __str__(self):
        return f"Savings account #{self.acc_nmbr}\nBalance: {Account.__str__(self)}"

class Business(Account):
    def __init__(self,acc_nmbr,balance=0):
        super().__init__(acc_nmbr,balance)

    def __str__(self):
        return f"Business account #{self.acc_nmbr}\nBalance: {Account.__str__(self)}"

#create a customer class
class Customer():
    def __init__(self,name,PIN):
        self.name = name
        self.PIN = PIN

        #a dictionary which holds the various accounts
        self.accts = {'C':[],'S':[],'B':[]}

    def __str__(self):
        return self.name

    #functions to open accounts
    def open_checking(self,acc_nmbr,balance):
        self.accts['C'].append(Checking(acc_nmbr,balance))

    def open_savings(self,acc_nmbr,balance):
        self.accts['S'].append(Savings(acc_nmbr,balance))

    def open_business(self,acc_nmbr_balance):
        self.accts['B'].append(Business(acc_nmbr,balance))

    #function to get balance
    def get_total_balance(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f"Combined total balance: ${total:.2f}")

#function to make deposit
def make_deposit(cust,acct_type,acct_num,dept_amt):
    for acct in cust.accts[acct_type]:
        if acct.acc_nmbr == acct_num:
            acct.credit(dept_amt)
        if acct.acc_nmbr != acct_num:
            print("We were unable to complete the requested deposit. Please confirm the account number and type.")
#function to make withdrawal
def make_withdraw(cust,acct_type,acct_num,wit_amt):
    for acct in cust.accts[acct_type]:
        if acct.acc_nmbr == acct_num:
            acct.debit(wit_amt)
        if acct.acc_nmbr != acct_num:
            print("We were unable to complete the requested withdrawal. Please confirm the account number and type.")

#put everything together
import random
from IPython.display import clear_output
mode= 0
in_use = True

error_message = "Sorry, please try again\n"

print("Welcome to Whitaker Banking!\n")
cust_name = input("Please enter your name to begin:\n")
clear_output()
the_customer = Customer(cust_name,1234)
print(f"Welcome {cust_name}!\n")

while in_use == True:

    while mode == 0:
        print("What would you like to do now?")
        print("(1) Open an account.")
        print("(2) Make a deposit.")
        print("(3) Make a withdrawal.")
        print("(4) Check account balance.")
        print("(5) Quit.")
        try:
            choice = int(input("Enter 1, 2, 3, 4 or 5 to choose.\n"))
        except ValueError:
            print("Sorry, please enter one of the options: 1, 2, 3, 4 or 5\n")
        else:
            if choice >5 or choice <=0:
                print("Sorry, please enter one of the options: 1, 2, 3, 4 or 5\n")
                continue
            elif choice == 1:
                mode = 1
                break
            elif choice == 2:
                mode = 2
            elif choice == 3:
                mode = 3
            elif choice == 4:
                mode = 4
            elif choice ==5:
                mode =5

    while mode == 1:
        #mode1, open an account.
        clear_output()
        print("You have choosen to open an account")
        account_type = ''
        try:
            choice = int(input("What kind of account would you like to open?\n(1) Checking Account\n(2) Savings Account\n(3) Business Account\n"))
        except ValueError:
            print(error_message)
        else:
            if choice == 1:
                x = random.randint(100000,199999)
                the_customer.open_checking(x,0)
                print(f"You have successfully opened a checking account with Whitaker Banking. Your account number is {x}\n")
                mode =0
            elif choice ==2:
                x = random.randint(100000,199999)
                the_customer.open_savings(x,0)
                print(f"You have successfully opened a savings account with Whitaker Banking. Your account number is {x}\n")
                mode =0
            elif choice ==3:
                x = random.randint(100000,199999)
                the_customer.open_checking(x,0)
                print(f"You have successfully opened a business account with Whitaker Banking. Your account number is {x}\n")
                mode =0

    while mode ==2:
        #mode2, make a deposit
        #make_deposit(cust,acct_type,acct_num,dept_amt)
        try:
            ask_type = int(input("Please enter the account type: (1) Checking, (2) Savings, (3) Business\n"))
        except ValueError:
            print(error_message)
        except ask_type < 0 or ask_type >3:
            print(error_message)
        else:
            if ask_type == 1:
                dep_type = 'C'
            elif ask_type == 2:
                dep_type = 'S'
            elif ask_type == 3:
                dep_type = 'B'

        try:
            ask_num = int(input("Please enter the account number:\n"))
        except ValueError:
            print(error_message)
        else:
            num = ask_num

        try:
            ask_dept = int(input("How much would you like to deposit?\n"))
        except ValueError:
            print(error_message)
        else:
            dep = ask_dept

        make_deposit(the_customer,dep_type,num,dep)
        print(f"You have successfully deposited ${dep}.\n")
        mode=0

    while mode == 3:
        #mode3, make a withdrawal
        try:
            ask_type = int(input("Please enter the account type: (1) Checking, (2) Savings, (3) Business\n"))
        except ValueError:
            print(error_message)
        except ask_type < 0 or ask_type >3:
            print(error_message)
        else:
            if ask_type == 1:
                dep_type = 'C'
            elif ask_type == 2:
                dep_type = 'S'
            elif ask_type == 3:
                dep_type = 'B'

        try:
            ask_num = int(input("Please enter the account number:\n"))
        except ValueError:
            print(error_message)
        else:
            num = ask_num

        try:
            ask_dept = int(input("How much would you like to withdraw:\n"))
        except ValueError:
            print(error_message)
        else:
            dep = ask_dept

        make_withdraw(the_customer,dep_type,num,dep)
        print(f"You have successfully withdrawn ${dep}.\n")
        mode=0


    while mode == 4:
        #mode4, get total balance.
        clear_output()
        the_customer.get_total_balance()
        print("\n")
        mode =0

    while mode == 5:
        #<<< It would be better to have a confirmation choice here, like "Are you sure you want to quit?"
        #instead of just quitting right away
        try:
            y= int(input("Are you sure you want to quit? Enter 1 to confirm, 2 to go back.\n"))
        except ValueError:
            print("Sorry, please try again.\n")
        else:
            if y == 1:
                clear_output()
                print("Thank you for choosing Whitaker Banking.")
                print("We look forward to your next visit.")
                in_use = False
                break
            else:
                mode =0

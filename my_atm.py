from datetime import datetime
import random


database = {6574762937: ["John", "Doe", "jdoe@gmail.com", "password", 50]}

print("Welcome to Blood Bank \n")
print("=" * 50)
now = datetime.now()
currentDT = now.strftime("%d/%m/%Y | %H:%M:%S")
print("Date & time\n%s" % currentDT)
print("=" * 50)

def home():

    validUser = int(input("Do you have an account with us? (1) Yes (2) No \n"))
    if(validUser == 1):
        login()
    elif(validUser == 2):
        register()
    else:
        print("Invalid option selected")
        home()


def register():
    email = input("Please enter your email address: ")

    # Very weak email validation. Can easily be fooled with "@.com"
    if "@" in email and email.endswith(".com",):
        pass       
    else:
        print("Invalid email address")
        register()

    f_name = input("Please enter your first name: ")
    l_name = input("Please enter your last name: ")
    passWd = input("Please create a unique password: ")

    userAccountNum = accountNumGen()
    accountbal = 0

    database[userAccountNum] = [ f_name, l_name, email, passWd, accountbal ]
    
    print("Your account has been created")
    print("=" * 50)
    print("Your account number is: %d" % userAccountNum)
    print("=" * 50)

    login()


def login():    
    AccountNumFromUser = int(input("Enter your account number: \n"))
    PasswordFromUser = input("Enter your password: \n")

    for userAccountNum, UserDetails in database.items():
        if(AccountNumFromUser == userAccountNum):
            if(PasswordFromUser == UserDetails[3]):
                bankOp(userAccountNum, UserDetails)
            else:
                print("Wrong password. Try again.")
                print("=" * 50)
                login()
        

def bankOp(userid, userinfo):
    print("=" * 50)
    print("Welcome %s %s \n" % (userinfo[0], userinfo[1]))
    print("These are the availabe options:")
    print("1. Check Balance")
    print("2. Withdrawal")
    print("3. Cash Deposit")
    print("4. Complaint")
    print("5. Logout")
    print("6. Exit")

    selectedOption = int(input("Please select an option: "))

    if (selectedOption == 1):
        print("Your current balance is %d" % userinfo[4])
    elif (selectedOption == 2):
        withdrawalOp(userinfo)
    elif (selectedOption == 3):
        depositOp(userinfo)
    elif (selectedOption == 4):
        complaintOp()
    elif (selectedOption == 5):
        print("=" * 50)
        home()
    elif (selectedOption == 6):
        exit()
    else:
        print("=" * 50)
        print("Invalid Option selected, please try again")
        print("="*50)
        bankOp(userid, userinfo)

    print("=" * 50)

    anyOther = int(input("\nWill you like to do any other operation: (1) Yes (2) No: "))
    if(anyOther == 1):
        bankOp(userid, userinfo)
    elif(anyOther == 2):
        print("Have A Good Day :-)")
        exit()


def depositOp(balance):
    cashDeposit = int(input("How much would you like to deposit? \n"))
    print("Deposit successful")
    balance[4] += cashDeposit
    print("Your current balance is $%d" % balance[4] )


def withdrawalOp(balance):
    withdrawal = int(input("How much would you like to withdraw? \n"))
    
    if withdrawal <= balance[4]:
        balance[4] -= withdrawal
        print("Take your cash of $%d" % withdrawal)
    else:
        print("=" * 50)
        print("Insufficient Funds. \n")
        print("Your current balance is %d \n" % balance[4])
        print("=" * 50)
        withdrawalOp(balance)

def complaintOp():
    compliant = input("What issue will you like to report \n")
    print("Thank you for contacting us")

def accountNumGen():
    return random.randrange(1111111111,9999999999)

home()
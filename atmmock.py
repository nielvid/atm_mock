import datetime
date = datetime.datetime.today()
allowedUsers = ['Godson', "Kate", "Deray"]
allowedPassword = ['123456', 'deray@08', '2016']
name = input("what is your name \n ")
if name in allowedUsers:
    password = input("Password\n")
    userId = allowedUsers.index(name)
    if password == allowedPassword[userId]:
        print("*****************************")
        print("Welcome %s " % name)
        print("You login today %s" % date)
        print("*****************************")
        print('What do you want to do ')
        print('Available options are:')
        print('1. Withdraw Cash')
        print('2. Deposit Cash')
        print('3. Print Statement')

        transaction = int(input('Select an option: \n'))
        if transaction == 1:
            try:
                amount = int(input('How much do you want to withdraw \n'))
                if not amount:
                    raise TypeError
                else:
                    print("Take your cash")
            except TypeError:
                print("Amount is not in digit")


        elif transaction == 2:
            try:
                amount = int(input('How much do you want to deposit\n'))
                if not amount:
                    raise TypeError
                else:
                    print("Your Balance is %d" % amount)
            except TypeError:
                print("Amount is not in digit")
            pass
        elif transaction == 3:
            issue = input('What issue will you like to report?\n')
            print("Thank you for contacting us")
        else:
            print('Invalid option, try again')
    else:
        print("Incorrect Password")
else:
    print('Name not found')

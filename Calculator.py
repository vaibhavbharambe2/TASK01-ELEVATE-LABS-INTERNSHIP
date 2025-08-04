
def Add(Entered_Numbers):
    Result = 0

    for numbers in Entered_Numbers:
        Result += numbers
    print("==> Addition is: ", Result)
    print()


def Sub(Entered_Numbers):
    Result = Entered_Numbers[0]

    for numbers in Entered_Numbers[1:]:
        Result -= numbers
    print("==> Difference is: ", Result)
    print()


def Mul(Entered_Numbers):
    Result = 1

    for numbers in Entered_Numbers:
        Result *= numbers
    print("==> Multiplication is: ", Result)
    print()


def Div(Entered_Numbers):
    Result = Entered_Numbers[0]

    for numbers in Entered_Numbers[1:]:
        try:
            Result /= numbers
        except ZeroDivisionError:    # if entered numbers has 0.
            print("==> Cannot divide by zero. Please make sure you dont enter '0' while selecting division operation.")
            print()
            return
    print("==> Division is: ", Result)
    print()



def Calculator():

    print("""   CALCULATOR APP

        Hello Guest, Please enter numbers for calculation and select the action you want to perform:

        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Exit

        """)

    print()    # Adding blank line.

    User_Choice = int(input("Enter your choice. Please enter number mentioned against the action: "))

    if User_Choice == 5:
        print("Exiting Calculator...")
        exit()

    print()

    User_Input = input("Enter more than one number separated by spaces: ").split()

    print()

    Entered_Numbers = []    #Creating a blank list.

    for item in User_Input:
        try:
            num = float(item)   # Converting entered numbers to float to allow decimal numbers calculations.
            Entered_Numbers.append(num)     # Adding entered numbers in the list.
        except ValueError:
            # making sure only integers and decimal values are allowed.
            print("==> Please revise your answer.  Enter integers or decimal numbers only.")
            print()
            return


    match User_Choice:

        case 1:
            Add(Entered_Numbers)
        case 2:
            Sub(Entered_Numbers)
        case 3:
            Mul(Entered_Numbers)
        case 4:
            Div(Entered_Numbers)
        case 5:
            print("Exiting Calculator...")
            exit()
        case _:
            print("==> Invalid input. Please select from 1 to 5.")
            print()

while True:  # running function till user dont exit.
    Calculator()

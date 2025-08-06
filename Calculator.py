

def Add(Entered_Numbers):
    Result = 0

    for numbers in Entered_Numbers:
        Result += numbers
    
    print("==> Addition is: ", Result, "\n")


def Sub(Entered_Numbers):
    Result = Entered_Numbers[0]

    for numbers in Entered_Numbers[1:]:
        Result -= numbers
        
    print("==> Difference is: ", Result, "\n")


def Mul(Entered_Numbers):
    Result = 1

    for numbers in Entered_Numbers:
        Result *= numbers

    print("==> Multiplication is: ", Result, "\n")


def Div(Entered_Numbers):
    Result = Entered_Numbers[0]

    for numbers in Entered_Numbers[1:]:
        try:
            Result /= numbers
        except ZeroDivisionError:
            print("==> Cannot divide by zero. Please make sure you dont enter '0' while selecting division operation. \n")
            return
        
    print("==> Division is: ", Result, "\n")



def Calculator():

    while True:

        print("** Welcome to CALCULATOR APP ** \n")
        print("Hello Guest, Please enter numbers for calculation and select the action you want to perform:\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        print()

        try:
            User_Choice = int(input("Enter your choice. Please enter number mentioned against the action: "))
        except ValueError:
            print("\n ==> Invalid input. Please select from 1 to 5. \n")
            continue

        if User_Choice == 5:
            print("Exiting Calculator...")
            break

        print()

        if User_Choice >= 1 and User_Choice <= 5:

            User_Input = input("Enter more than one number separated by spaces: ").split()

            print()

            Entered_Numbers = []

            try:
                for item in User_Input:
                    num = float(item)
                    Entered_Numbers.append(num) 
            except ValueError:
                print("==> Please revise your answer.  Enter integers or decimal numbers only. \n")
                continue
                
            if len(Entered_Numbers) < 2:
                print("==> Please enter at least two numbers.\n")
                continue

            if User_Choice == 1:
                Add(Entered_Numbers)
            elif User_Choice == 2:
                Sub(Entered_Numbers)
            elif User_Choice == 3:
                Mul(Entered_Numbers)
            elif User_Choice == 4:
                Div(Entered_Numbers)
            elif User_Choice == 5:
                print("Exiting Calculator...")
                break
            else:
                print("==> Invalid input. Please select from 1 to 5. \n")

        else:
            print("==> Invalid input. Please select from 1 to 5. \n")



Calculator()

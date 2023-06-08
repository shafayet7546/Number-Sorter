def InputTaker(a):
    x = []
    Numinput = 0
    count = 1

    for i in range(a):
        print("Please input digit #", count, end = ":")
        count += 1
        NumInput = int(input())
        x.append(NumInput)
    x.sort()
    return x
    
def main():
        NumChoices = 0
        UserinputTwo = ""
        y = []
        FinalResult = 0

        NumChoices = int(input("Welcome to the Program that sorts your number inputs from least to greatest! \nPlease input the number of digits you want to provide the sorter: "))
        
        if(NumChoices > 0):
            y = InputTaker(NumChoices)
            print("Your Inputted digits from least to greatest is:", y)
        else:
            UserInputTwo = input("You must provide atleast one digit. Would you like to try again?")
            if(UserInputTwo.upper() == "YES"):
                main()
            elif(UserInputTwo.upper() == "NO"):
                print("Good Bye")
        
main()
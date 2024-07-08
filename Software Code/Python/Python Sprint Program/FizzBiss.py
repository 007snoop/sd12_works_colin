#Code for Lucien and groups sprint Python Project number 2
#Description - a program to find all the fizzbizz... 
#Author - Lucien Swyers (cody and colin too <3)
#Dates - until june 26th

# Function to validate user input (since i messed up the last QAP a little, 
# i wanted to show i knew how to validate now and the problem was far to simple on its own :) )


def get_user_input():
    while True:
        User_Input = input("Would you like to find all the FizzBizz? (Y/N): ").strip().upper()
        if User_Input in ['Y', 'N']:
            return User_Input
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

# Main program
def main():
    User_Input = get_user_input()

    if User_Input == 'Y':
        for i in range(1, 101):
            if i % 5 == 0 and i % 8 == 0:
                print("FizzBizz")
            elif i % 5 == 0:
                print("Fizz")
            elif i % 8 == 0:
                print("Bizz")
            else:
                print(i)
        print("Congratulations! You have found all the FizzBizz!")
    else:
        print("Program ended.")

# edited by colin, had to define a fuction of main to pull program from menu
if __name__ == "__main__":
    main()
#We found all the fizzbizz... ;) 
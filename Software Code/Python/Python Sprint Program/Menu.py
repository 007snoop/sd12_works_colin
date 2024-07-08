# Description: Menu to display the programs we built.
# Author(s): Colin G. Yetman, Cody Collins, Lucien Swyers (College of Keyin Tech Software Development)
# Date(s): June 22nd, 2024

# Define required libraries.
import importlib

# Define program constants.
PROGRAMLIST = {  # builds a list of programs that are called using the functions
    1: {"name": "Complete a Travel Claim!", "module": "TravelClaim"},
    2: {"name": "Fun Interview Question", "module": "FizzBiss"},
    3: {"name": "Cool Stuff with Strings and Dates", "module": "CoolStuff"},
    4: {"name": "A little Bit of Everything", "module": "Everything"},
    5: {"name": "Something New, Something Old", "module": "SomethingNewSomethingOld"},
    6: {"name": "Exit", "module": None}
}

# Define program functions.
def menuDSP():
    # Menu display to pull from built program list.
    print("Program Menu: ")
    for key, value in PROGRAMLIST.items():
        print(f"{key}. {value['name']}")

def exeProgram(choice):
    # Pulls program inside the same directory as menu.py only if the option is not None [6]
    if choice in PROGRAMLIST:
        program = PROGRAMLIST[choice]
        if program["module"] is not None:
            module = importlib.import_module(program["module"])
            module.main()  # Assumes each module has a main() function
        else:
            print("Exiting program...")
            exit(0)  # terminate program completely
    else:  # this is outside the inside if/else to feedback an entry error
        print(f"\n\nDATA ENTRY ERROR - Please choose a number between 1 and 6.")

# Main program starts here.
if __name__ == "__main__":  # this line ensures that the next lines of code only run when this program is called directly
    while True:
        menuDSP()
        try:
            menuOption = int(input("Enter a number from 1 to 6: "))
            exeProgram(menuOption)
        except ValueError:
            print("Please enter a valid number between 1 and 6.")

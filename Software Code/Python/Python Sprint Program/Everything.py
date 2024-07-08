# Description: Python Sprint 1 - #4 A Little Bit of Everything - XYZ Company maintenance schedule
# Author: Cody Collins
# Date(s): June 18, 2024 - June 19, 2024
 
 
# Define required libraries.
import FormatValues as FV
import datetime

# Define program constants.
SALV_VAL_RATE = .10
USEFUL_MONTHS = 180

CurDate = datetime.datetime.now()
CurDateDSP = FV.FDateL(CurDate)


# Define program functions.
# function taken from https://www.geeksforgeeks.org/add-months-to-datetime-object-in-python/
def add_months(current_date, months_to_add):
    new_date = datetime.datetime(current_date.year + (current_date.month + months_to_add - 1) // 12,
                        (current_date.month + months_to_add - 1) % 12 + 1,
                        current_date.day, current_date.hour, current_date.minute, current_date.second)
    return new_date

def MthDiff(Date1, Date2):
    return Date1.month - Date2.month + 12 *(Date1.year - Date2.year)

def CleanDateList(PurDate, current_date):
    # function to create a list of every 10 days from the purchase date
    date_list = [PurDate + datetime.timedelta(days=10*i) for i in range(600)]

    # Get the current date
    current_date = datetime.datetime.now()

    # Find the closest date in the future from the generated list
    next_date = min(date for date in date_list if date > current_date)
    return next_date

def CheckDateList(PurDate, current_date):
    # function to create a list of every 3 weeks from the purchase date
    date_list = [PurDate + datetime.timedelta(weeks=3*i) for i in range(300)]

    # Get the current date
    current_date = datetime.datetime.now()

    # Find the closest date in the future from the generated list
    next_date = min(date for date in date_list if date > current_date)
    return next_date

def InspectDateList(PurDate, current_date):
    # function to create a list of every 6 months from the purchase date
    date_list = [PurDate + datetime.timedelta(days=183*i) for i in range(50)]

    # Get the current date
    current_date = datetime.datetime.now()

    # Find the closest date in the future from the generated list
    next_date = min(date for date in date_list if date > current_date)
    return next_date


# Main program starts here.
def main():
    while True:
        #gather user inputs
        while True:
            try:
                EquipCost = float(input("Enter the cost of the equipment:v"))
            except:
                print()
                print("ERROR - Equipment cost must be a valid number.")
                print()
            else:
                break
        while True:
            try:
                PurDate = input("Enter the purchase date (YYYY-MM-DD): ")
                PurDate = datetime.datetime.strptime(PurDate, "%Y-%m-%d")
            except:
                print()
                print("ERROR - Purchase date is not a valid format (YYYY-MM-DD).")
                print()
            if PurDate > CurDate:
                print()
                print("ERROR - Purchase date cannot be greater than the current date.")
                print()
            else:
                break

        #perform required calculations

        CleanDateNext = FV.FDateS(CleanDateList(PurDate, CurDate))


        CheckDateNext = FV.FDateS(CheckDateList(PurDate, CurDate))


        InspectDateNext = FV.FDateS(InspectDateList(PurDate, CurDate))

    

        UsefulLifeEnd = add_months(PurDate, USEFUL_MONTHS)

        SalvVal = EquipCost * SALV_VAL_RATE

        MthlyAmort = (EquipCost - SalvVal) / USEFUL_MONTHS

        # Display Results

        #                1         2         3         4         5         6         7
        #       12345678901234567890123456789012345678901234567890123456789012345678901234567890
        print()
        print()
        print(f"                                XYZ Company")
        print(f"                            Maintenance Schedule")
        print(f"------------------------------------------------------------------------------")
        print(f"                                                      {CurDateDSP}")
        print()
        print(f"Equipment Cost: {EquipCost}")
        print(f"Purchase Date:  {FV.FDateS(PurDate)}")
        print()
        print()
        print()
        print(f"                Schedule")
        print(f"------------------------------------------")
        print()
        print(f"Next Cleaning Date:             {CleanDateNext}")
        print()
        print(f"Next Tube and Fluid Check Date: {CheckDateNext}")
        print()
        print(f"Next Major Inspection Date:     {InspectDateNext}")
        print()
        print()
        print()
        print(f"                                                             Cost")
        print(f"                                                -----------------------------")
        print(f"                                                Amortization:       {FV.FDollar2(MthlyAmort):>9s}")
        print(f"                                                Salvage Value:      {FV.FDollar2(SalvVal):>9s}")
        print()
        print(f"Useful Life End: {FV.FDateS(UsefulLifeEnd)}")
        print("-----------------------------------------------------------------------------")
        print()
        print()

        # To end program

        ProgramEnd = input("Enter END to quit or anything to continue: ").upper()
        if ProgramEnd == "END":
            break

if __name__ == "__main__":
    main()

# Any housekeeping duties at the end of the program.
print()
print("Thank you for using this program!")
print()
# Description: Python Sprint 1 - #3 Cool Stuff with Strings and Dates. Program for a company to enter a new employee into their database
# Author: Cody Collins
# Date(s): June 17, 2024 -
 
 
# Define required libraries.
import datetime
import FormatValues as FV
import random

# Define program constants.
CurDate = datetime.datetime.now()
CurDateDSP = FV.FDateS(CurDate)
EmpRand = random.randint(1000,9999)


# Define program functions.



# Main program starts here.
def main():
    while True:

        # Gather User Inputs

        while True:
            EmpFName = input("Enter the employee's first name (END to quit): ").title()

            if EmpFName == "":
                print()
                print("ERROR - Employee first name cannot be blank.")
                print()
            else:
                break
        if EmpFName.upper() == "END":
            break

        while True:
            EmpLName = input("Enter the employee's last name: ").title()
            if EmpLName == "":
                print()
                print("ERROR - Employee last name cannot be blank.")
                print()
            else:
                break

        allowed_char = "1234567890"
        while True:
            EmpPhNum = input("Enter the employee's phone number (9999999999): ")
            if EmpPhNum == "":
                print()
                print("ERROR - Employee phone number cannot be blank.")
                print()
            
            elif set(EmpPhNum).issubset(allowed_char) == False:
                print()
                print("ERROR - Employee phone number contains invalid characters.")
                print()

            else:
                break
        
        while True:
            EmpAdd = input("Enter the employee's street address: ")
            if EmpAdd == "":
                print()
                print("ERROR - Employee address cannot be blank.")
                print()
            else:
                break

        while True:
            try:
                EmpStartDate = input("Enter the employee's start date (YYYY-MM-DD): ")
                EmpStartDate = datetime.datetime.strptime(EmpStartDate, "%Y-%m-%d")
            except:
                print()
                print("ERROR - Employee start date is not a valid format (YYYY-MM-DD).")
                print()
            else:
                break
        
        while True:
            try:
                EmpBDay = input("Enter the employee's birth date (YYYY-MM-DD): ")
                EmpBDay = datetime.datetime.strptime(EmpBDay, "%Y-%m-%d")
            except:
                print()
                print("ERROR - Employee birth date is not a valid format (YYYY-MM-DD).")
                print()
            else:
                break
        
        while True:
            EmpPos = input("Enter the employee position: ")
            if EmpPos == "":
                print()
                print("ERROR - Employee position cannot be blank.")
                print()
            else:
                break
        
        while True:
            EmpPass = input("Enter employee password (must contain at least 8 characters): ")
            LowerCount = 0
            UpperCount = 0
            NumCount = 0
            for Letter in EmpPass:
                if Letter.isalpha() == True and Letter.isupper() == True:
                    UpperCount += 1
                elif Letter.isalpha() == True and Letter.islower() == True:
                    LowerCount += 1
                elif Letter.isdigit() == True:
                    NumCount +=1

            if len(EmpPass) < 8:
                print()
                print("ERROR - Password must be 8 characters or greater.")
                print()
            elif UpperCount == 0:
                print()
                print("ERROR - password must contain at least one uppercase character")
                print()
            elif LowerCount == 0:
                print()
                print("ERROR - password must contain at least one lowercase character")
                print()
            elif NumCount == 0:
                print()
                print("ERROR - password must contain at least one number character")
                print()
            else: 
                break
        
        # Perform required calculations
        
        EmpID = EmpFName[0] + EmpLName[0] + "-" + EmpPhNum[6:10] + "-" + str(EmpRand)
        
        EmpUser = EmpFName + EmpLName[0] + str(EmpRand)
        
        EmpPhNumDSP = "(" + EmpPhNum[0:3] + ")" + " " + EmpPhNum[3:6] + "-" + EmpPhNum[6:10]

        # Display results
        EmpStartDateDSP = FV.FDateS(EmpStartDate)
        EmpBDayDSP = FV.FDateS(EmpBDay)
        print()
        print()
        print(f"New Employee Intake")
        print(f"{CurDateDSP}")
        print()
        print(f"Name:          {EmpFName} {EmpLName}")
        print(f"Birth Date:    {EmpBDayDSP}")
        print(f"Phone Number:  {EmpPhNumDSP}")
        print(f"Address:       {EmpAdd}")
        print()
        print(f"Position:      {EmpPos}")
        print()
        print(f"Start Date:    {EmpStartDateDSP}")
        print()
        print(f"ID:            {EmpID}")
        print()
        print(f"Username:      {EmpUser}")
        print(f"Password:      {EmpPass}")
        print()
        print()
 
# removed housekeeping from file to replace with main fuction to pull from menu file
if __name__ == "__main__":
    main()
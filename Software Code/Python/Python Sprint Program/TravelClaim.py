#Code for Lucien and groups sprint Python Project number 1
#Description - a program for a chocolate companys employee travel claims
#Author - Lucien Swyers (cody and colin too <3)
#Dates - until june 26th


import datetime


# Constants for all
EMPLOYEE_NUMBER_LENGTH = 5
MAX_TRIP_DAYS = 7
MAX_KILOMETERS = 2000
PER_DIEM_RATE = 85.00
MILEAGE_RATE_OWN_CAR = 0.17
MILEAGE_RATE_RENTED_CAR = 65.00
BONUS_DAYS_THRESHOLD = 3
BONUS_AMOUNT_DAYS_THRESHOLD = 100.00
BONUS_KILOMETERS_THRESHOLD = 1000
BONUS_RATE_EXTRA_KILOMETERS = 0.04
EXECUTIVE_BONUS_RATE = 45.00
HOLIDAY_BONUS_RATE = 50.00
HST_RATE = 0.15
HOLIDAY_START_DATE = datetime.datetime(2024, 12, 15)
HOLIDAY_END_DATE = datetime.datetime(2024, 12, 22)

#Define a bunch of important blocks

def validate_employee_number(Emp_Number):
    return len(Emp_Number) == EMPLOYEE_NUMBER_LENGTH

def validate_name(Name):
    return Name.strip() != ""

def validate_date(Date_Str):
    try:
        return datetime.datetime.strptime(Date_Str, "%Y-%m-%d")
    except ValueError:
        return None

def calculate_per_diem(Days):
    return Days * PER_DIEM_RATE

def calculate_mileage(Kilometers, Car_Type, Days):
    if Car_Type == "O":
        return Kilometers * MILEAGE_RATE_OWN_CAR
    elif Car_Type == "R":
        return Days * MILEAGE_RATE_RENTED_CAR
    return 0

def calculate_bonus(Days, Kilometers, Car_Type, Claim_Type, Start_Date):
    Bonus = 0
    if Days > BONUS_DAYS_THRESHOLD:
        Bonus += BONUS_AMOUNT_DAYS_THRESHOLD
    if Kilometers > BONUS_KILOMETERS_THRESHOLD and Car_Type == "O":
        Bonus += Kilometers * BONUS_RATE_EXTRA_KILOMETERS
    if Claim_Type == "E":
        Bonus += Days * EXECUTIVE_BONUS_RATE
    if HOLIDAY_START_DATE <= Start_Date <= HOLIDAY_END_DATE:
        Bonus += Days * HOLIDAY_BONUS_RATE
    return Bonus

def calculate_hst(Claim_amount):
    return Claim_amount * HST_RATE

def main():
    while True:
        # Get inputs from our users!
        Emp_Number = input("Enter employee number (5 characters) or 'exit' to quit: ").strip()
        if Emp_Number.lower() == "exit":
            break
        if not validate_employee_number(Emp_Number):
            print(f"Invalid employee number. It must be {EMPLOYEE_NUMBER_LENGTH} characters.")
            continue

        First_Name = input("Enter employee first name: ").strip().title()
        if not validate_name(First_Name):
            print("First name must be entered.")
            continue

        Last_Name = input("Enter employee last name: ").strip().title()
        if not validate_name(Last_Name):
            print("Last name must be entered.")
            continue

        Location = input("Enter location of the trip: ").strip()

        Start_Date_Str = input("Enter start date (YYYY-MM-DD): ").strip()
        Start_Date = validate_date(Start_Date_Str)
        if not Start_Date:
            print("Invalid start date.")
            continue

        End_Date_Str = input("Enter end date (YYYY-MM-DD): ").strip()
        End_Date = validate_date(End_Date_Str)
        if not End_Date:
            print("Invalid end date.")
            continue

        if End_Date <= Start_Date or (End_Date - Start_Date).days > MAX_TRIP_DAYS:
            print(f"End date must be after start date and within {MAX_TRIP_DAYS} days.")
            continue

        Car_Type = input("Did you use your own car or rented car (O/R): ").strip().upper()
        if Car_Type not in ["O", "R"]:
            print("Invalid car type. Must be 'O' or 'R'.")
            continue

        Kilometers = 0
        if Car_Type == "O":
            Kilometers = int(input("Enter total kilometers traveled: ").strip())
            if Kilometers > MAX_KILOMETERS:
                print(f"Kilometers cannot exceed {MAX_KILOMETERS}.")
                continue

        Claim_Type = input("Enter claim type (Standard/Executive) (S/E): ").strip().upper()
        if Claim_Type not in ["S", "E"]:
            print("Invalid claim type. Must be 'S' or 'E'.")
            continue

        # Calculate values for our program
        Days = (End_Date - Start_Date).days + 1
        Per_Diem = calculate_per_diem(Days)
        Mileage_Amount = calculate_mileage(Kilometers, Car_Type, Days)
        Bonus = calculate_bonus(Days, Kilometers, Car_Type, Claim_Type, Start_Date)
        Claim_Amount = Per_Diem + Mileage_Amount + Bonus
        HST = calculate_hst(Claim_Amount)
        Claim_Total = Claim_Amount + HST

        # Display results
        print("\nEmployee Travel Claim Summary")
        print(f"Employee Number: {Emp_Number}")
        print(f"Employee Name: {First_Name} {Last_Name}")
        print(f"Location: {Location}")
        print(f"Start Date: {Start_Date_Str}")
        print(f"End Date: {End_Date_Str}")
        print(f"Number of Days: {Days}")
        print(f"Per Diem Amount: ${Per_Diem:.2f}")
        if Mileage_Amount > 0:
            print(f"Mileage Amount: ${Mileage_Amount:.2f}")
        print(f"Bonus: ${Bonus:.2f}")
        print(f"Claim Amount: ${Claim_Amount:.2f}")
        print(f"HST (15%): ${HST:.2f}")
        print(f"Claim Total: ${Claim_Total:.2f}\n")

        # Prompt to repeat or exit our program
        Continue_Input = input("Would you like to enter another claim? (yes/no): ").strip().lower()
        if Continue_Input != "yes":
            break

if __name__ == "__main__":
    main()

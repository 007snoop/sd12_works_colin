# Dataclass builder for creating people and sorting data automatically.
# Written by Colin G. Yetman 

from dataclasses import dataclass

@dataclass
class Person: 
    # automatically building a boilerplate dataset
    name: str
    age: int
    city: str # You can also specify any value here when no input is used.
    province: str
    country: str
    # This constructor will automatically store the data input by the user.

def personFromInput() -> Person:
    # build a dataclass from user input
    while True: # had to do this because data validation was breaking out of the loop with no data

        while True: # these loops keep the validation loop running while staying inside the main loop
            name = input("Enter Name: ").title()
            if not all(char.isalpha() or char.isspace() for char in name):
                print(f"\n\n DATA ENTRY ERROR \n\n")
            else:
                break

        while True:        
            try:
                age = int(input("Enter Age (between 1-99): "))
                if age < 0 or age > 100: 
                    print(f"\n\n DATA ENTRY ERROR \n\n")
                else: # this else must come before execpt
                    break
            except ValueError:
                print(f"\n\n DATA ENTRY ERROR\n\n")

        while True:
            city = input("Enter City: ").title()
            if not all(char.isalpha() or char.isspace() for char in city):
                print(f"\n\n DATA ENTRY ERROR \n\n")
            else:
                break

        while True:
            province = input("Enter Province: ").title()
            if not all(char.isalpha() or char.isspace() for char in province):
                print(f"\n\n DATA ENTRY ERROR \n\n")
            else:
                break

        while True:
            country = input("Enter Country: ").title()
            if not all(char.isalpha() or char.isspace() for char in country):
                print(f"\n\n DATA ENTRY ERROR \n\n")
            else:
                break 
        break
    
    # call person constructor later on
    return Person(name, age, city, province, country)

# person constructor
def main():
    while True:
        person = personFromInput() # this line is the entire program
# import this module and call the constructor function to build a person object


# display the person
        print(f"\n\n Name:\n {person.name}\n\n Age:\n {person.age}\n\n City:\n {person.city}\n\n Province:\n {person.province}\n\n Country:\n {person.country}\n\n")

if __name__ == "__main__":
    main()
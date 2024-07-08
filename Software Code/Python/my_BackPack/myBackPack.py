def fDollar2(DollarValue):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def fDollar0(DollarValue):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def fComma2(Value):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    ValueStr = "{:,.2f}".format(Value)

    return ValueStr

def fComma0(Value):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def fNumber0(Value):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def fNumber1(Value):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def fNumber2(Value):
    # function will accept a value and format it to $#,###.##.
    # function Written by Maurice Babbin
    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def fDateS(DateValue):
    # function will accept a value and format it to yyyy-mm-dd.
    # function Written by Maurice Babbin
    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def fDateM(dateValue):
    # function will accept a value and format it to dd-Mon-yy.
    # function Written by Maurice Babbin
    dateValueStr = dateValue.strftime("%d-%b-%y")

    return dateValueStr


def fDateL(DateValue):
    # function will accept a value and format it to Day, Month dd, yyyy.
    # function Written by Maurice Babbin
    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr

def fNameS(nameValue):
    # function will accept multiple names and format it to ie: C. G. Y.
    # function Written by Colin Yetman Jun 15th 2024
    nameParts = nameValue.split() # Splits name into parts. first, Middle, Last. .split is based on spaces 

    nameInitails = " ".join([part[0] + "." for part in nameParts]) # sets parts [0] in nameParts up first, then Adds Space at front, then joins the first letter of each word with a "." added
    return nameInitails # Dont call this value, call fNameS() and use your name value in brackets

def fNameM(nameValue):
    # function will accept multiple names and format it to ie: C. Yetman
    # function Written by Colin Yetman Jun 15th 2024
    nameParts = nameValue.split() # Splits name into parts. first, Middle, Last. .split is based on spaces 

    firstInitial = nameParts[0][0] + "." # Both 0 values required as first grabs full first name and second grabs initial of first name
    lastName = nameParts[-1] # The -1 will always choose the last entered value

    formattedName = f"{firstInitial.title()} {lastName.title()}" # Takes already formatted first name and adds last name

    return formattedName # Dont call this, Call fNameM() and use your name value in brackets

def fNameL(nameValue):
    # function will accept multiple names and format it to ie: Colin Grant Yetman
    # function Written by Colin Yetman Jun 15th 2024
    nameParts = nameValue.split() # Splits name into parts. first, Middle, Last. .split is based on spaces 

    formattedParts = [part.title() for part in nameParts] # Sets first letter to capital in each name

    formattedName = " ".join(formattedParts) # Joins name with space between

    return formattedName # Dont call this value, call fNameL() and use your name value in brackets

def fNameFirstL(nameValue):
    # function will accept multiple names and format it to ie: Colin Y.
    # function Written by Colin Yetman Jun 15th 2024
    nameParts = nameValue.split() # Splits name into parts. first, Middle, Last. .split is based on spaces 

    firstName = nameParts[0] # Sets first value [0]
    lastName = nameParts[-1][0] + "." # Both values required, [-1] grabs last entered value, [0] grabs first letter of last value

    formattedName = f"{firstName.title()} {lastName.title()}" # Joins name values

    return formattedName # Dont call this value, call fNamefirstL() and use your name vlaue in brackets


# Program test kit
""" 
dollarValue = int(input("Enter a Dollar Value: "))

value = int(input("Enter a Number Value: "))

nameValue = input("Enter full name: ")


print(f"\n{fNameFirstL(nameValue)}\n")
print(f"\n{fDollar2(dollarValue)}\n")
print(f"\n{fComma2(value)}\n")
"""
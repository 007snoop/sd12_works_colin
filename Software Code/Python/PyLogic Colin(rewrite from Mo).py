# Description: A boilerplate template for Python programs.
# Author: Colin
# Date(s): [Add your dates here]

# Define required libraries.
# Example: import os, sys, math

# Define program constants.
# Example: PI = 3.14159

# Define program functions.

def getUserInput():
    """
    Function to gather user input.
    Example usage: return float(input("Enter a number: "))
    """
    try:
        value = float(input("Enter a number: "))
        return value
    except ValueError:
        print("Invalid input. Please enter a number.")
        return getUserInput()  # Recursively ask for input again

def performCalculations(inputData):
    """
    Function to perform required calculations.
    Example: return inputData * 2
    """
    return inputData * 2  # Simple example calculation

def displayResults(results):
    """
    Function to display results.
    Example usage: print(f"Results: {results}")
    """
    print(f"Results: {results}")

def writeResultsToFile(results, filename="results.txt"):
    """
    Function to write results to a file for future use.
    Modes can be "a" to append, "w" to overwrite, and "r" to read.
    Any value written to a file must be a string.
    Example usage: with open(filename, "w") as file: file.write(str(results))
    """
    try:
        with open(filename, "w") as file:
            file.write(str(results))
            print(f"Results written to {filename}")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main program starts here.
    """
    while True:
        # Gather user input
        userInput = getUserInput()

        # Perform required calculations
        results = performCalculations(userInput)

        # Display results
        displayResults(results)

        # Write results to file for future use
        writeResultsToFile(results)

        # Ask the user if they want to continue
        continueProgram = input("Do you want to continue? (yes/no): ").lower()
        if continueProgram != 'yes':
            break

    # Any housekeeping duties at the end of the program
    print("Program has ended. Thank you for using this program.")

# Run the main function
if __name__ == "__main__":
    main()
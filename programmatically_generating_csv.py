# Programmatically Generating CSV Files
# Author: Donavan McFadden
# Student ID: Donmcf8357
# This program builds on my Calculations and Return Values program. It keeps
# the dictionary menu, the validation, and my Temperature conversion. Now
# option 1 saves each record to a csv file called ZooData.csv, and option 2
# reads the file back and displays it.

from datetime import datetime

# The csv file my program saves to and reads from
CSV_PATH = "ZooData.csv"


# This function takes one Fahrenheit temperature and returns it in Celsius.
def convertData(data):
    return (data - 32) * 5 / 9


# This function appends one comma-separated line to the csv file at path. It
# opens the file in append mode ("a"), which creates the file if it does not
# exist yet, and uses try-except to catch any error while writing.
def insertData(path, data):
    try:
        with open(path, "a", newline="") as csvFile:
            csvFile.write(data + "\n")
        return True
    except OSError as error:
        print("Error: Could not write to " + path + ": " + str(error))
        return False


# This function displays the path of the csv file and everything in it. It
# opens the file read-only ("r"), the least permission needed to read it, and
# uses try-except to handle errors such as the file not existing yet.
def viewData(path):
    try:
        with open(path, "r") as csvFile:
            print("Reading data from: " + path)
            fileContents = csvFile.read()
            if fileContents == "":
                print("The file is empty. Choose option 1 to add data.")
            else:
                print(fileContents, end="")
    except FileNotFoundError:
        print("Error: " + path + " was not found. Choose option 1 to add data first.")
    except OSError as error:
        print("Error: Could not read " + path + ": " + str(error))


# This function asks how many records to enter, converts each temperature,
# and saves each record to ZooData.csv using insertData().
def getInput():
    try:
        entryCount = int(input("How many entries will be entered? "))

        for entry in range(entryCount):
            print()
            print("Entry " + str(entry + 1) + " of " + str(entryCount))
            recordDate = input("Enter the date of the record (MM/DD/YYYY): ")
            fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

            # convertData() requires one argument: the temperature in degrees Fahrenheit.
            # It returns the converted temperature in degrees Celsius.
            celsius = convertData(fahrenheit)

            # Build the comma-separated line: date, Fahrenheit, Celsius
            csvLine = recordDate + "," + str(fahrenheit) + "," + str(round(celsius, 2))

            # Save the line to ZooData.csv and confirm only if the write worked
            if insertData(CSV_PATH, csvLine):
                print("The following data was saved at " + str(datetime.now()) + ": " + csvLine + ".")
    except ValueError:
        print("Error: Please enter whole numbers for the entry count and temperature.")


# My student ID is stored as a string so it prints exactly as written.
student_id = "Donmcf8357"

# Title line (this is the first thing the program prints)
print(student_id + " Spreadsheet Automation Menu")

# The menu options are stored in a dictionary (key = option number, value = description)
menu_options = {
    "1": "Input Data",
    "2": "View Current Data",
    "3": "Generate Report"
}

# Use a for loop to print each option number and description in order
for number, description in menu_options.items():
    print(number + ". " + description)

# The next line retrieves the inputted option and stores into the variable called selected_option.
selected_option = input("Enter your selection (1, 2, or 3): ")

# Check if the choice is one of the dictionary keys
if selected_option in menu_options:
    print("Option " + selected_option + " has been selected")
    print("the time and date is", str(datetime.now()))
else:
    print("Error: Invalid choice selected.")

# Run the feature that matches the selection (options 1 and 2 are built so far)
if selected_option == "1":
    getInput()
elif selected_option == "2":
    viewData(CSV_PATH)
else:
    print("Error: The chosen functionality is not implemented yet")

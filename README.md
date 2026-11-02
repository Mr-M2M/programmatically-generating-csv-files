# Programmatically Generating CSV Files

**Author:** Donavan McFadden | **Student ID:** Donmcf8357

This is the next part of my Spreadsheet Automation project (Temperature spreadsheet). It builds on my Calculations and Return Values program and adds file handling, so my records are saved to a csv file and can be read back.

## Functions
- `convertData(data)`: converts a Fahrenheit temperature to Celsius with `(F - 32) * 5/9` and returns it.
- `insertData(path, data)`: opens the csv file in append mode (`"a"`), which creates it if it doesn't exist, and writes one comma-separated line inside a try-except.
- `viewData(path)`: opens the csv file read-only (`"r"`), the least permission needed, and prints the file path and its contents. A try-except handles a missing file or a read error.
- `getInput()`: asks how many entries to add. For each one, it asks for a date and a Fahrenheit temperature, converts it, saves `date,F,C` to `ZooData.csv` with `insertData()`, and prints `The following data was saved at <date/time>: <data>.` It's wrapped in a try-except.

## Menu
- `1`: Input Data. Calls `getInput()`.
- `2`: View Current Data. Calls `viewData("ZooData.csv")`.
- Anything else: `Error: The chosen functionality is not implemented yet`

## Files
- `programmatically_generating_csv.py`: the program
- `ZooData.csv`: the data file my program created during the three-entry run
- `ZooData_output_screenshot.png`: output from the three-entry run (top) and the second run choosing option 2 (bottom)

## How to run
Open `programmatically_generating_csv.py` in IDLE and choose **Run > Run Module**. Enter `1` and add 3 entries. Then run it again and enter `2` to view the saved data.

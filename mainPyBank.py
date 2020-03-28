# Import os module provides a way to use operating system dependent functionality. 
# The *os* and *os. path* modules include functions to interact with the file system.
# The csv module implements classes to read and write tabular data in CSV format.
import os
import csv

# Start the function header, (file) is a parameter - Passing csv file/list as an argument
def analyze_budget_data(file):
    # Declare variables
    total_months = 0
    total_profit = 0
    greatest_increase = 0
    greatest_increase_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""
    
    # Declare changes variable, create a list and track month to month change
    changes = []
    previous_profit_loss = 0

    # Using a with statement open the file
    # Using the csv module function csv.reader, structure data split at delimiter
    # next() excludes the first row of data (column heads) from the analysis 
    with open(file) as data:
        csvreader = csv.reader(data, delimiter = ',') 
        header = next(csvreader)

        # Loop through each row in csv, store values as date object and integer 
        # Input data - row[0] because date is the first item in the set, row[1] profit_loss is second item
        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])

            # total_profit = total_profit + profit_loss
            total_profit += profit_loss
            total_months += 1

            # Subtract previous month's profit_loss from current month profit_loss
            # Ignore first month, otherwise add the value for change to the change list
            change = profit_loss - previous_profit_loss
            if total_months !=1:
                changes.append(change)
            
            # Conditional statement to define greatest increase, decrease, and date
            # Continually calculate greatest_ while looping 
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = date
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = date
            # For next loop replace 0 with current profit_loss
            previous_profit_loss = profit_loss
    # Still inside of the with statement but outside the stored values
    # Calculate average_change by sum(changes) and divide by the length of the list len(changes), round 2 decimal places
    average_change = round(sum(changes)/len(changes), 2)

    # Create an f string to display the calculations
    Analysis = f"""
    Total Profit: ${total_profit}
    Total Months: {total_months}
    Average Monthly Change: ${average_change}
    Greatest Increase: {greatest_increase_month}, ${greatest_increase}
    Greatest Decrease: {greatest_decrease_month}, ${greatest_decrease}
    """

    print(Analysis)

    #Create output text file
    output_file = "output_PyBank.txt"
    with open(output_file, "w") as doc:
        doc.write(Analysis)

# Create file path for budget_data.csv file
path = os.path.join("Resources", "budget_data.csv")

# Run the function on the path
analyze_budget_data(path)




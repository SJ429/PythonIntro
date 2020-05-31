# Import the os module to create file path across operating systems
import os

# Module for reading CSV files
import csv

# Assignment of variables
month = []
date = []
totalnet_income_change = []

# Assignment of starting value to track changes
month_counts = 0
totalnet_income = 0
current_month_netincome = 0
previous_month_netincome = 0
netincome_month_change = 0

# Path of the file
csvpath = "C:/Users/susie/Desktop/python-challenge/PyBank/Resources/budget_data.csv"


# Open ans read CSV file  
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
  
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Begin to solve questions with codes
    # Find the number of months
    for row in csvreader: 
        month_counts += 1
   
       # Calculate total net income (P&L)
       # Define totalnet_income
        current_month_netincome = int(row[1])
        totalnet_income += current_month_netincome
        
        if(month_counts == 1):
            # Make value of previous and curent months equal 
            previous_month_netincome = current_month_netincome
            
        else:
            # Calcuate the monthly change in net income
            netincome_month_change = current_month_netincome - previous_month_netincome
            
            # Append each month to each month ongoing []   
            month.append(row[0])   
            
            # Append each month net income change
            totalnet_income_change.append(netincome_month_change) 
            
            # Make current month net income equal to the previous month net income 
            previous_month_netincome = current_month_netincome
            
            # Calculate average of changes in total net income 
            sum_totalnet_income_change = sum(totalnet_income_change) 
            average_incomechange = round(sum_totalnet_income_change/(month_counts-1), 2)

            # Greatest increase and decrease in net income and date (month and day) of these changes
            # Append date
            date.append(row[0])
            
            greatest_increase_totalnet_income = max(totalnet_income_change)
            greatest_decrease_totalnet_income = min(totalnet_income_change)
            increase_date = date[totalnet_income_change.index(greatest_increase_totalnet_income)]
            decrease_date = date[totalnet_income_change.index(greatest_decrease_totalnet_income)]         
   
# Print analysis to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_counts}")
    print(f"Total: {totalnet_income}")
    print(f"Average Change: {average_incomechange}")
    print(f"Greatest Increase in Profits: {increase_date} ({greatest_increase_totalnet_income})")
    print(f"Greatest Decrease in Profits: {decrease_date} ({greatest_decrease_totalnet_income})")
  
# Export results in a text file
PyBank_Results = "C:/Users/susie/Desktop/python-challenge/PyBank/analysis/PyBank_Results.txt"
with open(PyBank_Results, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months: {month_counts}\n")
    outfile.write(f"Total: {totalnet_income}\n")
    outfile.write(f"Average Change: {average_incomechange}\n")
    outfile.write(f"Greatest Increase in totalnet_income: {increase_date} ({greatest_increase_totalnet_income})\n")
    outfile.write(f"Greatest Decrease in totalnet_income: {decrease_date} ({greatest_decrease_totalnet_income})\n")

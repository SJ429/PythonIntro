# Import the os module
# Create file paths across operating systems
import os

# Module for reading CSV files
import csv

candidates = {}
totalvotes = 0

# Set path for file

csvpath = "C:/Users/susie/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Open and read CSV 

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
   
    # Read each row of data after the header
    for row in csvreader:
        
        # Calculate total votes
        totalvotes += 1

        # Determine the number of votes per canadidate
        candidate = row[2]
               
        if candidate not in candidates:
            candidates[candidate] = 1 

        else:
            candidates[candidate] += 1 

        # Print the results of the analysis 
    print("Election Results")
    print(f"Total Votes: {totalvotes}")
    print("----------------------------")
    for key, value in candidates.items():
        print(f"{key} : {str('{0:.3%}'.format(value /totalvotes))}, ({value})")
    print("----------------------------")
    print(f"Winner: {max(candidates, key=candidates.get)}")

    #  Write results in a text file 
PyBank_Results = "C:/Users/susie/Desktop/python-challenge/PyPoll/analysis/PyPoll_Results.txt"
with open(PyBank_Results, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Votes: {totalvotes}\n")
    outfile.write("----------------------------\n")
    for key, value in candidates.items():
        outfile.write(f"{key} : {str('{0:.3%}'.format(value /totalvotes))}, ({value})\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Winner: {max(candidates, key=candidates.get)})\n")
    outfile.write("----------------------------\n")
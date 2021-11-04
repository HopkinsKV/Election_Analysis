# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
   # Read the file object with the reader function. 
   # file_reader is referencing the fileobject stored in memory
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file as a list.
    for row in file_reader:
        print(row)



#Do analysis here
#1 the total number of votes
#2 complete list of candidates that got votes
#3 the perrcentage of votes per candidates
#4 total number of votes per candidates
#5 the winner based on votes



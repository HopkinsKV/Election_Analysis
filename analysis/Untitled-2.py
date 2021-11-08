# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# 2: Track the largest county and county voter turnout.
total_votes= 0
county_largest = ""
county_percentage = 0
largest_turnout = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
   # Read the file object with the reader function.
   # ***file_reader is referencing the fileobject stored in memory***
    file_reader = csv.reader(election_data)

    # Read the header row (skipping it with next)
    headers = next(file_reader)

    # Print each row in the CSV file as a list.
    for row in file_reader:
        total_votes += 1
        # 3: Extract the county name from each row.
        county_name = (row[1])
        
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1




    # 6a: Write a for loop to get the county from the county dictionary.
    with open(file_to_save, "w") as txt_file:
        for county_name in county_votes:
            # 6b: Retrieve the county vote count.
            countyvotes = county_votes[county_name]
            # 6c: Calculate the percentage of votes for the county.
            county_vote_percentage = float(countyvotes) / float(total_votes) *100
            county_results = (
                f"{county_name}: {county_vote_percentage:.1f}% ({countyvotes:,})\n")
            # 6d: Print the county results to the terminal.
            print(county_results)
            # 6e: Save the county votes to a text file.
            txt_file.write(county_results)
            # 6f: Write an if statement to determine the winning county and get its vote count.
            if (countyvotes > largest_turnout) and (county_vote_percentage > largest_turnout):
                largest_turnout = countyvotes
                largest_turnout = county_vote_percentage
                county_largest = county_name
                

        # 7: Print the county with the largest turnout to the terminal.
        print(largest_turnout, end="")
        # 8: Save the county with the largest turnout to a text file.
        txt_file.write(county_largest)
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the accumulator variable. ***This is above the open statement,
# because we want to set it to 0 each time we run the file***
total_votes = 0

# Candidate variables
candidate_options = []
# Declare empty dictionary to hold candidate votes
candidate_votes = {}

# 1: Create a county list and county votes dictionary.





#Declare variables for winning
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.





# Open the election results and read the file.
with open(file_to_load) as election_data:
   # Read the file object with the reader function.
   # ***file_reader is referencing the fileobject stored in memory***
    file_reader = csv.reader(election_data)

    # Read the header row (skipping it with next)
    headers = next(file_reader)

    # Print each row in the CSV file as a list.
    for row in file_reader:
        # Iterate through each row and increase accumulator. ***Shorthand for number = number + 1***
        total_votes += 1
        # Print Candidate name
        candidate_name = (row[2])

        # 3: Extract the county name from each row.


        #if uinique add candidate name to list, set votecounter to 0
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.


            # 4b: Add the existing county to the list of counties.


            # 4c: Begin tracking the county's vote count.


        # 5: Add a vote to that county's vote count.



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.

        # 6b: Retrieve the county vote count.

        # 6c: Calculate the percentage of votes for the county.


         # 6d: Print the county results to the terminal.

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.


    # 7: Print the county with the largest turnout to the terminal.


    # 8: Save the county with the largest turnout to a text file.


    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
           f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # determine winning votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

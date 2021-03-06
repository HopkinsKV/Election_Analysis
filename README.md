# Election Analysis

## Project Overview
Previously, the Colorado Board of Elections had requested the following information to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

The below information was requested to supplement the previously provided data.

6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. The county with the highest turnout


## Resources

- Data Source: [election_results.csv](https://github.com/HopkinsKV/Election_Analysis/blob/main/Resources/election_results.csv)
- Software: Python 3.7.3, Visual Studio Code 1.62.0, Atom 1.58.0

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The county results were:
  -  Jefferson County received 10.5% of the vote and 38,855 votes.
  -  Denver County received 82.8% of the vote and 306,055 votes.
  -  Arapahoe County received 6.7% of the vote and 24,801 votes.
- The county with the largest voter turnout was:
   - Denver


- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette 73.8% (272,892)



## Election-Audit Summary

The script as currently written will provide analysis of county and candidate results for an election. Adding additional result aspects, such as state or polling location, would be easy to modify by following the pattern set forth as shown here. 
![image](https://user-images.githubusercontent.com/91762315/140790657-0bf26053-e5b6-49f5-a821-debc75a4ea33.png)

Additional variables can be added with slight name modifications and repetition of the code already in place.
![image](https://user-images.githubusercontent.com/91762315/140791076-1080d8a1-ab71-42a7-9c0b-a669989377b5.png)

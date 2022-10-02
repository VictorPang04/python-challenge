# Modules
import csv
import os

# Path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")

# Defining variables
total_votes = 0
stockham_votes = 0
stockham_percent = 0
degette_votes = 0
degette_percent = 0
doane_votes = 0
doane_percent = 0

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvreader)

    # Loop through counting total votes
    for row in csvreader:
        total_votes += 1

        # If else statement to count votes
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes +=1

# Formulas to find percentage for votes
stockham_percent = (stockham_votes / total_votes) * 100
degette_percent = (degette_votes / total_votes) * 100
doane_percent = (doane_votes / total_votes) * 100

#If else statement to determine the winner based on popular vote
if stockham_votes > degette_votes and stockham_votes > doane_votes:
    winner = "Charles Casper Stockham"
elif degette_votes > stockham_votes and degette_votes > doane_votes:
    winner = "Diana DeGette"
elif doane_votes > stockham_votes and doane_votes > degette_votes:
    winner = "Raymon Anthony Doane"

# Print the results of the election
print("```text")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({stockham_votes})")
print(f"Diana DeGette: {round(degette_percent,3)}% ({degette_votes})")
print(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({doane_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
print("'''")

# Path for output file
output_file = os.path.join(".", "analysis", "election_results.txt")

# Write to the text file
with open(output_file,"w") as file:
    file.write("```text")
    file.write("\n")
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {round(stockham_percent,3)}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {round(degette_percent,3)}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {round(doane_percent,3)}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------")
    file.write("\n")
    file.write("'''")

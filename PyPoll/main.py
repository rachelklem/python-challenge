#
# 1. total number of votes cast
# 2. complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. total number of votes each candidate won
# 5. winner of the election based on popular vote


import csv

# create variables
election_file_path = "Resources\election_data.csv"
total_votes = 0
candidates = []
candidate_votes = []

# open the file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file)
    # read a row in the file
    for row in csv_file:
        # add to total votes
        total_votes += 1
        #"Ballot ID,County,Candidate"
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        # check to see if candidate exists
        if candidate not in candidates:
            # add to list if they haven't been added
            candidates.append(candidate)
            candidate_votes.append(1) #add the first vote


# done reading the file
# add to total votes
# print the results to screen
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')

print(candidates, "candidates")
print(candidate_votes)
# print the results to file

# example output
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------
# Import os module provides a way to use operating system dependent functionality. 
# The *os* and *os. path* modules include functions to interact with the file system.
# The csv module implements classes to read and write tabular data in CSV format.
import os
import csv

# Breakout the challenge into parts, each using a function to call results 
# Function header and parameters to pass a csv file, count votes, tabulate winner, and print results to screen and .txt
# Open csv and save contents to a list named data, skip header 
def open_read(path):
    with open(path) as data:
        csvreader = csv.reader(data, delimiter = ",")
        next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return (data)

# Pass data from open_read(path) function
# Create dictionary named poll and store candidate and total_vote data
def vote_count(data):
    poll = {}
    total_vote = 0
    for row in data:
        candidate = row[2]
        total_vote += 1
        if candidate in poll:
            poll[candidate] += 1
        else:
            poll[candidate] = 1
    return [poll, total_vote]

# Sum up the data, print results for each candidate and show winner
def tabulate(poll, total_vote):
    vote_count = 0
    winner = ""
    for candidate, total_vote in poll.items():
        if total_vote > vote_count:
            winner = candidate
            vote_count = total_vote
    print_winner = f"The winner is {winner} with {vote_count} votes."

    print_poll = ""
    for candidate, votes in poll.items():
        print_poll = print_poll + f"{candidate}: {votes} votes ({int(round((votes/total_vote), 2))}%)"
    
    results = f"""
    Election Results\n
    -------------------------\n
    Winner: {print_winner}\n
    -------------------------\n
    Candidates: {print_poll}\n
    -------------------------\n
    """
    return results

# Define the sequence of called functions to print, export txt  
def showresults(path):
    vote_csv = open_read(path)
    poll, total_vote = vote_count(vote_csv)
    results = tabulate(poll, total_vote)
    print(results)
      
    output_file = "output_PyPoll.txt"
    with open(output_file, 'w') as doc:
        doc.write(results)

# Run the function on the path
showresults("election_data.csv")

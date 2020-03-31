import os
import csv

def open_read(path):
    with open(path) as data:
        csvreader = csv.reader(data, delimiter = ",")
        next(csvreader)
        data = []
        for row in csvreader:
            data.append(row)
    return (data)

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
    Winner: {print_winner} \n
    -------------------------\n
    Candidates: {print_poll} \n
    -------------------------\n
    """
    return results

def showresults(path):
    vote_csv = open_read(path)
    poll, total_vote = vote_count(vote_csv)
    results = tabulate(poll, total_vote)
    print(results)
      
    output_file = "output_PyPoll.txt"
    with open(output_file, 'w') as doc:
        doc.write(results)

showresults("election_data.csv")

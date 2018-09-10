import csv
import sys

candidates = []
khanVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

with open('election_data.csv', "r", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        candidates.append(row[2])

        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        else:
            otooleyVotes += 1
            


totalVotes = len(candidates)
khanPercent = (khanVotes / totalVotes) * 100
correyPercent = (correyVotes / totalVotes) * 100
liPercent = (liVotes / totalVotes) * 100
otooleyPercent = (otooleyVotes / totalVotes) * 100

electionResults = {
    "Khan": [khanVotes],
    "Correy": [correyVotes],
    "Li": [liVotes],
    "O'Tooley": [otooleyVotes]
}

winner = max(electionResults, key=electionResults.get)

def electionSummary():
    print(
f"""
Election Results
-------------------------
Total Votes:{totalVotes}
Khan: {round(khanPercent,3)}% {khanVotes}
Correy: {round(correyPercent,3)}% {correyVotes}
Li: {round(liPercent,3)}% {liVotes}
O'Tooley: {round(otooleyPercent,3)}% {otooleyVotes}
-------------------------
Winner: {winner}
"""
    )

electionSummary()

sys.stdout = open("election_data_homework.txt", "w")
print (electionSummary())
import os
import csv

votes = 0
Khan_votes = Correy_votes = Li_votes = Tooley_votes = 0
Khan_percent = Correy_percent = Li_percent = Tooley_percent = 0

with open('election_data.csv', "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        votes += 1
        if row[2] == "Khan":
            Khan_votes += 1
        elif row[2] == "Correy":
            Correy_votes += 1
        elif row[2] == "Li":
            Li_votes += 1
        elif row[2] == "O'Tooley":
            Tooley_votes += 1

Khan_percent = (Khan_votes / votes) * 100
Correy_percent = (Correy_votes / votes) * 100
Li_percent = (Li_votes / votes) * 100
Tooley_percent = (Tooley_votes / votes) * 100

winner = max(Khan_votes,Correy_votes,Li_votes,Tooley_votes)


print("Election Results:\n---------------------------------------------")
print(f"Total votes: ({votes})\n------------------------------------------")
print(f"Khan: {round(Khan_percent,3)}% ({Khan_votes})")
print(f"Correy: {round(Correy_percent,3)}%  ({Correy_votes})")
print(f"Li: {round(Li_percent,3)}%  ({Li_votes})")
print(f"O'Tooley: {round(Tooley_percent,3)}%   ({Tooley_votes})")
print("--------------------------------")
if (winner == Khan_votes):
    winner_name = 'Khan'
    print("Winner: Khan")
if (winner == Correy_votes):
    winner_name = 'Corry'
    print("Winner: Correy")
if (winner == Li_votes):
    winner_name = "li"
    print("Winner: Li")
if (winner == Tooley_votes):
    winner_name = "O'Tooley"
    print("Winner: O'Tooley")


file_name = "py_poll.txt"
file = open(file_name,'w')

file.writelines("Election Results:\n---------------------------------------------\n")
file.writelines("Total votes: " + str(votes) + "\n------------------------------------------\n")
file.writelines("Khan: " + str(round(Khan_percent,3)) + "% " + str({Khan_votes}))
file.writelines("\nCorrey: " + str(round(Correy_percent,3)) + "% " +  str({Correy_votes}))
file.writelines("\nLi: " + str(round(Li_percent,3)) + "% " + str({Li_votes}))
file.writelines("\nO'Tooley: " + str(round(Tooley_percent,3)) + "% " + str({Tooley_votes}))
file.writelines("\n--------------------------------")
file.writelines("\nWinner: " + winner_name)








import os
import csv 

# path created to collect data from resource folder
csvpath = os.path.join("Resources", "election_data.csv")

candidate = []
results = []
votes = []
percentage = []
count_votes = 0
count_candidates = 0
unique_candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        candidate.append(row[2])
        count_votes += 1

    for x in candidate:
        if x not in unique_candidates:
            unique_candidates.append(x)


for x in set(candidate):
    results.append(x)
    votes.append(candidate.count(x))
    percentage.append((candidate.count(x)/count_votes)*100)
    count_candidates += 1

print("Election Results")
print("-----------------------------------")
print(f'Total Votes: {count_votes}')
print("-----------------------------------")
for name in unique_candidates:
    print(f'{name}: {(candidate.count(name)/(count_votes)*100):.3f}% ({candidate.count(name)})')
print("-----------------------------------")
print(f'Winner: {max(set(candidate), key= candidate.count)}')

outputpath = os.path.join("Analysis", "election_results.txt")
with open(outputpath, 'w') as textfile:
    csv_writer = csv.writer(textfile)
    textfile.write(
        "Election Results"
            "\n"
        "-----------------------------------"
            "\n"
        f'Total Votes: {count_votes}'
            "\n"
        "-----------------------------------"
            "\n")
    for name in unique_candidates:
        textfile.write(f'{name}: {(candidate.count(name)/(count_votes)*100):.3f}% ({candidate.count(name)})\n')
    textfile.write(
        "-----------------------------------"
            "\n"
        f'Winner: {max(set(candidate), key= candidate.count)}'
            "\n"
    )

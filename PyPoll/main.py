import os
import csv
import statistics
minp = []

csvpath = os.path.join("Resources", "election_data.csv")
top = []
with open(csvpath, encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    data = list(reader)
    total = len(data)

    data_1 = iter(data)
    next(data_1,) 
    col_number = len(next(data_1))
    col_sets = [set() for i in range(col_number)]

    for new_row in data:
         for col in range(col_number):
            col_sets[col].add(new_row[col])
    for row in data:
        minp.append(row[2])
    

print("Election Results ") 
print("---------------------------------")
print("Total Votes: " + str(total))
print("---------------------------------")
print(col_sets[col])
print("---------------------------------")
print("Winner: " + max(minp))
print("---------------------------------")

output_file = os.path.join("analysis", "Analysis.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

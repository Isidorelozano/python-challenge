import os
import csv 
import enum

minp= []
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    next(reader)
    data = list(reader)
    row_count = len(data)
    t = sum(float(row[1]) for row in data)
    average = t / row_count
    for row in data:
        minp.append(row[1])

    
print("Financial Analysis")    
print("----------------------------")
print("Total Months: " + str(row_count))
print("Total: " + str(t))
print("Average Change: " + str(average))
print("Greatest increase in profit: " + max(minp))
print("Greatest decrease in profit: " + min(minp))
print("----------------------------")

output_file = os.path.join("analysis", "Analysis.csv")

with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
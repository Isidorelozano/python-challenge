import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    data = list(reader)
    row_count = len(data)

    for line in reader.readlines():
        columns = line.split(",")
        value = columns[1]
        Sum += value
        print(sum)

    
    
    
    print("Total Months: " + str(row_count))

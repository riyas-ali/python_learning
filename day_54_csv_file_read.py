import csv

total = 0.0

with open("day_54_total.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total, 2)}")
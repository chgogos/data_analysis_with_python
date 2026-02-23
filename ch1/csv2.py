import csv

fn = "Google_Stock_Train (2010-2022).csv"
with open(fn, newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i >= 2:
            break

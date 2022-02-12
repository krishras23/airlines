# Be able to:
# (1) Apply the CSV techniques we covered to a dataset, such as: next(),
# (2) iterating through a data set, access headers, etc.
# (3) Explain key terms for describing CSV data.

import csv

file = open('airlines.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)

print("Header: ")
print(header)

# next() accesses the next row of the particular dataset
first = []
first = next(csvreader)
print("first: ", first)
second = []
second = next(csvreader)
print("second: ", second)
third = []
third = next(csvreader)
print("third: ", third)


# function just generalizes obtaining the header
# (column descriptors) for any table

def headingsOfTable(sheet):
    file = open(sheet)
    csvreader = csv.reader(file)
    headers = next(csvreader)
    print("Header: ", headers)


headingsOfTable('airlines.csv')


def dataOfTable(sheet):
    with open(sheet, newline='') as f:
        reader = csv.reader(f)
        records = []
        i = 0
        for row in reader:
            if i != 0:
                records.append(row)
            i = i + 1
        return records

print(dataOfTable('airlines.csv'))
import csv


def recordOfTable(sheet, rowPos):
    if rowPos == 0:
        return "The header is not a record"

    else:
        with open(sheet, newline='') as f:
            reader = csv.reader(f)
            i = 0
            for row in reader:
                if i == rowPos:
                    return row
                i = i + 1
            return "Please enter valid inputs"


print(recordOfTable('airlines.csv', 3))  # row which starts with BWI
print(recordOfTable('airlines.csv', 0))  # see 2b, part ii above
print(recordOfTable('airlines.csv', 4000))  # row which starts with SFO
print(recordOfTable('airlines.csv', 4409))  # see 2b, part iv above


def fieldOfRecord(sheet, rowPos, fieldPos):
    record = recordOfTable(sheet, rowPos)
    counter = 0
    for field in record:
        if counter == fieldPos:
            return field
        counter = counter + 1
    return "Please enter valid inputs"


print(fieldOfRecord('airlines.csv', 3, 3))  # 6
print(fieldOfRecord('airlines.csv', 3, 10))  # 78
print(fieldOfRecord('airlines.csv', 4000, 0))  # SFO
print(fieldOfRecord('airlines.csv', 4000, 1))


# San Francisco, CA: San Francisco International


def columnOfTable(sheet, colPos):
    with open(sheet, newline='') as f:
        reader = csv.reader(f)
        column = []
        for row in reader:
            pos = 0
            for field in row:
                if pos == colPos:
                    column.append(field)
                pos = pos + 1
            return column


print(columnOfTable('airlines.csv', 0))  # Airport.Code column
print(columnOfTable('airlines.csv', 1))  # Airport.Name column
print(columnOfTable('airlines.csv', 12))
# Statistics.Carriers.Total column
# Be able to:
# (1) Create helper functions to make data easier to access
# (2)  Apply the CSV techniques & main HOFs  (map, filter, reduce)
# to address different data scenarios.

import csv
from functools import reduce
from slice import columnOfTable


def column_nh(sheet, colPos):
    column = columnOfTable(sheet, colPos)
    return column[1:]


# print(column_nh('airlines.csv', 1))  # 1st entry starts with 'Atlanta'
# Airport.Name column without Airport.Code
# print(column_nh('airlines.csv', 12))  # 1st entry: '11'
# Statistics.Carriers.Total column without Statistics.Carriers.Total

def column_int(column):
    return list(map(lambda x: int(x), column))


column_yr = column_nh('airlines.csv', 5)  # stores Time.Year without header


# print(column_int(column_yr))  # 1st entry: 2003 (all vals have no quotes)

def minimum(column):
    without_header = column_nh('airlines.csv', column)
    integers = column_int(without_header)
    return reduce(lambda x, y: min(x, y), integers)


print(minimum(18))


def average(column):
    without_header = column_nh('airlines.csv', column)
    integers = column_int(without_header)
    return reduce(lambda x, y: x + y, integers) / len(integers)


print(average(12))


def total(column):
    without_header = column_nh('airlines.csv', column)
    integers = column_int(without_header)
    return len(list(filter(lambda x: x <= 300, integers)))


print(total(7))

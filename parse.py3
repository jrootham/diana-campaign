import sys, csv

dataReader = csv.reader(sys.stdin)
for row in dataReader:
    print(row[0])

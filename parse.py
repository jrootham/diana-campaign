import sys, csv, sqlite3

def getId(cursor, table, name):
    params = {"name": name}
    row = cursor.execute("SELECT rowid FROM " + table + " WHERE name=:name", params)
    return row.fetchone()[0]

def readPolls(row, cursor) :
    pollList = [""]

    for i in range(1, len(row)):
        if row[i] == "Total": 
            break
        else:
            print (row[i])
            cursor.execute("INSERT OR IGNORE INTO poll VALUES(:name)", {"name": row[i]})
            pollList.append(row[i])

    return pollList

def votes(race, row, cursor, pollList) :
    name = row[0]
    cursor.execute("INSERT INTO candidate VALUES(:name)", {"name": name})
    candidate = getId(cursor, "candidate", name)

    for i in range(1, len(pollList) - 1):
        poll = getId(cursor, "poll", pollList[i])
        data = {"race": race, "candidate": candidate, "poll": poll, "votes" :row[i]}
        cursor.execute("INSERT INTO result VALUES(:race, :candidate, :poll, :votes)", data)

if len(sys.argv) == 3 : 
    dbFile = sys.argv[1]
    race = sys.argv[2]

    connect = sqlite3.connect(dbFile, isolation_level=None)
    cursor = connect.cursor()

    dataReader = csv.reader(sys.stdin)
    for row in dataReader:
        print(row[0])
        if row[0] == "Subdivision": 
            pollList = readPolls(row, cursor)
        else:
            votes(race, row, cursor, pollList)


else :
    print("Usage: parse.py3 data.db race <input.csv")

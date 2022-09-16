import csv
import pandas as pd
times = []
start = []
finish = []
def add_column_in_csv(input, output, transform_row):
    with open(input, 'r') as roster, \
            open(output, 'w', newline='') as new_roster:
        csv_reader = csv.reader(roster)
        csv_writer = csv.writer(new_roster)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)

with open('Copy of Copy of Arana Hills Roster BU_.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('Edited_roster.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for row in csv_reader:
            if row[4] != "Arana Hills":
                if row[8] != "X":
                    if row[8] != "x":
                        if row[8] != "James":
                            del row[3:8]
                            csv_writer.writerow(row[2:4])
add_column_in_csv('Edited_roster.csv', 'James_Shifts1.csv', lambda row, line_num: row.insert(0, 'Work'))

df = pd.read_csv("James_Shifts1.csv", header=None)
df.to_csv("James_Shifts1.csv", header=["Subject", "Date", "Time"], index=False)

with open('James_Shifts1.csv', 'r') as data_file, open('James_Shifts2.csv', 'w') as outfile:
    csv_data_r = csv.reader(data_file)
    csv_data_w = csv.writer(outfile)
    next(csv_data_r)

    for line in csv_data_r:
        times.append(f"{line[2]}")
        times = [s.replace("-", "") for s in times]
        times = [s.replace(" ", "") for s in times]
        print(times)
    for line in times:
        start = line[0:line.find("m")+1]
        finish = line[line.find("m")+1:len(line)]
      




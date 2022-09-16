import csv
import pandas as pd
import ast
import numpy as np

finish = []
RawValues = []
SepValues = []
A3 = []


def add_column_in_csv(input, output, transform_row):
    with open(input, 'r') as roster, \
            open(output, 'w', newline='') as new_roster:
        csv_reader = csv.reader(roster)
        csv_writer = csv.writer(new_roster)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)


with open('Copy of Copy of Arana Hills Roster BU_QRT2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('Edited_roster.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for row in csv_reader:
            row = [s.replace(" ", "") for s in row]
            if row[1] != "Arana Hills":
                if row[4] != "Arana Hills":
                    if row[8] != "X":
                        if row[8] != "x":
                            if row[8] != "James":
                                del row[3:8]
                                RawValues.append(row[2:4])
                                csv_writer.writerow(row[2:4])
for i in RawValues:
    A1 = [i[0]]
    A2 = i[1].split('-')
    A3.append(A1 + A2)

df = pd.DataFrame(A3)
df.to_csv(r'C:\Users\Willa\OneDrive\Documents\PycharmProjects\pythonProject\DataForJames\Shifts.csv', index=False)
add_column_in_csv('Shifts.csv', 'James_Shifts.csv', lambda row, line_num: row.insert(0, 'Work'))
df = pd.read_csv("James_Shifts.csv", header=None)
df.drop(df.head(2).index, inplace=True)
df = df.iloc[:-1, :]
df.to_csv("James_Shifts1.csv", header=["Subject", "Start Date", "Start Time", "End Time"], index=False)
df = pd.read_csv("James_Shifts1.csv")
df['Start Time'] = df['Start Time'].str.upper()
df['End Time'] = df['End Time'].str.upper()
df['Start Time'] = df['Start Time'].str[:-2] + ':00 ' + df['Start Time'].str[-2:]
df['End Time'] = df['End Time'].str[:-2] + ':00 ' + df['End Time'].str[-2:]
df['End Time'].replace(to_replace='12:00 AM', value='11:59 PM', inplace=True)
df['End Time'].replace(to_replace='4:00 AM', value='4:00 PM', inplace=True)
df.to_csv("James_ShiftsQ2.csv", header=["Subject", "Start Date", "Start Time", "End Time"], index=False)
####

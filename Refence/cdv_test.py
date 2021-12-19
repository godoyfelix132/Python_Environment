import csv
import numpy as np
fields = ['Vgs', 'Vg=1', 'Vg=2', 'Vg=3', 'Vg=4', 'Vg=5', 'Vg=6', 'Vg=7', 'Vg=8']

# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

rows = zip(*rows)
filename = "../Tesis/Curves/university_records.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
import csv
import os
import shutil

a = os.listdir('./Project-s1_Files')

with open(r'persons.csv', encoding="utf-8")as file:
    
    csvFile = csv.reader(file)
    count = 0
    for lines in csvFile:
        if count == 0:
            count += 1
            continue
        else:
            os.mkdir(lines[1])
            for i in a:
                if i[0:10] == lines[0]:

                    shutil.move(f'./Project-s1_Files/{i}',lines[1])
        
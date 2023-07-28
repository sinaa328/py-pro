import csv
import os
import shutil

a = os.listdir('./1/Project-s1_Files')

with open(r'./1/Project-s1_Files/persons.csv', encoding="utf-8")as file:
    
    csvFile = csv.reader(file)
    count = 0
    for lines in csvFile:
        if count == 0:
            count += 1
            continue
        else:
            path = f"./1/{lines[1]}"
            os.mkdir(path)
            for i in a:
                if i[0:10] == lines[0]:
                    shutil.move(f'./1/Project-s1_Files/{i}',path)
                    old_name = path + '/' + i
                    new_name = path + '/' + i[11:]
                    os.rename(old_name,new_name)
                    
print('Done!')
        
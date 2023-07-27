import csv


job_titles = {}
with open(r'./2/salaries_cyber.csv', encoding='utf-8')as file:
    csvFile = csv.reader(file)
    count = 0
    for lines in csvFile:
        if count == 0:
            count += 1
        else:
            if lines[2] != 'FT':
                continue
            else:
                if lines[3] in job_titles:
                    job_titles[lines[3]][0] += int(lines[6])
                    job_titles[lines[3]][1] += 1
                else:
                    job_titles[lines[3]] = [int(lines[6]),1]

# print(job_titles)
for i in job_titles:
    print(job_titles[i][0]/job_titles[i][1])
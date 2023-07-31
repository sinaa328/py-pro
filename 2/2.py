import csv


job_titles_per_income = {}
income_per_experince = {'SE' : [0,0], 'EN' : [0,0], 'MI' : [0,0], 'EX' : [0,0]}
income_per_country = {}

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
                if lines[3] in job_titles_per_income:
                    job_titles_per_income[lines[3]][0] += int(lines[6])
                    job_titles_per_income[lines[3]][1] += 1
                else:
                    job_titles_per_income[lines[3]] = [int(lines[6]),1]

                income_per_experince[lines[1]][0] += int(lines[6])
                income_per_experince[lines[1]][1] += 1

                if lines[7] in income_per_country:
                    income_per_country[lines[7]][0] += int(lines[6])
                    income_per_country[lines[7]][1] += 1
                else:
                    income_per_country[lines[7]] = [int(lines[6]),1]

# for i in job_titles_per_income:
#     print(job_titles_per_income[i][0]/job_titles_per_income[i][1])


# print(job_titles_per_income)
# print(income_per_experince)
# print(income_per_country)

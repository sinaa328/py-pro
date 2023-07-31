import csv
import math
import heapq
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


job_titles_per_income = {}
income_per_experience = {'SE' : [0,0], 'EN' : [0,0], 'MI' : [0,0], 'EX' : [0,0]}
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

                income_per_experience[lines[1]][0] += int(lines[6])
                income_per_experience[lines[1]][1] += 1

                if lines[7] in income_per_country:
                    income_per_country[lines[7]][0] += int(lines[6])
                    income_per_country[lines[7]][1] += 1
                else:
                    income_per_country[lines[7]] = [int(lines[6]),1]

# first chart: which jobs have how much salary

first_chart_x = []
first_chart_y = []

for i in job_titles_per_income:
    first_chart_x.append(i)
    first_chart_y.append(math.floor(job_titles_per_income[i][0]/job_titles_per_income[i][1]))

plt.plot(first_chart_x, first_chart_y)

plt.show()

# second chart: how experience effect on salary

second_chart_x = []
second_chart_y = []

for i in income_per_experience:
    second_chart_x.append(i)
    second_chart_y.append(math.floor(income_per_experience[i][0]/income_per_experience[i][1]))

plt.plot(second_chart_x,second_chart_y)

plt.show()

# third chart: which country pay mor salaries

third_chart_x = []
third_chart_y = []

for i in income_per_country:
    third_chart_x.append(i)
    third_chart_y.append(math.floor(income_per_country[i][0]/income_per_country[i][1]))

top_income_per_x = []
top_income_per_y = []

for i in heapq.nlargest(5,third_chart_y):  # this loop is for find top 5 countries
    top_income_per_x.append(third_chart_x[third_chart_y.index(i)])
    top_income_per_y.append(i)

plt.plot(top_income_per_x,top_income_per_y)
plt.show

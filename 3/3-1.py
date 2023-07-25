import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv

with open('new.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    req = requests.get("https://talakar.com/#")

    soup = BeautifulSoup(req.content, "html.parser")

    news_link = soup.find_all(style="cursor: pointer;")
    b = str(news_link[0])
    c = b.split('<')
    d = c[4].split('>')
    nowtime = datetime.datetime.now()
    csv_writer.writerow([nowtime,d[1]])
    print(nowtime)
    print(d[1])


    # while True:
    #     while True:
    #         try:



            # except:
            #     continue
            # time.sleep(10)        


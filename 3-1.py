import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv

with open('new.csv', mode='w') as csv_file:
    fieldnames = ['time', 'price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    while True:
        while True:
            try:
                    req = requests.get("https://talakar.com/#")

                    soup = BeautifulSoup(req.content, "html.parser")

                    news_link = soup.find_all(style="cursor: pointer;")
                    b = str(news_link[0])
                    c = b.split('<')
                    d = c[4].split('>')
                    nowtime = datetime.datetime.now()
                    print(nowtime)
                    print(d[1])
                    writer.writeheader()
                    writer.writerow({'time' :nowtime ,'price' : d[1] })
            except:
                continue
            time.sleep(10)        


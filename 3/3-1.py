import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv
count = 0
with open('new.csv','w',encoding='utf-8',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['date and time','price'])
    
    dollor = None
    
    for count in range(50):
        try:
            req = requests.get("https://talakar.com/#")

            soup = BeautifulSoup(req.content, "html.parser")

            news_link = soup.find_all(style="cursor: pointer;")
            b = str(news_link[0])
            c = b.split('<')
            d = c[4].split('>')
            if dollor != d[1]:
                nowtime = datetime.datetime.now()
                nowtime = str(nowtime)
                csv_writer.writerow([nowtime[0:19],d[1]])
                print(nowtime[0:19])
                print(d[1])
                dollor = d[1]
                count += 1
            time.sleep(120)  
            
        except:
            continue      


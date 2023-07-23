import requests
from bs4 import BeautifulSoup
import time
    
while True:
    while True:
        try:
            req = requests.get("https://www.tgju.org/")

            soup = BeautifulSoup(req.content, "html.parser")

            news_link = soup.find_all(class_="info-price")

            print(news_link[5])
        except:
            continue
        time.sleep(10)
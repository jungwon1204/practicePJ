import requests
from bs4 import BeautifulSoup as bs

url = r"https://home.sch.ac.kr/xe/02/01.jsp"

data = requests.get(url)
data = bs(data.text, "lxml")
print(data)
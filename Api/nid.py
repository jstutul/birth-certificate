import requests
from bs4 import BeautifulSoup
import json


main_url= "https://bdris.gov.bd/br/correction"
session = requests.Session()
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

response= session.get(main_url,headers=headers)
if response.status_code != 200:
    print('Error:', response.status_code)
    exit()
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
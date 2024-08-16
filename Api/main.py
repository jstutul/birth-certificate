import requests
from bs4 import BeautifulSoup
import json

page_url = 'http://everify.bdris.gov.bd/'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
    'Accept': '*/*',
}

session = requests.Session()
page_response = requests.get(page_url, headers=headers)
page_content = page_response.text

# Check for errors
if page_response.status_code != 200:
    print('Error:', page_response.status_code)
    exit()

# Parse the login page content
soup = BeautifulSoup(page_content, 'html.parser')

captchaDeText = soup.find('input', {'name': 'CaptchaDeText'})['value']
print(captchaDeText)

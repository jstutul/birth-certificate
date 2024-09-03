import requests
from bs4 import BeautifulSoup
import json


def gettoken(session):
    response_token= session.get("http://crvs-institute.banbeis.gov.bd/students-create",headers=headers)
    if login_page_response.status_code != 200:
        print('Error:', login_page_response.status_code)
        exit()
    soup = BeautifulSoup(login_page_content, 'html.parser')
    _token = soup.find('input', {'name': '_token'})['value']
    return _token

def getniddata(session):
    token = gettoken(session)
    url = 'http://crvs-institute.banbeis.gov.bd/nid_verification_request'

    # Get cookies directly from the session
    cookies = session.cookies.get_dict()
    xsrf_token = cookies.get('XSRF-TOKEN')
    crvs_session = cookies.get('crvs_session')

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'X-CSRF-TOKEN': token,
        'X-Requested-With': 'XMLHttpRequest'
    }

    # Define the form data
    data = {
        'dataOfBirth': '1997-05-14',
        'nid10Digit': '8701665575',
        'nid17Digit': '',
        '_token': token
    }

    # print(headers)
    # print(data)
    # Send the request
    response_json = session.post(url, headers=headers, data=data, verify=False)

    # Print the response
    # print(response.status_code)
    # print(response.text)

    response_json = response_json.json()  # Parse JSON response
    return json.dumps(response_json, indent=4)


login_page_url = 'http://crvs-institute.banbeis.gov.bd/institute-login'
login_check_url = 'http://crvs-institute.banbeis.gov.bd/institute-login-check'
session = requests.Session()
login_page_response = session.get(login_page_url)
login_page_content = login_page_response.text
print(login_page_response.status_code)
# Check for errors
if login_page_response.status_code != 200:
    print('Error:', login_page_response.status_code)
    exit()
# Parse the login page content
soup = BeautifulSoup(login_page_content, 'html.parser')
# Extract the CSRF token and crvs_session
xsrf_token = soup.find('input', {'name': '_token'})['value']
# Write XSRF-TOKEN to xsrf.txt
# with open('xsrf.txt', 'w') as file:
#     file.write(xsrf_token)
# Get crvs_session from cookies
crvs_session = session.cookies.get('crvs_session')
xsrf_cookie = session.cookies.get('XSRF-TOKEN')
# Write crvs_session to crvs.txt
# with open('crvs.txt', 'w') as file:
#     file.write(crvs_session)
# Data to POST
post_data = {
    '_token': xsrf_token,
    'user': 'sksazan665@gmail.com',
    'password': 'Baba885@',
    'user_role': '2'
}
# Perform the login POST request
headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
    'Origin': 'http://crvs-institute.banbeis.gov.bd',
    'Referer': 'http://crvs-institute.banbeis.gov.bd/institute-login',
    'Accept': '*/*',
}
response = session.post(login_check_url, data=post_data, headers=headers)
# Check for errors
if response.status_code != 200:
    print('Error:', response.status_code)
else:
    print('Response:', response.text)
    # with requests.Session() as session:
        # response = send_request(session)
    niddata=getniddata(session)
    # niddata=getbirthdata(session,'19960321404045616','06','11','1996')
    print(niddata)
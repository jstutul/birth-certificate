import requests
from bs4 import BeautifulSoup
import time
import json
# URLs for login and NID verification
login_page_url_1 = 'https://idp-devsso.land.gov.bd/login'
login_url_1 = 'https://idp-devsso.land.gov.bd/login'
nid_verify_url_1_template = 'https://idp-devsso.land.gov.bd/nidverify?dob={dob}&nid={nid}'

session = requests.Session()

# First login process
def login_first_site():
    initial_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
        'Accept-Language': 'en-US',
    }

    response = session.get(login_page_url_1, headers=initial_headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': '_token'})['value']
    print('CSRF Token for First Site:', csrf_token)

    login_data = {
        '_token': csrf_token,
        'userOptionType': 'Citizen',
        'identity': 'mobile',
        'country_code': '88',
        'username': '01980290854',
        'password': 'Sazan885@'
    }

    login_headers = {
        'Host': 'idp-devsso.land.gov.bd',
        'Cache-Control': 'max-age=0',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Accept-Language': 'en-US',
        'Upgrade-Insecure-Requests': '1',
        'Origin': 'https://idp-devsso.land.gov.bd',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'Referer': 'https://idp-devsso.land.gov.bd/login',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=0, i'
    }

    login_response = session.post(login_url_1, headers=login_headers, data=login_data)
    if login_response.status_code == 200:
        print('Login successful for First Site')
        return True, session.cookies.get_dict()
    else:
        print('Login failed for First Site with status code:', login_response.status_code)
        return False, None

# Perform NID verification for the first site
def verify_nid_first_site(cookies, dob, nid):
    nid_verify_url_1 = nid_verify_url_1_template.format(dob=dob, nid=nid)
    nid_headers = {
        'Host': 'idp-devsso.land.gov.bd',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
        'Accept': '/',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'en-US',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.6478.127 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://idp-devsso.land.gov.bd/home',
        'Accept-Encoding': 'gzip, deflate, br',
        'Priority': 'u=1, i'
    }

    max_attempts = 10
    attempt = 0
    success = False
    response_data = {}

    while attempt < max_attempts and not success:
        attempt += 1
        print(f'Attempt {attempt} for NID verification (First Site)...')

        nid_response = session.get(nid_verify_url_1, headers=nid_headers, cookies=cookies)

        if nid_response.status_code == 200:
            response_data['first_site'] = nid_response.text
            print('NID verification successful for First Site')
            success = True
        elif nid_response.status_code == 500:
            print('NID verification failed with status code: 500. Retrying...')
            time.sleep(5)
        else:
            print(f'NID verification failed with status code: {nid_response.status_code}')
            success = True

    return response_data



dob = '"1997-05-14'
nid = '8701665575'
success, cookies = login_first_site()
if not success:
    print({'error': 'Login failed for first site'}), 500

first_site_data = verify_nid_first_site(cookies, dob, nid)
print(first_site_data)
#     success, csrf_token = login_second_site()
#     if not success:
#         return jsonify({'error': 'Login failed for second site'}), 500

#     second_site_data = verify_nid_second_site(csrf_token, dob, nid)

#     merged_data = {
#         'first_site': first_site_data,
#         'second_site': second_site_data
#     }

#     return jsonify(merged_data), 200

# if _name_ == '_main_':
#     app.run()
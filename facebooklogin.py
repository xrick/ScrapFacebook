from bs4 import BeautifulSoup
import requests
import re
session = requests.Session()
r = session.get('https://www.facebook.com/', allow_redirects=False)
soup = BeautifulSoup(r.text)
action_url = soup.find('form', id='login_form')['action']
inputs = soup.find('form', id='login_form').findAll('input', {'type': ['hidden', 'submit']})
post_data = {input.get('name'): input.get('value')  for input in inputs}
post_data['email'] = 'xrickliao@gmail.com'
post_data['pass'] = 'rlpwd20270528'.upper()
scripts = soup.findAll('script')
scripts_string = '/n/'.join([script.text for script in scripts])
datr_search = re.search('\["_js_datr","([^"]*)"', scripts_string, re.DOTALL)
if datr_search:
        datr = datr_search.group(1)
        cookies = {'_js_datr' : datr}
print(session.post(action_url, data=post_data, cookies=cookies, allow_redirects=False))
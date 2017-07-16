import requests
from bs4 import BeautifulSoup
import urllib3
import io
import re
import pandas as pd
from dateutil.parser import parse

'''
login to the facebook to get correct data
'''



token = "EAACEdEose0cBAAMHU7uN3T4B54shclZCOBoxqfv9XzgEfRCt0qeYDvXrT3xoxPhWVKhaY0hB35n2Fxnj0nZC46KAYRnwhDt9QZC36ZAGrLYha1p5ZBye9u00UFDNebNToZCaOvZBvkWAIcQHVU3edJU8uLREvmFT8Qs32Kr91u7KcPD56v3MVzLbvpmZApl7Tg4ZD"
uid = "653163668113554"
targetUrl = "https://graph.facebook.com/v2.9/{}?".format(uid)+"fields=name,id,link&access_token={}".format(token)
res = requests.get(targetUrl)
personalFbPage = res.json()['link']
print(personalFbPage)


'''
login to facebook

'''
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

'''
end of login to facebook
'''

pageRes = session.get(personalFbPage)
pageRes.encoding = "Big5"

wr = open('pagesrc5.txt','w')
wr.write(pageRes.content.__str__())
print(pageRes.content)

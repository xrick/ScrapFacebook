import requests
import urllib3
import io
import re
import pandas as pd
from dateutil.parser import parse



token = "EAACEdEose0cBALcnFZBqdiGAb53MfAzAXfLMeF63kQ0nedOhvIBLfH3Fnlhwz7jvVD3hcw7uRjuZBmeK0lbUMoN1ZBF4lfHZCJNPypkUaU6R3LDr5vzn5ktK2dXQDD1zmpgqZCnPmSPi9OHQul7L1pknNrciZCbbU34FZB2XNYZCIUafs2ikipSPnp7VSZArRlHcZD"
uid = "653163668113554"
targetUrl = "https://graph.facebook.com/v2.9/{}?".format(uid)+"fields=name,id,link&access_token={}".format(token)

res = requests.get(targetUrl)

personalFbPage = res.json()['link']

pageRes = (personalFbPage)
pageRes.encoding = "UTF-8"

wr = open('pagesrc2.txt','w')
wr.write(pageRes.text.__str__())
#print(pageRes.content)

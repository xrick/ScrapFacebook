##https://www.facebook.com/4think.net/
import requests
import re
import pandas as pd
from dateutil.parser import parse

# 在Facebook Graph API Exploer取得token

token = 'EAACEdEose0cBAPZC4jYBgAZBkMSFxPq99N8gB1CCPHKgB9Mc51ab0rkfx1hqGtZCUHymfA5in0Wk7VsGmOHwdhsrrOCAQSZAHRUX87rsmwk03UZAEMEYJsugsncbl8BPM8rLXZAguGpByRMPZCNefI3nZBgg7Md96iytRvunR3JBIZBJxxsACflz4E8zKKpJHr10ZD'

# 在Facebook Graph API Exploer取得粉絲專頁的id與名稱，並將其包成字典dic

siteInfo = {'1103602483088646': '4THINK'}

# 建立二個空的list

original_post_list = []
commentor_list = []

# 先在第一層使用for迴圈依序讀取粉絲頁的資訊，並使用format將id與token傳入{}裡


#res = requests.get('https://graph.facebook.com/v2.9/1103602483088646_1327094857406073?fields=comments&access_token={}'.format(token))


for ele in siteInfo:
    res1 = requests.get('https://graph.facebook.com/v2.9/{}/posts?limit=100&access_token={}'.format(ele, token))

camRex = re.compile(r'\"id\":\"\d{15}\"')

while 'paging' in res1.json():
        for information in res1.json()['data']:
            if 'message' in information:
                original_post_list.append([siteInfo[ele], information['message'], parse(information['created_time']).date(),information['id']])
                res2 = requests.get('https://graph.facebook.com/v2.9/{}?'.format(information['id'])+'fields=comments,likes&limit=30&access_token={}'.format(token))
                tmplist = camRex.findall(res2.content.__str__())
                commentor_list.append(tmplist)

        if 'next' in res1.json()['paging']:
            res1 = requests.get(res1.json()['paging']['next'])
        else:
            break

comRex2 = re.compile(r'\d{15}')
finalllist = comRex2.findall(commentor_list.__str__())
print(finalllist)
information_writer = pd.DataFrame(original_post_list, columns=['粉絲專頁', '發文內容', '發文時間','回文ID'])
information_writer.to_excel('4Think.xls', encoding="UTF-8",index=False)
information_writer2 = pd.DataFrame(finalllist, columns=['評論者id'],dtype=str)
information_writer2.to_excel('4think_data2.xls',index=False)




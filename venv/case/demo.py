
import requests,pytest
import  json
def get_token():
    url='http://219.134.240.180:51103/api/oauth/connect/token'
    data={
    "username":'admin',
    "password":'1q2w3E*',
    "grant_type":'password',
    "client_id":'vue.client'
    }
    res=requests.post(url=url,data=data)
    return res.json()['access_token']
#print(res.status_code)
# print(res.json())
# print(res.json()['access_token'])

# assert res.status_code==200
# print(res.url)
# print(res.headers)
# print(res.content)
# print(res.text)
# print   rs.headers[ ' Cache-Control'])
#assert res.headers['Cache-Control']!="private, no-cache, no-store, proxy-revalidate, no-transform"


if __name__ == '__main__':
    print(get_token())




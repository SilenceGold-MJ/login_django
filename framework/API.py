#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests,json

address,port='http://192.168.1.182','8888'

class API():

    def login_api(self,username,password):
        url = "%s:%s/login"%(address,port)
        payload = {"user_name": username, "pwd": password}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        #print(response.cookies)
        return data
    def check_user(self,username):
        url = "%s:%s/check_user"%(address,port)
        payload ={"user_name":username}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data

    def getalluser(self,number):
        url = "%s:%s/getalluser"%(address,port)
        payload ={"number":number}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data
    def Registered(self,dic):

        url = "%s:%s/Registered"%(address,port)
        payload =dic
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data

    def Updatapwd(self,username,password):
        url = "%s:%s/Updatapwd"%(address,port)
        payload = {"user_name": username, "pwd": password}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data
    def updata_info(self,dic):
        url = "%s:%s/updata_info"%(address,port)
        payload = dic
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data

    def get_user(self,username):
        url = "%s:%s/getuser"%(address,port)
        payload = {
            'username':username
        }
        headers = {}
        response = requests.request("GET", url, headers=headers, params=(payload))
        data = json.loads(response.text)
        return data



# username,password='huangpeng24','123456'
# dic={
#      'user_name':'huangpeng2',
#      'pwd': '1',
#      'realname': '阿萨德',
#      'nickname': 'ad',
#      'gender': '男',
#      'email': '',
#      'mobile': '',
#      'deleted': '0',
#      'head': 'ashdk'}
# data=API().get_user(username)
# print(data)

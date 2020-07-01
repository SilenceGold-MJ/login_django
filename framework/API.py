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
    def Registered(self,username,password):

        url = "%s:%s/Registered"%(address,port)
        payload = {"user_name": username, "pwd": password}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        data = json.loads(response.text)
        return data
# username,password='huangpeng7','123456'
# data=API().Registered(username,password)
# print(data)

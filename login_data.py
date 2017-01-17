#coding=utf8

import json

def getData():
    with open('loginData.json', encoding='utf-8') as f:
        data = json.load(f)
        # print(data)
        return data
        # print(data)
        # print(data[0]['Name'])
        # for line in data:
        #     usr = line['Name']
        #     psw = line['Pwd']
        #     # login_action.login(usr,psw)

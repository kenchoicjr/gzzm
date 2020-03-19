# -*- encoding: utf-8 -*-

import urllib.request
# import urllib2
# from urllib import urlencode
import json
import datetime

appid = 'wx3c868c4551f594de'
secret = 'ab69766cc4fffba541db0c945b5fc2cc'

gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

f = urllib.request.urlopen(gettoken)

stringjson = f.read()

access_token = json.loads(stringjson)['access_token']

# print access_token

posturl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=" + access_token

menu = '''{
     "button":[
       {
           "name":"快速查找",
           "sub_button":
           [{
               "type":"click",
               "name":"告警助手",
               "key":"123"
            },
            {
               "type":"click",
               "name":"帮助系统",
               "key":"456"
            }
            ]
       },
      {
           "name":"网站",
           "sub_button":
           [
         
            {
               "type":"view",
               "name":"正脉售后客户&工单管理系统",
               "url":"https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx3c868c4551f594de&redirect_uri=http://1u818m7919.iask.in/schools_list/&response_type=code&scope=snsapi_base&state=1#wechat_redirect"
            },
            {
               "type":"view",
               "name":"后台管理",
               "url":"http://1u818m7919.iask.in/admin/"
            }            
            ]
      },
      {
           "name":"我的",
           "sub_button":
           [{
               "type":"click",
               "name":"客户数",
               "key":"1"
            },
            {
               "type":"click",
               "name":"工单总数",
               "key":"2"
            },
            {
               "type":"click",
               "name":"预计绩效月报",
               "key":"3"
            },
            {
               "type":"click",
               "name":"待完成工单",
               "key":"4"
            }
            ]
       }]
 }'''

request = urllib.request.urlopen(posturl, menu.encode('utf-8'))

print(request.read())

# {
#     "type":"view",
#     "name":"Fox008",
#     "url": "http://www.fox008.com/analysis/listV3?"
#  },
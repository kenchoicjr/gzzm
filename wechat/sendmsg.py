# Create your views here.
# -*- coding: utf-8 -*-

import hashlib
import json
import requests
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from customerservice.models import User
import urllib.request

appid = 'wx3c868c4551f594de'
secret = 'ab69766cc4fffba541db0c945b5fc2cc'


def sendmsg(request, touser, content):
    def get_access_token():
        """
        获取微信全局接口的凭证(默认有效期俩个小时)
        如果不每天请求次数过多, 通过设置缓存即可
        """
        result = requests.get(
            url="https://api.weixin.qq.com/cgi-bin/token",
            params={
                "grant_type": "client_credential",
                "appid": appid,
                "secret": secret,
            }
        ).json()
        if result.get("access_token"):
            access_token = result.get('access_token')
        else:
            access_token = None
        return access_token

    access_token = get_access_token()

    def send_custom_msg():
        body = {
            "touser": touser,
            "msgtype": "text",
            "text": {
                "content": str(json.dumps(content, ensure_ascii=False))
            }
        }
        response = requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
            params={
                'access_token': access_token
            },
            data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        )
        # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
        result = response.json()
        print("res-------------->", response.json())
        return result

    def send_template_msg():
        """
        发送模版消息
        """
        # print(access_token*100)
        print(content)
        res = requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/template/send",
            params={
                'access_token': access_token
            },
            json={
                "touser": touser,
                "template_id": 'fjoak29eH9rrlcWm-1Q8WWnoKhKwal5AEeq3UeOJMbY',
                "data": {
                    "school": {
                        "value": content.get('school'),
                        "color": "red"
                    },
                    "terminial": {
                        "value": content.get('terminial'),
                        "color": "red"
                    },
                    "content": {
                        "value": content.get('job'),
                        "color": "red"
                    },
                    "termviewer": {
                        "value": content.get('termviewer'),
                        "color": "red"
                    },
                    "anydesk": {
                        "value": content.get('anydesk'),
                        "color": "red"
                    },
                    "contect_person": {"value": content.get('contect_person'), "color": "red"},
                    "contect_person2": {"value": content.get('contect_person2'), "color": "red"},
                }
            }
        )
        print("res-------------->", res.json())
        result = res.json()
        return result

    def send_template_msg2():
        """
        发送模版消息
        """
        # print(access_token*100)
        print(content)
        res = requests.post(
            url="https://api.weixin.qq.com/cgi-bin/message/template/send",
            params={
                'access_token': access_token
            },
            json={
                "touser": touser,
                "template_id": '96_aDizt3vTuY24R7zfecf9xEqWt78etHiNgLhVUOmM',
                "data": {

                    "remarks": {"value": content.get('remarks'), "color": "red"},

                }
            }
        )
        print("res-------------->", res.json())
        result = res.json()
        return result

    # 在这里编辑要发送的函数中的内容
    # result = send_custom_msg()
    result = send_template_msg()
    result2 = send_template_msg2()

    if result.get('errcode') == 0 and result2.get('errcode') == 0:
        return HttpResponse('发送成功')
    return HttpResponse('发送失败')

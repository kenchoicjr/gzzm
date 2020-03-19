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

gettoken = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

f = urllib.request.urlopen(gettoken)

stringjson = f.read()

access_token = json.loads(stringjson)['access_token']


# django默认开启csrf防护，这里使用@csrf_exempt去掉防护
@csrf_exempt
def weixin_main(request):
    print("-------------------------------")
    if request.method == "GET":

        # 接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # 服务器配置中的token
        token = 'gzzm'
        # 把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr.encode("utf-8")).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        othercontent = autoreply(request)

        # print(str(othercontent))
        return HttpResponse(othercontent)


# 微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET


def autoreply(request):
    try:
        webData = request.body
        xmlData = ET.fromstring(webData)
        print("*" * 10, webData)
        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgType = xmlData.find('MsgType').text
        # MsgId = xmlData.find('MsgId').text
        # Event = xmlData.find('Event').text
        # print("-" * 100, MsgType)

        toUser = FromUserName
        fromUser = ToUserName

        if msg_type == 'text':
            content = "您好,欢迎来到Python大学习!希望我们可以一起进步!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print("成功了!!!!!!!!!!!!!!!!!!!")
            print(replyMsg)
            return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'link':
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'event':
            EventKey = xmlData.find('EventKey').text
            CreateTime = xmlData.find('CreateTime').text
            Event = xmlData.find('Event').text
            if Event == 'subscribe':
                customer_detail = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=' + access_token + '&openid=' + toUser
                customerf = urllib.request.urlopen(customer_detail)
                customerjson = customerf.read()
                headimgurl = json.loads(customerjson)['headimgurl']
                # print(headimgurl)
                # access_token = json.loads(customerjson)['nickname']
                # print(type(User.objects.get(user_name=toUser)))
                suser = User.objects.filter(user_name=toUser)
                print(suser)
                if len(suser) > 0:
                    user = User.objects.filter(user_name=toUser)[0]
                else:
                    print(toUser)
                    user = User()
                    user.user_name = toUser
                    user.nick_name = json.loads(customerjson)['nickname']
                    user.headimgurl = headimgurl
                    user.password = "Gzzm" + CreateTime
                    user.loginstate = '0'
                    user.save()

                content = "地址：%s\n/用户名：%s\n密码：%s" % ("http://1u818m7919.iask.in/index/",user.user_name, user.password)
                # print(content)
                replyMsg = TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif Event == 'unsubscribe':
                user = User.objects.get(user_name=toUser)
                user.loginstate = '0'
                user.save()
                content = "用户名：%s 已禁用" % (user.nick_name)
                print(content)
                replyMsg = TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                customer_detail = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token=' + access_token + '&openid=' + toUser
                customerf = urllib.request.urlopen(customer_detail)
                customerjson = customerf.read()
                print(customerjson.decode("utf-8"))
                headimgurl = json.loads(customerjson)['headimgurl']
                print(headimgurl)
                print(toUser, CreateTime, Event)
                content = toUser, CreateTime, Event
                replyMsg = TextMsg(toUser, fromUser, content)
                return replyMsg.send()
    except Exception as e:
        print(e.args)
        return e


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text
        self.Event = xmlData.find('Event').text


import time


class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content

    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        # print(XmlForm.format(**self.__dict))
        return XmlForm.format(**self.__dict)

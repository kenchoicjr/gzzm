# Create your views here.
# -*- coding: utf-8 -*-

# import hashlib
import json
# from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render, redirect
from customerservice.models import *
from django.http import JsonResponse
import urllib.request
from datetime import datetime
from wechat.sendmsg import *
from django.core import serializers
import itertools
from django.forms.models import model_to_dict
from django.conf import settings
import logging

# 指定所用的logger
logger = logging.getLogger('log')

appid = settings.MY_APPID
secret = settings.MY_SECRET


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not callable(value):
            pr[name] = value
    return pr


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = User.objects.get(user_name=username)

    if len(username) == 0:
        request.session['errormessage'] = "请输入用户名！"
        return redirect('/index')
    if user is None:
        request.session['errormessage'] = "用户名和密码不正确!"
        return redirect('/index')

    if user.user_name == username and user.password == password and user.loginstate == 1:
        request.session['user_name'] = user.user_name
        request.session['nick_name'] = user.nick_name
        request.session['user_headimgurl'] = user.headimgurl
        request.session['user_role'] = user.role
        request.session['user_provinces'] = user.provinces
        # print(request.session['user_name'], request.session['user_headimgurl'])
        # logger.info(user,"登录了")
        logger.info(user.__str__() + "：通过网页进来了！")
        return redirect('/schools_list')
    elif user.user_name == username and user.password == password and user.loginstate == 0:
        request.session['errormessage'] = "用户名未授权!"
        return redirect('/index')
    else:
        request.session['errormessage'] = "用户名和密码不正确!"
        return redirect('/index')


@csrf_exempt
def index(request):
    return render(request, 'login.html')


def schools_list(request):
    # print(request.session.get("user_name"))
    if request.GET.get('code') is not None:
        code = request.GET.get('code')
        # print("---------------------------" + code)
        state = request.GET.get('state')
        # print(state)
        gettoken = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid=' + appid + \
                   '&secret=' + secret + '&code=' + code + '&grant_type=authorization_code'
        # print(gettoken)
        f = urllib.request.urlopen(gettoken)
        stringjson = f.read()
        openid = json.loads(stringjson)['openid']
        # print(openid)
        user = User.objects.get(user_name=openid)
        if state == '1' and user.loginstate == 1:
            request.session['user_name'] = user.user_name
            request.session['nick_name'] = user.nick_name
            request.session['user_headimgurl'] = user.headimgurl
            request.session['user_role'] = user.role
            request.session['user_provinces'] = user.provinces
            # print(request.session['user_name'], request.session['user_headimgurl'])
            logger.info(user.__str__() + "：通过微信进来了！")
            return redirect('/schools_list')
        else:
            request.session['errormessage'] = "用户未授权!"
            return redirect('/index')
    if request.session.get("user_name") is None:
        return redirect('/index')
    # schools = School.objects.all()

    user_role = request.session.get("user_role")
    user_provinces = request.session.get("user_provinces")
    # print("-" * 50, user_role, user_provinces)
    schools = School.objects.filter(province='0')
    # print(schools)
    if user_role == '管理员':
        schools = School.objects.all()
    elif user_role == '城市负责人':
        provinces = user_provinces.split(",")
        for province in provinces:
            # print(province)
            schools = schools | (School.objects.filter(province=province))

    provinces = Province.objects.all()
    context = {'schools': schools, 'provinces': provinces}
    return render(request, 'schools_list.html', context)


def order_list(request):
    user_role = request.session.get("user_role")
    user_name = request.session.get("user_name")
    user_provinces = request.session.get("user_provinces")
    user = User.objects.get(user_name=user_name)
    # print("user", user.id)
    school_id = request.GET.get('school_id')
    # print("school_id", school_id)
    school_id = school_id if school_id is not None else "0"
    if school_id == "0":
        if user_role == "管理员":
            orders = Order.objects.all()
        elif user_role == "城市负责人":
            orders = Order.objects.filter(user_id=user.id)
            # 按区域
            # for province in user.provinces:
            #     orders = orders | Order.objects.filter()
    else:
        if user_role == "管理员":
            orders = Order.objects.filter(school_id=school_id)
        elif user_role == "城市负责人":
            orders = Order.objects.filter(school_id=school_id) | Order.objects.filter(user_id=user.id)

    content = {"orders": orders}
    # print(orders)
    return render(request, 'order_list.html', content)


def logout(request):
    request.session.clear()
    return redirect('/index')


# 获得城市
def getCity(request):
    province_id = request.GET.get('province_id')
    cities = City.objects.filter(province_id=province_id)
    res = []
    for i in cities:
        res.append([i.id, i.city_name])
    # print(res)
    return JsonResponse({'cities': res})


@csrf_exempt
def schoolAdd(request):
    # print("--" * 10)

    province = Province()
    city = City()
    request.POST.get('city')
    province.id = request.POST.get('province')
    city.id = request.POST.get('city')
    school = School()
    school.school_name = request.POST.get('school_name')
    school.province = province
    school.city = city
    school.address = request.POST.get('address')
    school.contect_person = request.POST.get('contect_person')
    school.project_nature = request.POST.get('project_nature') if request.POST.get(
        'project_nature') is not None else "0"
    # school.software_period = request.POST.get('software_period')
    school.software_period = datetime.strptime(request.POST.get('software_period'), '%m/%d/%Y').strftime('%Y-%m-%d')
    school.save()
    return redirect('/schools_list')
    # return HttpResponse(school.project_nature)


@csrf_exempt
def schoolEditSave(request):
    # print("--" * 10)
    # print("--" * 10, request.POST.get("school_id"))
    school_id = request.POST.get("school_id")
    school = School.objects.get(id=school_id)
    province = Province()
    city = City()
    request.POST.get('city')
    province.id = request.POST.get('province')
    city.id = request.POST.get('city')

    school.school_name = request.POST.get('school_name')
    school.province = province
    school.city = city
    school.address = request.POST.get('address')
    school.contect_person = request.POST.get('contect_person')
    school.project_nature = request.POST.get('project_nature') if request.POST.get(
        'project_nature') is not None else "0"
    # school.software_period = request.POST.get('software_period')
    school.software_period = request.POST.get('software_period')
    school.save()
    return redirect('/schools_list')


@csrf_exempt
def schoolEdit(request):
    # print(request.POST.get('id'))
    school = School.objects.get(id=request.POST.get('id'))
    cities = City.objects.filter(province_id=school.province.id)
    list = ["school", school]
    res2 = []
    for i in cities:
        res2.append([i.id, i.city_name])
    res = [school.school_name, school.province.id, school.city.id, school.address, school.contect_person,
           school.project_nature, school.software_period, school.id]
    # print(res)
    # 发送消息
    # print(sendmsg(request))

    return JsonResponse({'school': res, 'cities': res2}, safe=False, json_dumps_params={'ensure_ascii': False})
    # return redirect('/schools_list')


def terminial_list(request, id):
    # print(id)
    school = School.objects.get(id=id)
    user_role = request.session.get("user_role")
    user_provinces = request.session.get("user_provinces")
    schools = School.objects.filter(province='0')
    if user_role == '管理员':
        schools = School.objects.all()
    elif user_role == '城市负责人':
        provinces = user_provinces.split(",")
        for province in provinces:
            # print(province)
            schools = schools | (School.objects.filter(province=province))

    # print(school)
    terminial_list = Terminial.objects.filter(school=school)
    # print(terminial_list)
    printers = Printer.objects.all()
    terminialTypes = TerminialType.objects.all()
    wiscards = Wiscard.objects.all()
    schools_all = []
    for i in schools:
        # print(i.school_name)
        schools_all.append(i.school_name)
    schoolJson = json.dumps(schools_all, ensure_ascii=False)
    # print(schoolJson)
    context = {"school": school, "terminials": terminial_list, "printers": printers, "terminialTypes": terminialTypes,
               "wiscards": wiscards, "schools": schoolJson}
    return render(request, 'terminial_list.html', context)


@csrf_exempt
def terminialAdd(request):
    school_name = request.POST.get('school_name')
    school_id = request.POST.get('school_id')
    # terminial_type = TerminialType.objects.filter(terminial_type=request.POST.get('terminial_type'))

    # print(school_name, school_id)
    terminial = Terminial()
    terminial.terminial_name = request.POST.get('terminial_name')
    terminial.teamviewerid = request.POST.get('teamviewerid')
    terminial.anydeskid = request.POST.get('anydeskid')
    terminial.hardware_period = datetime.strptime(request.POST.get('hardware_period'), '%m/%d/%Y').strftime('%Y-%m-%d')
    terminial.address = request.POST.get('address')
    terminial.contect_person = request.POST.get('contect_person')
    terminial.contect_person2 = request.POST.get('contect_person2')
    terminial.remarks = request.POST.get('remarks')
    terminial.printer_id = request.POST.get('printer')
    terminial.school_id = request.POST.get('school_id')
    terminial.terminial_type_id = request.POST.get('terminial_type')
    terminial.wiscard_id = request.POST.get('wiscard_name')
    terminial.save()
    return redirect('/terminial_list/' + terminial.school_id)
    # return HttpResponse(school_name,school_id,terminial_type)


@csrf_exempt
def terminialEditSave(request):
    id = request.POST.get('id')
    terminial = Terminial.objects.get(id=id)
    terminial.terminial_name = request.POST.get('terminial_name')
    terminial.teamviewerid = request.POST.get('teamviewerid')
    # print(terminial.teamviewerid)
    terminial.anydeskid = request.POST.get('anydeskid')
    terminial.hardware_period = request.POST.get('hardware_period')
    terminial.address = request.POST.get('address')
    terminial.contect_person = request.POST.get('contect_person')
    terminial.contect_person2 = request.POST.get('contect_person2')
    terminial.remarks = request.POST.get('remarks')
    terminial.printer_id = request.POST.get('printer')
    terminial.school_id = request.POST.get('school_id')
    terminial.terminial_type_id = request.POST.get('terminial_type')
    terminial.wiscard_id = request.POST.get('wiscard_name')
    terminial.save()
    return redirect('/terminial_list/' + terminial.school_id)


@csrf_exempt
def terminialEdit(request):
    # print(request.POST.get('id'))
    terminial = Terminial.objects.get(id=request.POST.get('id'))
    # cities = City.objects.filter(province_id=terminial.province.id)
    # list = ["school",terminial]
    wiscards = Wiscard.objects.all()
    school = School.objects.get(id=terminial.school.id)
    # res = []
    # terminialJson = json.dumps(terminial, ensure_ascii=False)
    res = [terminial.terminial_name, terminial.teamviewerid, terminial.anydeskid, terminial.hardware_period,
           terminial.contect_person,
           terminial.contect_person2, terminial.remarks, terminial.printer_id, school.school_name,
           terminial.terminial_type_id, terminial.wiscard_id, terminial.address, terminial.id]
    # 发送消息
    # print(sendmsg(request))
    res2 = []
    for i in wiscards:
        res2.append([i.id, i.wiscard_name])
    # terminialJson = serializers.serialize("json", terminial)
    # print(res)
    return JsonResponse({'terminial': res, 'wiscard': res2}, safe=False, json_dumps_params={'ensure_ascii': False})
    # return redirect('/schools_list')


@csrf_exempt
def order_edit(request):
    # print(request.POST.get('id'))
    order = Order.objects.get(id=request.POST.get('id'))
    status = Status.objects.all()
    classification = Classification.objects.all()
    users = User.objects.all()
    order_type = OrderType.objects.all()
    schools = School.objects.all()
    res2 = []
    for i in users:
        res2.append([i.id, i.nick_name])

    res3 = []
    for i in status:
        res3.append([i.id, i.status_name])
    res4 = []
    for i in order_type:
        res4.append([i.id, i.order_type, i.value])

    res5 = []
    for i in classification:
        res5.append([i.id, i.classification])
    order_type_id = order.order_type.id if order.order_type.id is not None else 0
    res = [order.school.school_name, order.terminial.terminial_name, order.job, order.user.id, order.status.id,
           order.classification.id, order_type_id, order.value1, order.value2, order.remarks, order.id]
    content = {'orders': res, 'status': res3, 'classification': res5, 'users': res2, 'order_type': res4,
               'user_role': request.session.get("user_role")}
    # print(content)
    return JsonResponse(content,
                        safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def order_add(request):
    user_role = request.session.get("user_role")
    user_provinces = request.session.get("user_provinces")
    schools = School.objects.filter(province='0')
    if user_role == '管理员':
        schools = School.objects.all()
    elif user_role == '城市负责人':
        provinces = user_provinces.split(",")
        for province in provinces:
            # print(province)
            schools = schools | (School.objects.filter(province=province))

    schools_all = []
    for i in schools:
        schools_all.append(i.school_name)
    schoolJson = json.dumps(schools_all, ensure_ascii=False)
    status = Status.objects.all()
    classification = Classification.objects.all()
    user_role = request.session.get("user_role")
    user_name = request.session.get("user_name")
    if user_role == "管理员":
        users = User.objects.all()
    elif user_role == "城市负责人":
        users = User.objects.filter(user_name=user_name)
    # users = User.objects.all()
    order_type = OrderType.objects.all()
    res2 = []
    for i in users:
        res2.append([i.id, i.nick_name])
    res3 = []
    for i in status:
        res3.append([i.id, i.status_name])
    res4 = []
    for i in order_type:
        # pass
        res4.append([i.id, i.order_type, i.value])
    res5 = []
    for i in classification:
        res5.append([i.id, i.classification])
    content = {'schoolJson': schoolJson, 'status': res3, 'classification': res5, 'users': res2, 'order_type': res4,
               'schoolJson': schoolJson, 'user_role': request.session.get("user_role")}
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def order_add_save(request):
    school_name = request.POST.get('school_name')
    order = Order()
    order.school = School.objects.get(school_name=school_name)
    terminial_namea = request.POST.get('terminial_namea')
    # print(terminial_namea)
    order.terminial = Terminial.objects.get(id=terminial_namea)
    order.job = request.POST.get('job')
    classification = request.POST.get('classification')

    order.classification = Classification.objects.get(id=classification)
    if order.classification.id == 1:
        order.order_type = OrderType.objects.get(id=request.POST.get('order_type_name'))
    else:
        order.order_type = OrderType.objects.get(id=request.POST.get('order_type_name'))
    userid = request.POST.get('user')
    order.user = User.objects.get(id=userid)
    order.status = Status.objects.get(id=request.POST.get("status"))
    order.create_date = datetime.now().strftime('%Y-%m-%d')
    if request.POST.get("status") == "2":
        order.comleted_date = datetime.now().strftime('%Y-%m-%d')
        # print(order.comleted_date)
    order.value1 = request.POST.get('value1')
    order.value2 = request.POST.get('value2')
    order.remarks = request.POST.get('remarks')
    order.save()
    termviewer = order.terminial.teamviewerid
    anydesk = order.terminial.anydeskid
    contect_person = order.terminial.contect_person
    contect_person2 = order.terminial.contect_person2
    remarks = order.terminial.remarks
    content = {'job': order.job, 'school': school_name, 'terminial': order.terminial.terminial_name,
               'termviewer': termviewer,
               'anydesk': anydesk, 'contect_person': contect_person, 'contect_person2': contect_person2,
               'remarks': remarks}
    user_name = request.session.get("user_name")
    if order.user.user_name != user_name:
        print(sendmsg(request, order.user.user_name, content))
    return redirect("/order_list")


@csrf_exempt
def termail_a(request):
    school = School.objects.get(school_name=request.POST.get('school_name'))
    # print(school)
    termail = Terminial.objects.filter(school=school)
    termail_a = []
    for i in termail:
        termail_a.append([i.id, i.terminial_name])
    content = {'termailJson': termail_a}
    # print(termail_a)
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def classification_a(request):
    classification = Classification.objects.get(id=request.POST.get('classification'))
    # print(classification)
    order_type = OrderType.objects.filter(classification=classification)
    classification = []
    for i in order_type:
        classification.append([i.id, i.order_type])
    content = {'classificationJson': classification}
    # print(classification)
    return JsonResponse(content, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def order_edit_save(request):
    order = Order.objects.get(id=request.POST.get("orderide"))
    if request.POST.get("statuse") == "2":
        order.comleted_date = datetime.now().strftime('%Y-%m-%d')
        # print(order.comleted_date)
    order.status = Status.objects.get(id=request.POST.get("statuse"))
    order.school = School.objects.get(school_name=request.POST.get("school_namee"))
    order.terminial = Terminial.objects.get(terminial_name=request.POST.get("terminial_namee"))
    order.classification = Classification.objects.get(id=request.POST.get("classificatione"))
    if order.classification.id == 1:
        order.order_type = OrderType.objects.get(id=request.POST.get('order_type_namee'))
    else:
        order.order_type = OrderType.objects.get(id=request.POST.get('order_type_namee'))
    order.job = request.POST.get("jobe")
    order.value1 = request.POST.get("value1e")
    order.value2 = request.POST.get("value2e")
    order.remarks = request.POST.get("remarkse")
    order.order_type_name = request.POST.get("order_type_namee")
    # $("input[name='jobe']").val(data.orders[2]);
    # $("select[name='usere']").val(data.orders[3]).attr("selected", true);
    # $("select[name='statuse']").val(data.orders[4]).attr("selected", true);
    # $("select[name='classificatione']").val(data.orders[5]).attr("selected", true);
    # $("select[name='order_type_namee']").val(data.orders[6]).attr("selected", true);
    # $("select[name='order_type_valuee']").val(data.orders[6]).attr("selected", true);
    # $("input[name='value1e']").val(data.orders[7]);
    # $("input[name='value2e']").val(data.orders[8]);
    # $("textarea[name='remarkse']").val(data.orders[9]);
    # $("input[name='orderide']").val(data.orders[10]);
    order.save()
    return redirect("/order_list")

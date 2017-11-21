from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.context_processors import csrf
import xlrd, xlwt, time
import csv
import math
import os

dataFromFile = []

def index(request):
    return secureRender(request, "index.html", {
        "accounts": 'abc'
    })

def organizationList(request):
    reader = dataSource()
    count = 6
    page = math.ceil(len(reader) * 1.0 / count)
    try:
        int(request.GET.get("start", 1))
        start = int(request.GET.get("start", 1))
        if (start <= 0) | (start > page):
            start = 1
    except:
        print(request.GET.get("start", 1))
        start = 1
    # start = int(request.GET.get("start", 1))
    print(start)
    print('start: {0}'.format(start))
    sourceData = []
    itemData = []

    max_number = min(len(reader), (start-1) * (count) + count)
    j = 0
    for i in range((start-1) * count, max_number):
        itemData.append(reader[i])
        if ((j % 2 == 1) | (i == len(reader) - 1)):
            sourceData.append(itemData.copy())
            itemData = []
        j += 1

    return secureRender(request, "list.html", {
        "sourceData": sourceData,
        "page": page,
        "start": start,
        "prevStart": start - 1 if start >= 2 else None,
        "nextStart": start + 1 if start <= page-1 else None
    })

def organizationDetail(request, userId):
    organization = dataWithId(userId)
    return secureRender(request, "details.html", {
        "organization": organization
    })

def dataSource():
    global  dataFromFile
    if len(dataFromFile) == 0:
        data =  BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        data = os.path.join(data, 'static', 'data.csv')
        with open(data, 'rt', newline='', encoding='utf-8') as f:
            source = list(csv.reader(f))
            for organization in source:
                sourceDic = {}
                sourceDic['id'] = organization[0]
                sourceDic['name'] = organization[1]
                sourceDic['address'] = organization[2]
                sourceDic['phone'] = organization[3]
                sourceDic['website'] = organization[4]
                sourceDic['product'] = organization[5]
                sourceDic['customer'] = organization[6]
                sourceDic['detail'] = organization[7]
                sourceDic['charge'] = organization[8]
                sourceDic['destionation'] = organization[9]
                sourceDic['count'] = organization[10]
                sourceDic['brief'] = organization[11]
                sourceDic['country'] = organization[12]
                sourceDic['city'] = organization[13]
                sourceDic['logo'] = organization[14]
                sourceDic['wechat'] = organization[15]
                dataFromFile.append(sourceDic)
    return dataFromFile

def dataWithId(Id):
    datas = dataSource()
    for data in datas:
        if data['id'] == Id:
            return data

def secureRender(request, template, dic, userContext=True):
    dic.update(csrf(request))
    if userContext:
        return render_to_response(template, dic, RequestContext(request))
    else:
        return render_to_response(template, dic)

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:16:52 2020

@author: HYSEO
"""

# api/database.py
import datetime
import requests
import json

from mongoengine import connect
from api.models import (FinanceItemModel, UserFinanceItemModel)
from pandas.io.json import _json_normalize

MONGO_DATABASE = "graphql-example"
MONGO_HOST = "mongomock://localhost"

# Database 연결
conn = connect(MONGO_DATABASE, host=MONGO_HOST, alias="default")
print(conn.server_info())


def init_db():
    url = "https://finance.naver.com/api/sise/etfItemList.nhn"
    json_data = json.loads(requests.get(url).text)
    df = _json_normalize(json_data['result']['etfItemList'])

    for loc in range(len(df.index)):
        local = df.loc[loc]
        FinanceItemModel(
            code=local["itemcode"],
            name=local["itemname"],
            value=local["nowVal"],
            updDttm=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        ).save()

    UserFinanceItemModel(
        userId=0,
        code="069500",
        value=20000,
        count=100
    ).save()
    UserFinanceItemModel(
        userId=0,
        code="229200",
        value=10000,
        count=50
    ).save()


def financeItemlists():
    lists = FinanceItemModel.objects()
    json_data = lists.to_json()
    return json.loads(json_data)

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 23:01:28 2020

@author: HYSEO
"""

from mongoengine import Document
from mongoengine.fields import (StringField, IntField)


class FinanceItemModel(Document):
    meta = {
        "collection": "financeItems"
    }
    code = StringField()
    name = StringField()
    value = IntField()
    updDttm = StringField()


class UserFinanceItemModel(Document):
    meta = {
        "collection": "userFinanceItems"
    }
    userId = IntField()
    code = StringField()
    value = IntField()
    count = IntField()
    updDttm = StringField()
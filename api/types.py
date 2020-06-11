# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:37:50 2020

@author: HYSEO
"""

import datetime

from graphene import relay
from graphene_mongo import MongoengineObjectType

from api.models import (FinanceItemModel, UserFinanceItemModel)


# Schema Type
class FinanceItemType(MongoengineObjectType):
    class Meta:
        model = FinanceItemModel

    # resolve updDttm
    def resolve_upd_dttm(parent, info, **input):
        return datetime.strptime(parent.updDttm, "%Y%m%d%H%M%S").strftime("%Y-%m-%d %H:%M:%S")


class FinanceItemConnection(relay.Connection):
    class Meta:
        node = FinanceItemType


class FinanceItemConnectionType(MongoengineObjectType):
    class Meta:
        model = FinanceItemModel
        interfaces = (relay.Node,)
        connection_class = FinanceItemConnection


class UserFinanceItemType(MongoengineObjectType):
    class Meta:
        model = UserFinanceItemModel


class FinanceItemConnection(relay.Connection):
    class Meta:
        node = UserFinanceItemType


class UserFinanceItemConnectionType(MongoengineObjectType):
    class Meta:
        model = UserFinanceItemModel
        interfaces = (relay.Node,)
        connection_class = FinanceItemConnection

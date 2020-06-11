# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:04:19 2020

@author: HYSEO
"""

import graphene

from graphene_mongo import MongoengineConnectionField
from .types import (FinanceItemConnectionType, UserFinanceItemConnectionType)

"""
class InputPagination(graphene.InputObjectType):
    page = graphene.Int(default_value = 1)
    count_for_rows = graphene.Int(default_value = 10)
"""

class Query(graphene.ObjectType):

    finance_item_edges = MongoengineConnectionField(FinanceItemConnectionType)
    user_finance_item_edges = MongoengineConnectionField(UserFinanceItemConnectionType)
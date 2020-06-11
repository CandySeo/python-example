# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:17:43 2020

@author: HYSEO
"""

import graphene

from .types import FinanceItemType
from .query import Query


# Schema 생성
schema = graphene.Schema(
    query=Query,
    types=[
        FinanceItemType
    ]
)
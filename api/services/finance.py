# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 19:50:07 2020

@author: HYSEO
"""


import json

from api.models import FinanceItemModel


class FinanceService():

    def getFinanceItemByCode(code):
    
        item = FinanceItemModel.objects(code=code)
        
        if item is not None:
            json_data = item.to_json()
            dicts = json.loads(json_data)
            
            print(dicts)
            return dicts
        else:
            return None
        
        
        
        
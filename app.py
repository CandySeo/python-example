# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:28:26 2020

@author: HYSEO
"""

import dotenv

from flask import render_template
from api import create_app
from api.database import (
        init_db, financeItemlists
    )
from api.services.finance import (
        FinanceService
    )
    
init_db()
app = create_app()    
   
       

@app.route('/index')
def index():
    return render_template(
        'index.html',
        title = 'Flask Template Test',
        home_str = 'Hello Flask!',
        home_list = [1, 2, 3, 4, 5]
    )


@app.route('/info')
def info():
    return render_template('info.html')



@app.route('/')
@app.route('/financeitem')
def financeitem():
      
    return render_template(
        'financeitem.html',
        lists = financeItemlists()
    )

@app.route('/financeitem/<code>')
def getFinanceItem(code):

    print("Code[%s] get a finance item." % code)
    
    lists = list()
    lists.append(FinanceService.getFinanceItemByCode(code))
        
    return render_template(
        'financeitem.html',
        lists = lists
        )
    
    

if __name__ == '__main__':
    dotenv.load_dotenv(dotenv_path=".env")
    
    app.run(host="localhost", port=3000)
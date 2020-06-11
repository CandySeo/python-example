# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:16:21 2020

@author: HYSEO
"""


from flask import Flask
from flask_graphql import GraphQLView
from api.schema import schema


def create_app():
    # Create to Flask Application
    app = Flask(__name__)
    
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )
    
    return app

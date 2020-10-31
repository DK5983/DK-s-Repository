#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 11:53:56 2020

@author: dk
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Run this flask app within a Docker file!"
if __name__ == "__main__":
app.run()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:53:01 2020

@author: clara
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('sample2.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])


app.run(debug=True, use_reloader=False)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 00:53:01 2020

@author: clara
"""
from flask import Flask, render_template, request
import os
from main import complete_function, compta_buits

app = Flask(__name__)


# final_state = main.complete_function(image_path)

# final_state = [[1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
# [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
# [1, 1, 1, 1, 'X', 'X', 'X', 1, 1, 1, 1, 1, 1, 1],
# [1, 1, 1, 0, 1, 'X', 'X', 'X', 'X', 1, 1, 1, 1, 1, 1],
# [1, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 1, 1, 1]]



@app.route("/form")
def form():
    files=os.listdir("resources")
    return render_template('form.html', files=files)

@app.route("/", methods = ["GET", "POST"])
def template_test():
    select = request.form.get('comp_select')
    print(select)
    final_state = complete_function("resources/" + select)
    buits=compta_buits(final_state)
    return render_template('sample.html', final_state=final_state, buits=buits, select=select)


app.run(debug=True, use_reloader=False)
from flask import Flask, render_template
import random

from flask.wrappers import Request
from werkzeug.wrappers import request
app=Flask(__name__)


@app.route("/")
def hello():
    return render_template( "index.html")  

@app.route("/validate")
def validate():
    num1=Request.form("start")
    num2=Request.form("End")
    answer=Request.form("num")
    for i in random.randrange(num1,num2):
        if answer>i:
            pass

    
    
app.run()
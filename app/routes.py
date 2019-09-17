from app import app
from flask import render_template, request
from app.models import model, formopener
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/results', methods = ['GET', 'POST'])
def results():
    data = dict(request.form)
    print(userdata)
    userdata = eval(json.dumps(data))
    nickname = userdata['nickname']
    print(userdata['nickname'])
    output = model.shout(userdata['nickname'])
    print(output)
    return render_template('results.html')

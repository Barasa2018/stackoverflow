import flask
from flask import request,jsonify,abort,datetime

app = flask.Flask('__name__')
app.config['DEBUG'] = True

@app.route('/app/api/v1/questions',methods=['POST'])
def createQuis():
    question = {'title':request.json['title'],
                'description':request.json['description'],
                'date':datetime.datetime.now()}

    questions.append(question)

app.run()
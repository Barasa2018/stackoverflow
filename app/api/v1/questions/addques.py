import flask
from flask import request,jsonify,abort
from datetime import datetime

app = flask.Flask('__name__')
app.config['DEBUG'] = True

questions = [{'title':'Flask post method not allowed',
            'description':'I am trying to test my api endpoint for posting a question and its returning error 405, please help',
            'date':datetime.now()}]

@app.route('/app/api/v1/questions',methods=['POST'])
def createQuis():
    question = {'title':request.json['title'],
                'description':request.json['description'],
                'date':datetime.now()}

    questions.append(question)
    return jsonify(questions)

app.run()
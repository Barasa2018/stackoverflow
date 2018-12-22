import flask
from flask import request,jsonify

app = flask.Flask('__name__')
app.config['DEBUG'] = True

#add dummy questions
questions = [{'id':1,
            'What is computer science ?':'posted by Charles'},
            {'id':2,
            'Explain the importance of the Big O notation in computer science':'posted ny Ann'},
            {'id':3,
            'Define the term Algorithm':'posted by Goodwill'}]

@app.route('app/api/v1/questions/<question_id>',methods=['GET'])
def showUser(question_id):

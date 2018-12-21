import flask
from flask import request,jsonify
from datetime import datetime

app = flask.Flask('__name__')
app.config['DEBUG'] = True

#add some dumpy questions

questions = [{'Q.':'What are data structures ?','Posted by':'Gilly','time':datetime.now().strftime('%Y-%m-%dT%H:%M:%S')},
            {'Q.':'What is an algorithm ?','Posted by':'Mercy','time':datetime.now().strftime('%Y-%m-%dT%H:%M:%S')},
            {'Q.':'Define OOP ?','Posted by':'Gilly','time':datetime.now().strftime('%Y-%m-%dT%H:%M:%S')},]

@app.route('/app/api/v1/questions',methods=['GET'])
def showQuestions():
    return jsonify(questions)

app.run()
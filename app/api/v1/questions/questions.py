import flask
from flask import request,jsonify,abort,make_response

app = flask.Flask('__name__')
app.config['DEBUG'] = True

#add dummy questions
questions = [{'id':1,
            'What is computer science ?':'posted by Charles'},
            {'id':2,
            'Explain the importance of the Big O notation in computer science':'posted ny Ann'},
            {'id':3,
            'Define the term Algorithm':'posted by Goodwill'}]

@app.route('/app/api/v1/questions/<int:question_id>',methods=['GET'])
def showUser(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify(question[0])

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'The question was Not found !'}), 404)

app.run()
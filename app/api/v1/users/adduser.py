import flask
from flask import request,jsonify,abort

app = flask.Flask('__name__')
app.config['DEBUG'] = True

users = [{'id':1,
        'name':'jane',
        'email':'jane@testmail.com'}]

@app.route('/app/api/v1/users', methods=['post'])
def addUser():
    # user = ({'name': 'cornelius'});
    # return jsonify(request.json), 200;
    if not request.json:
        abort(400)
    user = {'id':users[-1]['id']+1,
            'name':request.json['name'],
            'email':request.json.get('email')
            }

    users.append(user)
    return jsonify(users),201

app.run()
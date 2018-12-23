import flask
from flask import request,jsonify,make_response

app = flask.Flask('__name__')
app.config['DEBUG'] = True

@app.route('/app/api/v1/users',methods=['POST'])
def addUser():
    user = {'id':user[-1]['id']+1,
            'title':request.json('title'),
            'description':request.json.get('description')}

    user.append(user)
    return jsonify(user)

app.run
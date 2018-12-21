import flask
from flask import request,jsonify

app = flask.Flask('__name__')
app.config['DEBUG'] = True

#add dumpy users for trial

users = [{'name':'Barasa','email':'barasa@gmail.com'},
        {'name':'Joan','email':'joan@domain.com'},
        {'name':'Ben','email':'ben@testmail.com'}]

@app.route('/app/api/v1/users',methods=['GET'])
def showUsers():
    return jsonify(users)

app.run()
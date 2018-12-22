import flask
from flask import request,jsonify

app = flask.Flask('__name__')
app.config['DEBUG'] = True

#add dummy users
users = [{'id':1,'name':'jackie','email':'jackie@mariba.com'},
        {'id':2,'name':'Antony','email':'anto@domain.com'},
        {'id':3,'name':'Ali','email':'ali@mindyourlanguage.com'},]

@app.route('/app/api/v1/users',methods=['GET'])
def showUsers():
    return jsonify(users)

app.run()
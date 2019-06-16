import os
from flask import Flask, render_template,request,redirect,url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = 'secret'

mongo = PyMongo(app)

@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html', user=mongo.db.mydb.find())


@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/find')
def find():

    return render_template('find.html')

@app.route('/delete')
def delete():
 
    return render_template('delete.html')




if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
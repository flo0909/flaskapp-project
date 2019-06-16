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


@app.route('/add', methods=['GET', 'POST'])
def add():
    user = mongo.db.users
    if request.method == 'POST':
        Recipe_name = request.form['Recipe_name']
        user.insert_one({'Recipe_name': Recipe_name})
    return render_template('add.html')

@app.route('/find')
def find():
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()
    
    return render_template('find.html',user2=user2,user3=user3, user=user)



@app.route('/delete', methods=['GET', 'POST'])
def delete():
    user = mongo.db.users
    if request.method == 'POST':
        Recipe_name = request.form['Recipe_name']
        user.delete_one({'Recipe_name': Recipe_name})
        return redirect(url_for('find'))
    return render_template('delete.html')

@app.route('/sort')
def sort():
    user = mongo.db.users
    sort_results=''
    return render_template('sort.html', user=user, sort_results=sort_results)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
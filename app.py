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
        Suitable_for = request.form['Suitable_for']
        Serves_as = request.form['Serves_as']
        Allergens = request.form['Allergens']
        Portions_served = request.form['Portions_served']

        Ingredients = request.form['Ingredients']
        user.insert_one(
            {
                'Recipe_name': Recipe_name ,
                'Details':{
                    'Suitable_for': Suitable_for ,
                    'Serves_as': Serves_as ,
                    'Allergens': Allergens ,
                    'Portions_served': Portions_served,
                },
                'Ingredients': [Ingredients]
                }
                )
        return redirect(url_for('find'))
    return render_template('add.html')

@app.route('/find')
def find():
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()
    
    return render_template('find.html',user2=user2,user3=user3, user=user)



@app.route('/update/')
@app.route('/update/<name>', methods=['GET','POST'])
def update(name):
   
    user = mongo.db.users
    Recipe_name = ''
    user4 = ''
    u_recipe=''
    u_ingr=''
    u_suitablefor=''
    u_servesas=''
    u_allergens=''
    u_portions_served=''

    if request.method == 'POST':
        Recipe_name = request.form['u_recipe']
        Suitable_for = request.form['u_suitablefor'] 
        Serves_as = request.form['u_servesas']
        Allergens = request.form['u_allergens']   
        Portions_served = request.form['u_portions_served'] 

        Ingredients = request.form['u_ingr']   

        user.update({'Recipe_name':name } , {'$set':{'Recipe_name': Recipe_name}})
        user.update({'Recipe_name':name } , {'$set':{'Details':{ 'Suitable_for': Suitable_for } }})
        user.update({'Recipe_name':name } , {'$set':{'Details':{ 'Serves_as': Serves_as } }})
        user.update({'Recipe_name':name } , {'$set':{'Details':{ 'Allergens': Allergens } }})
        user.update({'Recipe_name':name } , {'$set':{'Details':{ 'Portions_served': Portions_served } }})

        user.update({ 'Recipe_name':Recipe_name} , {'$set':{'Ingredients': [Ingredients]}})
        return redirect(url_for('find'))
    return render_template('update.html', u_portions_served=u_portions_served ,u_allergens=u_allergens  , u_servesas=u_servesas , u_suitablefor=u_suitablefor  ,u_recipe=u_recipe, name=name, Recipe_name=Recipe_name, user=user, user4=user4, Ingredients=Ingredients,u_ingr=u_ingr )


@app.route('/results/')
@app.route('/results/<name>')
def results(name=None):
    users = mongo.db
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()  
    return render_template('results.html', name=name, user2=user2, user3=user3, user=user, users=users)


@app.route('/recipe/')
@app.route('/recipe/<name>', methods=['GET','POST'])
def recipe(name=None):
    users = mongo.db
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()
    user4 = ''
    if request.method == 'GET':
        user4=user.delete_one({'Recipe_name': name})
        return render_template('find.html')
    return render_template('recipe.html', name=name, user2=user2, user3=user3, user=user, users=users, user4=user4)


@app.route('/sort')
def sort():
    user = mongo.db.users
    sort_results=''
    return render_template('sort.html', user=user, sort_results=sort_results)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
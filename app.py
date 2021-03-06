#import dependencies
import os
from flask import Flask, render_template,request,redirect,url_for
from flask_pymongo import PyMongo



#assigning the app to Flask
app = Flask(__name__)
#app.config for the app linking to mongodb uri
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.config['SECRET_KEY'] = 'secret'

mongo = PyMongo(app)


@app.route('/')
@app.route('/index.html')
def index():
	return render_template('index.html', user=mongo.db.mydb.find())
    

#routing for getting info from user from the add page form
@app.route('/add', methods=['GET', 'POST'])
def add():
    user = mongo.db.users
    if request.method == 'POST':
        Recipe_name = request.form['Recipe_name']
        Suitable_for = request.form['Suitable_for']
        Serves_as = request.form['Serves_as']
        Allergens = request.form['Allergens']
        Portions_served = request.form['Portions_served']
        Credits_to = request.form['Credits_to']
        Cooking_time_minutes = request.form['Cooking_time_minutes']
        Ingredients = request.form['Ingredients']
        Description = request.form['Description']
        user.insert_one(
            {
                'Recipe_name': Recipe_name ,
                'Details':{
                    'Suitable_for': Suitable_for ,
                    'Serves_as': Serves_as ,
                    'Allergens': Allergens ,
                    'Portions_served': Portions_served ,
                    'Credits_to': Credits_to , 
                },
                'Cooking_time_minutes': int(Cooking_time_minutes),
                'Ingredients': [Ingredients],
                'Description': Description 
                }
                )
        return redirect(url_for('find'))
    return render_template('add.html')
#routing for List page to find and display the recipes names
@app.route('/find')
def find():
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()
    
    return render_template('find.html',user2=user2,user3=user3, user=user)

#routing for updating the recipes using an update form 
# and update them in database using a button from results page
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
    u_credits_to=''
    Ingredients=''
    u_cooking_time_minutes=''
    u_description=''

    if request.method == 'POST':
        Recipe_name = request.form['u_recipe']
        Suitable_for = request.form['u_suitablefor'] 
        Serves_as = request.form['u_servesas']
        Allergens = request.form['u_allergens']   
        Portions_served = request.form['u_portions_served'] 
        Credits_to = request.form['u_credits_to'] 
        Cooking_time_minutes = request.form['u_cooking_time_minutes']  
        Ingredients = request.form['u_ingr']
        Description = request.form['u_description']

        user.replace_one(
                   { "Recipe_name" : name },
                   { "Recipe_name" : Recipe_name, 
                   	"Details": {
		            "Suitable_for": Suitable_for,
		            "Serves_as": Serves_as,
		            "Allergens": Allergens,
		            "Portions_served": Portions_served,
		            "Credits_to": Credits_to },
                   	"Cooking_time_minutes": Cooking_time_minutes,
	                "Ingredients": [Ingredients],
	                "Description": Description
                     })


         #after updating recipes user is redirected to "List page"   
        return redirect(url_for('find'))
    return render_template('update.html', u_description=u_description, u_credits_to=u_credits_to , u_cooking_time_minutes=u_cooking_time_minutes,u_portions_served=u_portions_served ,u_allergens=u_allergens  , u_servesas=u_servesas , u_suitablefor=u_suitablefor  ,u_recipe=u_recipe, name=name, Recipe_name=Recipe_name, user=user, user4=user4, Ingredients=Ingredients,u_ingr=u_ingr )

#the route for getting the results of the find query, displayed on results page
@app.route('/results/')
@app.route('/results/<name>')
def results(name=None):
    users = mongo.db
    user = mongo.db.users
    user2=user.find_one()
    user3=user.find()  
    return render_template('results.html', name=name, user2=user2, user3=user3, user=user, users=users)

#route for deleting recipes using the delete button from the results page
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

#route for sorting page 
@app.route('/sort')
def sort():
    user = mongo.db.users
    sort_results=''
    return render_template('sort.html', user=user, sort_results=sort_results)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
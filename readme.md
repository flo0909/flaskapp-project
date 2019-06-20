
**Recipe cookbook** using *Flask*, *Python*, *MongoDB*, *Javascript*, *Html5*, *CSS3*.

Hello and thank you for reading this page and visit the cookbook app.

The cookbook app is deployed on **Heroku.com**, the link is at the bottom of the page.  

The app is built and styled to be responsive and has been tested on Windows, different resolutions and ratios using google developer tools. Also has been tested for on Google Android and it showed that it is responsive.

I have used **MongoDb Atlas** as a database.

I have used the name of the recipe rather than the object id to find and identify the recipes.
The app is simple to use and navigate and 
The navbar has four links excluding the navbar-brand that links to the home page. Home link takes the user to the home page.The home page has included a button linked to the "List Page", where a list of recipes can be found.
The next link on the navbar is "Add Page" where the user can use a form to add his own recipe. 
The next link of the navbar is "List Page" where the user can find a list of all published recipes . The list is in the form of buttons that can be clicked and the user can access an individual recipe page with full description of the recipe and all the characteristics displayed. 
The individual recipe page shows a full description of the recipe with all the criteria displayed.
Down the page, the user can find an Update button that leads to a form where the user can update the  recipe, just in case there is something that needs updating.The fields are already filled in with the recipe informations.Another button is used to delete the recipe. There is also a "Back" button that navigates back to the "List Page".

Another link on the navbar is "Categories Page" where the user can find the category of recipes in what has a particular interest such as: 
 - Number of portions category;
 - Vegetarians suitable recipes;
 - Fast cook recipes ;
 - The range in what the recipe is served as Desert, Salad, Main course .Also for people susceptible to allergies, based of ingredients , they can find Allergens free recipes.
 Pressing on any button will give the user on the same page, a full description of the recipe within the category provided.

Code:

**Python:**
I have used for loops and Python conditionals along with Jinja2 for templating. Jinja2 templating was particularly useful for structuring the project aspect.

**MongoDb:**
The database schema is available in the repository as: **Schema.md**

**HTML:**
I have decided to use Bootstrap for responsive design although there is the Materialise option available, I am more comfortable with Bootstrap. 

**CSS:**
I have used CSS to style the app and to add functionality to buttons on sort page.

**Javascript:**
I have used event listeners to add functionality to the Category page buttons.They are set to add or remove the "show" and the "hide" class , that have a display:block and a display:none settings.

**Deployment:** I have used an environment variable to deploy the app to Heroku and conceal the MONGO_URI.The code has been deployed also on github


**Testing:**
I have tested if the data structure is a valid Json at  https://jsonformatter.org/.
I have tested the responsivness using Google Developer Dools the provided small devices: Galaxy S5,Pixel2,Pixe2 XL,Iphone 5/SE,Iphone 6/7/8, Iphone 6/7/8 plus, Iphone X,Ipad,Ipad Pro, as well as small , normal and large resolution desktops.App functionality tested for adding, reading, deleting ,updating operations.


Deployed project: https://flaskmongoproject.herokuapp.com/

Credits to shared recipes website:https://cookeatshare.com/
Credits to https://www.pexels.com/photo/close-up-decorate-dish-edible-416491/ for the background image,
Credits for : Photo by Julien Sarazin on Unsplash
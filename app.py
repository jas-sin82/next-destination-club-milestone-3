import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


#Homepage
@app.route("/")
@app.route("/home_page")
def home_page():
  
    return render_template("index.html")


# register user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' 
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# user login
@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Hi {}! Welcome to Next Destination club!".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("login.html")


# user profile 
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """grab the session user's username from db
       search session users created events"""

    if session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        user_profile = mongo.db.users.find_one({"username": session["user"]})
        destinations = list(mongo.db.destinations.find({"created_by": session["user"]}))
    
        if session["user"]:
            return render_template("profile.html", username=username, 
                destinations=destinations, user_profile=user_profile)
    
    else:
        return redirect(url_for("home_page"))

    return redirect(url_for("log_in"))


#log out
@app.route("/log_out")
def log_out():
    """
    remove user from session &
    return to login page
    """

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


# get destinations
@app.route("/get_destinations")
def get_destinations():
    if session:
        destinations = list(mongo.db.destinations.find().sort("destination_name", 1))
        return render_template("destinations.html", destinations=destinations)
    else:
        return redirect(url_for("home_page"))



# singel destination page
@app.route("/destination/<destination_id>", methods=['GET'])
def single_destination_page(destination_id):
    try:
        destination = mongo.db.destinations.find_one({"_id": ObjectId(destination_id)})
        return render_template("one-destination.html", destination=destination)
    except:
        return redirect(url_for("home_page"))


# Contact page
@app.route("/contact_page")
def contact_page():
    """ Return contact page """

    return render_template("contact.html")



# destination search 
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    destinations = list(mongo.db.destinations.find({"$text": {"$search": query}}))
    return render_template("destinations.html", destinations=destinations)


# add destination
@app.route("/add_destination", methods=["GET", "POST"])
def add_destination():
    if session:
        if request.method == "POST":
            destination = {
                "destination_name": request.form.get("destination_name"),
                "category_name": request.form.get("category_name"),
                "country": request.form.get("country"),
                "climate": request.form.get("climate"),
                "language": request.form.get("language"),
                "best_time_to_travel": request.form.get("best_time_to_travel"),
                "destination_image": request.form.get("destination_image"),
                "destination_description": request.form.get(
                    "destination_description"),
                "created_by": session["user"]
            }
            mongo.db.destinations.insert_one(destination)
            flash("Destination Successfully Added")
            return redirect(url_for("get_destinations"))

        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("add-destination.html", categories=categories)
    
    else:
        return redirect(url_for("home_page"))


#edit profile
@app.route("/edit-profile/<user_id>", methods=["GET", "POST"])
def edit_profile(user_id):
    if session:
        session_user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users = list(mongo.db.users.find({"_id": ObjectId(user_id)}))

        for user in users:
            username = user['username']

            if session_user == username:
                if request.method == "POST":
                    update_profile = {
                        "username": request.form.get("username").lower(),
                        "password": generate_password_hash(
                            request.form.get("password"))
                    }
                    session["user"] = request.form.get("username").lower()
                    mongo.db.users.update(
                        {"_id": ObjectId(user_id)}, update_profile)
                    flash("Profile Updated")
                    return redirect(url_for("profile", username=session['user']))
           
    else:
        return redirect(url_for("home_page"))

    return render_template("edit-profile.html", user=user)


#remove profile
@app.route("/remove-user-profile/<user_id>")
def remove_user_profile(user_id):
    if session:
        session_user = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        users = list(mongo.db.users.find({"_id": ObjectId(user_id)}))

        for user in users:
            username = user['username']

            if session_user == username:
                mongo.db.destinations.delete_many({"created_by": session["user"]})
                mongo.db.users.delete_one({"_id": ObjectId(user_id)})
                session.pop("user")
                return redirect(url_for("home_page"))
          
    else:
        return redirect(url_for("home_page"))


# update destination
@app.route("/update-destination/<destination_id>", methods=["GET", "POST"])
def update_destination(destination_id):
    if session:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        destinations = list(mongo.db.destinations.find({"_id": ObjectId(destination_id)}))

        for destination in destinations:
            user = destination['created_by']

            if username == user:
                if request.method == "POST":
                    submit = {
                        "destination_name": request.form.get("destination_name"),
                        "category_name": request.form.get("category_name"),
                        "country": request.form.get("country"),
                        "climate": request.form.get("climate"),
                        "language": request.form.get("language"),
                        "best_time_to_travel": request.form.get("best_time_to_travel"),
                        "destination_image": request.form.get("destination_image"),
                        "destination_description": request.form.get(
                            "destination_description"),
                        "created_by": session["user"]
                    }
                    mongo.db.destinations.update({"_id": ObjectId(destination_id)}, submit)
                    flash("Destination Successfully Updated")
                    return redirect(url_for("profile", username=session['user']))

        destination = mongo.db.destinations.find_one({"_id": ObjectId(destination_id)})
        categories = mongo.db.categories.find().sort("category_name", 1)
        return render_template("update-destination.html", destination=destination, categories=categories)
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
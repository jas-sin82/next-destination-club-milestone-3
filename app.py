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
        destinations = list(mongo.db.events.find({"created_by": session["user"]}))
    
        if session["user"]:
            return render_template("profile.html", username=username, 
                destinations=destinations, user_profile=user_profile)

    return redirect(url_for("log_in"))


#log out
@app.route("/log_out")
def log_out():
    """
    remove user from session cookie &
    return to login page
    """

    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


# get destinations
@app.route("/get_destinations")
def get_destinations():
    destinations = mongo.db.destinations.find()
    return render_template("destinations.html", destinations=destinations)


# Contact page
@app.route("/contact_page")
def contact_page():
    """ Return contact page """

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
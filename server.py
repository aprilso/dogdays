"""Server for dog logging app."""

from flask import (
    Flask,
    render_template,
    request,
    flash,
    session,
    redirect,
    jsonify,
    send_from_directory,
)
from flask.helpers import url_for
from model import connect_to_db
import crud
import cloudinary.uploader
from cloudinary_secrets import CLOUDINARY_KEY, CLOUDINARY_SECRET
from jinja2 import StrictUndefined
from time import sleep

app = Flask(__name__)
app.secret_key = "thiswillbeasecretkey"  # Used to encrypt a session. Can set it to generate random #s and letters each time, or in secrets.sh (make more secret before deployment)
app.jinja_env.undefined = StrictUndefined

# TBD: Add routes for production


@app.route("/")
def homepage():
    """view homepage"""
    return render_template("homepage.html")


@app.route("/users")
def allusers():
    """view all users"""

    users = crud.return_all_users()

    return render_template("all_users.html", users=users)


@app.route("/users/<user_id>")
def userprofile(user_id):
    """view a user profile"""

    user = crud.get_user_by_id(user_id)
    userdogs = crud.get_dog_by_user(user_id)

    return render_template("your_profile.html", user=user, userdogs=userdogs)


@app.route("/dogs")
def alldogs():
    """view all dogs (*this will not be public)"""

    dogs = crud.return_all_dogs()

    return render_template("all_dogs.html", dogs=dogs)


@app.route("/dogs/<dog_id>")
def dogprofile(dog_id):
    """view the dog's profile"""

    dog = crud.get_dog_by_id(dog_id)
    userdogs = crud.get_user_by_dog(dog_id)
    img_url = request.args.get("imgURL")

    return render_template(
        "dog_profile.html", dog=dog, userdogs=userdogs, img_src=img_url
    )


@app.route("/login", methods=["POST"])
def login():
    """login user"""
    email = request.form.get("login_email")
    password = request.form.get("login_password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:  
        flash("The email or password is incorrect")
    else:
        session["user_email"] = user.email
        session["user_id"] = (user.user_id)  # in the future, could just store user_id and lookup email from that
        flash(
            f"Welcome back, {user.first_name}"
        )  # TO-DO - redirect to the logged in page instead

    return redirect("/")


@app.route("/logout")
def logout():
    """logs out the user, redirects them to homepage"""  # check if this is good
    session.clear()
    flash("You have been logged out!")
    return redirect("/")


@app.route("/new_user")
def new_user_page():
    """shows the new user account creation page"""

    return render_template("new_user.html")


@app.route("/users", methods=["POST"])
def new_user():
    """creates a new user account"""

    email = request.form.get("email")
    password = request.form.get("password")
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    phone_number = request.form.get("phone_number")
    icon = "default_user_icon.jpg"

    new_user = crud.get_user_by_email(email)

    if new_user == None:
        crud.create_user(first_name, last_name, email, password, phone_number, icon)
        flash("Success! New account has been created")
    else:
        flash("An account with that email already exists.")

    return redirect("/")


@app.route("/add_dog")
def new_dog_page():
    return render_template("new_dog.html")


@app.route("/add_dog", methods=["POST"])
def new_dog_to_user():
    """Adds a new dog and automatically adds it to the user"""

    dog_name = request.form.get("dog_name")
    img_src = "default_dog_icon.jpg"
    bio = request.form.get("bio")
    medication = request.form.get("medication")
    medical_info = request.form.get("medical_info")
    allergies = request.form.get("allergies")
    weight = request.form.get("weight") or None
    food = request.form.get("food")
    misc_notes = request.form.get("misc_notes")
    sex = request.form.get("sex")
    breed = request.form.get("breed")
    primary_color = request.form.get("primary_color")
    microchip_num = request.form.get("microchip_num") or None
    dob = request.form.get("dob") or None

    dog = crud.create_dog(
        dog_name,
        img_src,
        bio,
        medication,
        medical_info,
        allergies,
        weight,
        food,
        misc_notes,
        sex,
        breed,
        primary_color,
        microchip_num,
        dob,
    )
    # for cloudinary, add img_url to crud, pass in img_url as part of crud

    # To-Do - Check that primary user is displayed as true
    user_id = session["user_id"]
    dog_id = dog.dog_id
    primary_user = True

    crud.assign_dog_to_human(user_id, dog_id, primary_user)
    flash("Success! New dog has been added with you as primary user")

    return redirect("/")


@app.route("/lookup_dog", methods=["GET"])
def lookup_dog():
    """Look up an existing dog to add"""
    dog_id = request.args.get("dog_id")

    return redirect(f"/dogs/{ dog_id }")


# @app.route("/lookup_dog", methods=["POST"])
# def add_existing_dog():
#     """Adds an existing dog to a user after looking it up"""

#     dog_id = session["dog_id"]
#     user_id = session["user_id"]
#     primary_user = False  # because they're not the first person who created the dog
    
#     crud.assign_dog_to_human(user_id, dog_id, primary_user)

#     flash("Success! You have been added as this dog's caretaker!")

#     return redirect("/")


@app.route("/lookup_dog", methods=["POST"])
def add_existing_dog():

    dog_id = request.form.get("dog_id")
    user_id = session["user_id"]
    primary_user = False 

    crud.assign_dog_to_human(user_id, dog_id, primary_user)

    flash("Success! You have added this dog to your dogs!")

    return redirect("/")



@app.route("/upload-user-photo", methods=["POST"])
def add_user_photo():
    """Upload a user (human) photo - optional"""
    pass


@app.route("/show_image")
def show_image():
    img_url = request.args.get("imgURL")
    dog_id = session["dog_id"]

    return redirect(f"/dogs/{ dog_id }")


@app.route("/upload-dog-photo", methods=["POST"])
def add_dog_photo():
    """Process and upload a dog profile photo"""
    dog_photo = request.files["dog-photo"]

    result = cloudinary.uploader.upload(
        dog_photo,
        api_key=CLOUDINARY_KEY,
        api_secret=CLOUDINARY_SECRET,
        cloud_name="dogdays",
    )

    img_url = result["secure_url"]
    dog_id = session["dog_id"]

    crud.update_dog_photo(dog_id, img_url)
    # need to save this result to the database so it can be accessed again - update this as "photo" in the database

    return redirect(url_for("show_image", imgURL=img_url))


# ---TASKS SECTION ---



@app.route("/dogs/<dog_id>/schedule")
def show_schedule(dog_id):
    print("DOG ID", dog_id)
    session["dog_id"] = dog_id
    #return send_from_directory("static", "index.html")
    # return render_template("/daily_schedule.html")


@app.route("/api/add-task", methods=["POST"])
def add_task():
    """Add a new task to the database."""

    task_name = request.get_json().get("task_name")
    frequency = request.get_json().get("frequency")
    instructions = request.get_json().get("instructions")
    dog_id = session["dog_id"]

    created_task = crud.create_task(dog_id, task_name, frequency, instructions)

    new_task = {
        "taskId": created_task.task_id,
        "taskName": created_task.task_name,
        "frequency": created_task.frequency,
        "instructions": created_task.instructions,
    }

    return jsonify({"success": True, "taskAdded": new_task})
    # don't need a flash message b/c it will show up after you press the Add button


@app.route("/api/delete-task/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    """delete a selected task"""

    delete_task = crud.delete_task(task_id)
    response = {"success": delete_task}

    return response
    # could create a conditional statement with error response


@app.route("/api/dogschedule/<dog_id>")
def dog_schedule(dog_id):
    """Returns info about a dog's schedule as JSON"""

    schedule = [
        {
            "taskId": each.task_id,
            "taskName": each.task_name,
            "frequency": each.frequency,
            "instructions": each.instructions,
        }
        for each in crud.get_tasks_by_dog(dog_id)
    ]
    return jsonify(schedule)


if __name__ == "__main__":
    connect_to_db(app)
    app.run("0.0.0.0", debug=True)

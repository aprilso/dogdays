<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdayslogo.png" width="50%" alt="Dog Days Logo">

# Dog Days

## About
Dog Days is a full stack web application for keeping track of your dogs’ info and activities, and coordinate and share among multiple caretakers. Create an account, add new or existing dogs, and share and track their activities.

## Features

Create a new user profile, then add new or existing dogs. View important dog info like health and care or behavior notes.

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_newdog.png" width="100%" alt="Dog Log">

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_dogprofile.png" width="100%" alt="Dog Profile">

Track their activities by recording a new entry, adding info like category (feeding, exercise, grooming, etc), time it occurred, and optional notes. Flag for follow up to make sure other caretakers see it.

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_newentry.png" width="100%" alt="New Entry">

View all of your dog's activities synced with all of their caretakers. The icon system makes it easy to see your dog's day at a glance. Flagged entries are on the side so you never miss any important updates. 

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_log.png" width="100%" alt="Dog Log">

## Gallery

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_home.png" width="100%" alt="Home Page">

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_register.png" width="100%" alt="Dog Days register for new account page">

<img src="https://github.com/aprilso/dogdays/blob/main/static/images/readme-images/dogdays_signin.png" width="100%" alt="Dog Days signin page">



## Technologies

- Python 3.7
- PostgresSQL
- Flask
- Flask-SQLAlchemy
- SQLAlchemy
- Bootstrap
- HTML/CSS

## APIs

- Cloudinary


## Instructions

To run the Dog Days app on your machine:

1) Make sure you have PostgreSQL and Python 3.7 installed. 

2) Clone or fork this repo:
```
https://github.com/aprilso/dogdays.git
```
3) Create a new virtual environment inside your Dog Days directory, then activate it:

```
virtualenv env
source env/bin/activate
```
4) Install the dependencies:
```
pip install -r requirements.txt
```

5) Sign up to use the Cloudinary API - https://cloudinary.com/ and store your API keys in your secrets.sh file.
Example:
```export CLOUDINARY_KEY = "YOUR_API_KEY" export CLOUDINARY_SECRET = "YOUR_API_SECRET"
   ```

6) Set up the database:
```
createdb dogdaysdb
python3 model.py
python3 seed_database.py
```

7) Run the server:
```
python3 server.py
```
You can now access the Dog Days app at 'localhost:5000/'



### Notes on Javascript server: 
8/18/21 - The project currently has another Javascript server connected through Vite.js for future React builds (accessible through 'localhoust:3000/'). This is not requred for normal use and does not affect the current functionality.

### Javascript Setup

Setup Python environment as normal.

From the main project folder, run `npm install`.

### Running the application

In 2 different tabs

- Start the Python server
- Run Javascript server `npm run dev`


## About the developer
April Soetarman is an artist, designer, creative technologist, and new puppy owner. This is her first full-stack project. She can be found on [LinkedIn](https://www.linkedin.com/in/aprilsoetarman/), [Github](https://github.com/aprilso), and her portfolio site [AprilSoetarman.com](https://www.aprilsoetarman.com)

Huge thanks to the Hackbright instructors, my mentor Carolina Avila, and the rest of my September 2021 cohort!


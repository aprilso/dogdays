"""Models for dog logging app """

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
  """A human user."""

  __tablename__ = "users"

  user_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)
  first_name = db.Column(db.String, nullable=False)
  last_name = db.Column(db.String, nullable=False)
  email = db.Column(db.String, nullable=False, unique=True)
  password = db.Column(db.String)
  phone_number = db.Column(db.String, unique=True)
  icon = db.Column(db.String, default='humanicon.jpg')
  #optional: color_id = db.Column(db.String, unique=True)

  dogs = db.relationship("Dog",
                        secondary="users_dogs",
                        backref="users")
  #can access the dogs attribute through users_dogs, don't have to create for Dog class also cause backref
  #optional - check crud functions for accessing users with dogs?

  def __repr__(self):
        return f'<User: user_id={self.user_id} last_name={self.last_name} email={self.email}>'

class Dog(db.Model):
  """A dog"""

  __tablename__ = "dogs"

  dog_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)
  dog_name = db.Column(db.String, nullable=False)
  photo = db.Column(db.String) #default='dog.jpg'
  bio = db.Column(db.String, nullable=True)
  medication = db.Column(db.String, nullable=True)
  medical_info = db.Column(db.String, nullable=True)
  allergies = db.Column(db.String, nullable=True)
  weight = db.Column(db.Integer, nullable=True)
  food = db.Column(db.String, nullable=True)
  misc_notes = db.Column(db.String, nullable = True)
  sex=db.Column(db.String)
  breed=db.Column(db.String)
  primary_color=db.Column(db.String)
  microchip_num=db.Column(db.String, nullable=True)
  dob=db.Column(db.DateTime, nullable=True)
  #contacts = db.Column(db.String)

  def __repr__(self):
        return f"<Dog: dog_id={self.dog_id} dog_name={self.dog_name}>"


#users_dogs is the middle for two one-to-many relationships (not actually many to many)
# a dog can have many users. a user can have many dogs.

class UserDog (db.Model):
  """Relational class that connects a dog of a specific user"""

  __tablename__ = "users_dogs"

  usersdogs_id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer,
            db.ForeignKey('users.user_id'),
            nullable=False)
  dog_id = db.Column(db.Integer,
            db.ForeignKey('dogs.dog_id'),
            nullable=False)
  primary_user = db.Column(db.Boolean) #optional - this is just to indicate if someone's the main owner of a dog

  user = db.relationship("User")
  dog = db.relationship("Dog")

  def __repr__(self):
        return f'<UserDog: dog_id={self.dog_id} user_id={self.user_id}>'

#Questions - relationships vs foreignkey
#to have a relationship, need a foreign key in one table, primary key in another table

#foreignkeys - this column refers to a column in another database table
#relationships - this thing is a reference to another table
#relationships in sqlalchemy do use foreign keys


###### NEWER ENTRY VERSION 

class Entry(db.Model):
  """one time events"""

  __tablename__ = "entries"

  entry_id = db.Column(db.Integer,
                  autoincrement=True,
                  primary_key=True)

  dog_id = db.Column(db.Integer,
            db.ForeignKey('dogs.dog_id'),
            nullable=False)

  user_id = db.Column(db.Integer,
            db.ForeignKey('users.user_id'),
            nullable=False)

  entry_name = db.Column(db.String)
  entry_type = db.Column(db.String) # 9 options:Food, Training, Walk, Play, Poop, Pee, Sick, Medication, Grooming
  time_happen = db.Column(db.DateTime) 
  notes = db.Column(db.String)
  flag = db.Column(db.String)

  def __repr__(self):
    return f'<Entry: dog_id={self.dog_id} user_id={self.user_id} entry_id={self.entry_id} entry_name = {self.entry_name}>'






###### OLDER TASK VERSION 


class Task(db.Model): # simple Task version for testing
  """Simplified Task class for testing"""

  __tablename__ = "tasks"

  task_id = db.Column(db.Integer,
                  autoincrement=True,
                  primary_key=True)

  dog_id = db.Column(db.Integer,
              db.ForeignKey('dogs.dog_id'),
              nullable=False)

  task_name = db.Column(db.String)
  frequency = db.Column(db.String) #could set as Enum, but string for now is fine
  instructions = db.Column(db.String)

  def __repr__(self):
      return f'<Task: dog_id={self.dog_id} task={self.task_id} task_name = {self.task_name}>'



class ComplicatedTask(db.Model): #rename as Task later
  """Scheduled tasks to do for the dog"""
   #tasks specific to that dog - tasks marked as done

  __tablename__ = "complicated_tasks" #rename as tasks later

  task_id = db.Column(db.Integer,
                autoincrement=True,
                primary_key=True)

  dog_id = db.Column(db.Integer,
            db.ForeignKey('dogs.dog_id'),
            nullable=False)

  task_name = db.Column(db.String)
  task_created_time = db.Column(db.DateTime)
  # optional - should take in local datetime from the computer, on the front-end

  frequency = db.Column(db.String)
  #Enum - like a string, but restricted to on the front end to dropdown Daily, Weekly, Monthly, Yearly

  #OPTION: Maybe just make dropdowns to just Morning, Afternoon, Evening
  task_scheduled_time = db.Column(db.String) #On Frontend - Morning, Afternoon, Evening (coukd be #Enum)
  flexible = db.Column(db.Boolean) #optional, as a checkbox - then you don't have to set the time (like "all-day")
  #it could appear at the top

  task_scheduled_day = db.Column(db.String) #restrict on the frontend Monday, Tuesday, etc + everyday
  #if daily, it should already be everyday #Could be Enum

  task_scheduled_hour_start = db.Column(db.DateTime)
  task_scheduled_hour_end = db.Column(db.DateTime) #not required for all tasks


  def __repr__(self):
      return f'<Task: dog_id={self.dog_id} task={self.task_id} task_name = {self.task_name}>'


class TaskHistory(db.Model):
  """History of the specific dog's tasks"""
  #track the user who completed the tasks here
  #Ex: Query Join with the Task table, filtering taskhistory by user_id

  __tablename__ = "task_history"

  taskhistory_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)

  task_id = db.Column(db.Integer,
            db.ForeignKey('tasks.task_id'),
            nullable=True)

  user_id = db.Column(db.Integer,
            db.ForeignKey('users.user_id'),
            nullable=False)

  date_scheduled = db.Column(db.DateTime)
  date_happened = db.Column(db.DateTime)

  #option: restricting time frame when you can complete task, like morning walk only in morning
  #can log in whenever you want
  #You'll get the information from the task table

  task_comment = db.Column(db.String)
  task_completed = db.Column(db.Boolean, nullable=True) #check that it defaults to False as start
  #Add: create the next occurence for the task after the current one has been completed
  # Example - after Evening walk has occurred, create the next time it needs to happen
  #front end would check it off, Run a function in crud after a result of task_completed, then that would also call
  #crud function to create a new task.


  #Frontend - unscheduled task, task_id nullable=True
  #A task that doesn't need to be set, dropdown has (Unscheduled Event)
  #so the task_id takes in None. Frontend restriction
  #each element will have task_id - in this case the task_id will be none.







#Questions - check if nullable is default to true or false (which one do you have to specify?)



#----connection----

def connect_to_db(flask_app, db_uri='postgresql:///doglogdb', echo=True):
  flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  flask_app.config['SQLALCHEMY_ECHO'] = echo
  flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  db.app = flask_app
  db.init_app(flask_app)

  print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
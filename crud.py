"""CRUD operations (Create Read Update Delete) """

from model import Task, TaskHistory, db, User, Dog, UserDog, connect_to_db, Entry
from datetime import datetime, date

from sqlalchemy import Date, DATE, extract #added



def create_user(first_name, last_name, email, password, phone_number, icon):
  """Create and return a new user."""

  user = User(first_name=first_name, last_name=last_name, email=email, password=password, phone_number=phone_number, icon=icon)

  db.session.add(user)
  db.session.commit()

  return user

def return_all_users():
    """return all human users"""
    return User.query.all()

def get_user_by_id(user_id):
    """look up the user by id"""
    return User.query.get(user_id)

def get_user_by_email(email):
    """return a user by email"""
    return User.query.filter(User.email == email).first()


def get_user_without_dog(dog_id):
    """return all users without dogs"""
    #To-Do - where their dog_id = null??
    pass



#Note: unwieldy, could take in one dog_info as a dictionary and then key into it 
def create_dog(dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes, sex, breed, primary_color, microchip_num, dob):
  """Create and return a new dog."""

  dog = Dog(dog_name=dog_name, photo=photo, bio=bio, medication=medication, medical_info=medical_info, allergies=allergies, weight=weight, food=food, misc_notes=misc_notes, sex=sex, breed=breed,
        primary_color=primary_color, microchip_num=microchip_num, dob=dob)
  #add vet

  db.session.add(dog)
  db.session.commit()

  return dog

#To-Do - create functions for updating the info for users and dogs (without taking in each variable)
# def update_dog():
#Note: check out ratings lab crud.py

# def edit_dog(dog_id):
#   """Edit the info for an existing dog"""

#   editing_dog = Dog.query.get(dog_id)

#   if request.method != 'POST':


def get_dog_by_id(dog_id):
  """look up the dog by id"""
  return Dog.query.get(dog_id)

def return_all_dogs():
  """return all dogs"""
  return Dog.query.all()

def update_dog_photo(dog_id, new_photo):
  """update the dog's photo url from the upload"""
  # 7/25/21 - check if this works

  old_photo = Dog.query.get(dog_id)
  old_photo.photo = new_photo
  db.session.commit()

  # Dog.query.filter(Dog.photo == photo).replace()
  # db.session.commit()

#To-Do: update human info by user_id, update dog info by dog_id

def get_dog_by_user(user_id):
  """get all the dogs that belong to a user"""

  return UserDog.query.filter(UserDog.user_id == user_id).all()
  
def get_user_by_dog(dog_id):
  """get all the users of a single dog"""

  return UserDog.query.filter(UserDog.dog_id == dog_id).all()

def assign_dog_to_human(user_id, dog_id, primary_user):
  """assign a dog to a human""" #should also work for assign human to dog

  userdog = UserDog(dog_id=dog_id, user_id=user_id, primary_user=primary_user)

  db.session.add(userdog)
  db.session.commit()

  return userdog

def remove_dog(user_id, dog_id):
  """Remove a dog from a user's care""" #check if it works

  UserDog.query.filter(UserDog.user_id == user_id, UserDog.dog_id == dog_id).delete()
  db.session.commit()


# DELETE LATER
# def dog_age(dog_id):
#   """return the dog's age"""

#     today = datetime.now()
#     # today_year = datetime.now().year
#     # today_month = datetime.now().month

#     dog_year = dog.dob.year
#     dog_month = dog.dob.month

#     years = today.year - dog_year
#     months = today.month - dog_month

#     if (today.day < dog.dob.day):
#         months -= 1
#         while months < 0:
#             months += 12
#             years -= 1
#     return dog_age = '%sy %smo'% (years, months)


#### ENTRIES SECTION -----

def create_entry(dog_id, user_id, entry_name, entry_type, time_happen, notes, flag):
  """Creating an entry - something that happened one time"""

  entry = Entry(dog_id=dog_id, user_id=user_id, entry_name=entry_name, entry_type=entry_type, time_happen=time_happen, notes=notes, flag=flag)

  db.session.add(entry)
  db.session.commit()

  return entry


def delete_entry(entry_id):
  """delete a selected entry""" #need to check if it works

  Entry.query.filter(Entry.entry_id == entry_id).delete()
  db.session.commit()


def sort_entry_by_type(entry_type):
  """return display entries by type"""
  sorted_entries = Entry.query.filter(Entry.entry_type == entry_type).all()
  return sorted_entries


def get_entries_by_dog(dog_id):
  """Get all the entries for a dog"""

  # return Entry.query.filter(Entry.dog_id == dog_id).order_by(Entry.time_happen) #This is good!

  return Entry.query.join(User).add_columns(Entry.entry_name, Entry.time_happen, Entry.entry_type, Entry.notes, Entry.flag, User.first_name, User.last_name).filter(Entry.dog_id == dog_id).order_by(Entry.time_happen)
  # ADD ALL THE COLUMNS YOU NEED IN ADD_COLUMNS


def get_dog_entries_today(dog_id):
  """Get all the entries for a dog that occurred today""" #not working

  this_day = date.today() #but want just by year, month, day

  year = this_day.year
  month = this_day.month
  day = this_day.day

  entry_time = Entry.query.filter(Entry.time_happen == this_day).all()

  # entry_time = Entry.query.filter(date_format(Entry.time_happen,”Y-m-d”) == this_day).all()

  # entry_time = Entry.query.filter(datetime.strptime(Entry.time_happen, '%Y-%m-%d') == this_day).all()
  # .filter(Entry.dog_id == dog_id).all()

  # entry_time = Entry.query.filter(DATE((Entry.time_happen) == this_day).all()


  # entry_time = Entry.query.filter(extract('month', Entry.time_happen) == datetime.today().month).all

  
  # , Entry.time_happen.month == month, Entry.time_happen.day == day).all()
  # entry_match = entry_time.filter(Entry.time_happen.day == day)
  # today_year = datetime.now().year
  # today_month = datetime.now().month
  
  # dog_entries = Entry.query.filter(Entry.dog_id == dog_id).all()
  # today_entries = Entry.query.filter(Entry.time_happen == entry_time).all()
  # return entry_time

  #time_happen in the db is a datetime, but doesn't have a .year, .month or .day method
  
  return entry_time




#TASKS SECTION ----

# TASKS - SIMPLE VERSION
def create_task(dog_id, task_name, frequency, instructions):
  """simplied version of creating a task """

  task = Task(dog_id=dog_id, task_name=task_name, frequency=frequency, instructions=instructions)

  db.session.add(task)
  db.session.commit()

  return task

# TASKS -COMPLICATED VERSION
# def create_task(dog_id, task_name, task_created_time, frequency, task_scheduled_time, flexible, task_scheduled_day, 
#                 task_scheduled_hour_start, task_scheduled_hour_end):
#   """create a task for a dog (to be completed by the user)"""
  
#   task = Task(dog_id=dog_id, task_name=task_name, task_created_time=task_created_time, frequency=frequency, task_scheduled_time=task_scheduled_time, flexible=flexible, 
#         task_scheduled_day=task_scheduled_day, task_scheduled_hour_start=task_scheduled_hour_start, task_scheduled_hour_end=task_scheduled_hour_end)

#   db.session.add(task)
#   db.session.commit()

#   return task

def get_tasks_by_dog(dog_id):
  """return all the tasks that are scheduled to one dog"""
  return Task.query.filter(Task.dog_id == dog_id).all()
  
def mark_task_complete():
  """Update the status of a task - mark an existing dog's task as complete or add notes """
  pass

def sort_tasks_by_frequency(frequency):
  """show all tasks by frequency (ex: show all daily tasks)"""
  return Task.query.filter(Task.frequency == frequency).all()

def delete_task(task_id):
  """delete a selected task"""

  Task.query.filter(Task.task_id == task_id).delete()
  db.session.commit()
  return "1"
  
def return_completed_tasks():
  """return all tasks that have already been completed"""
  pass

def return_all_tasks_until_now():
  """return all tasks (by all users) up until this datetime"""
  #will reference TaskHistory
  pass

def return_all_tasks_from_user(user_id):
  """will return all the tasks completed by one user"""
  return TaskHistory.query.filter(TaskHistory.user_id == user_id).all()


#CRUD - make a function that translates the Dictionary format of Task class objects - getting information that's already there
#Still need all the server side functions


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
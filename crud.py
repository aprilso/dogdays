"""CRUD operations (Create Read Update Delete) """

from model import Task, TaskHistory, db, User, Dog, UserDog, connect_to_db, Entry
from datetime import datetime, date, timedelta

from sqlalchemy import cast, Date



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
    #To-Do - where their dog_id = null
    pass


def create_dog(dog_name, photo, bio, medication, medical_info, allergies, weight, food, misc_notes, sex, breed, primary_color, microchip_num, dob):
  """Create and return a new dog."""

  dog = Dog(dog_name=dog_name, photo=photo, bio=bio, medication=medication, medical_info=medical_info, allergies=allergies, weight=weight, food=food, misc_notes=misc_notes, sex=sex, breed=breed,
        primary_color=primary_color, microchip_num=microchip_num, dob=dob)

  db.session.add(dog)
  db.session.commit()

  return dog

#To-Do - create functions for updating the info for users and dogs (without taking in each variable)
# def update_dog():


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
 
  old_photo = Dog.query.get(dog_id)
  old_photo.photo = new_photo
  db.session.commit()



def get_dog_by_user(user_id):
  """get all the dogs that belong to a user"""

  return UserDog.query.filter(UserDog.user_id == user_id).all()
  
def get_user_by_dog(dog_id):
  """get all the users of a single dog"""

  return UserDog.query.filter(UserDog.dog_id == dog_id).all()

def assign_dog_to_human(user_id, dog_id, primary_user):
  """assign a dog to a human""" 

  userdog = UserDog(dog_id=dog_id, user_id=user_id, primary_user=primary_user)

  db.session.add(userdog)
  db.session.commit()

  return userdog

def remove_dog(user_id, dog_id):
  """Remove a dog from a user's care""" 

  UserDog.query.filter(UserDog.user_id == user_id, UserDog.dog_id == dog_id).delete()
  db.session.commit()


#Edit & update dog info
def update_dog_info(dog_id, dog_name, bio, medication, medical_info, allergies, weight, food, misc_notes, sex, breed, primary_color, microchip_num, dob):
  """Update dog info"""
  
  dog = Dog.query.get(dog_id)

  dog.dog_name = dog_name
  dog.bio = bio
  dog.medication = medication
  dog.medical_info = medical_info
  dog.allergies = allergies
  dog.weight = weight
  dog.food = food
  dog.misc_notes = misc_notes
  dog.sex = sex
  dog.breed = breed
  dog.primary_color = primary_color
  dog.microchip_num = microchip_num
  dog.dob = dob

  db.session.commit()

  return dog 
  
  







#### ENTRIES SECTION -----

def create_entry(dog_id, user_id, entry_name, entry_type, time_happen, notes, flag):
  """Creating an entry - something that happened one time"""

  entry = Entry(dog_id=dog_id, user_id=user_id, entry_name=entry_name, entry_type=entry_type, time_happen=time_happen, notes=notes, flag=flag)

  db.session.add(entry)
  db.session.commit()

  return entry


def delete_entry(entry_id):
  """delete a selected entry""" 

  Entry.query.filter(Entry.entry_id == entry_id).delete()
  db.session.commit()


def sort_entry_by_type(entry_type):
  """return display entries by type"""
  sorted_entries = Entry.query.filter(Entry.entry_type == entry_type).all()
  return sorted_entries


def get_entries_by_dog(dog_id):
  """Get all the entries for a dog"""

  return Entry.query.join(User).add_columns(Entry.entry_name, Entry.time_happen, Entry.entry_type, Entry.notes, Entry.flag, User.first_name, User.last_name).filter(Entry.dog_id == dog_id).order_by(Entry.time_happen)



def get_dog_entries_today(dog_id):
  """Get all the entries for a dog that occurred today""" 

  today_entries_joined = Entry.query.join(User).add_columns(Entry.entry_name, Entry.time_happen, Entry.entry_type, Entry.notes, Entry.flag, User.first_name, User.last_name).filter(Entry.time_happen +timedelta(days=1) >= datetime.now()).filter(Entry.dog_id == dog_id).order_by(Entry.time_happen).all()

  return today_entries_joined

def get_dog_entries_past(dog_id):
  """Get all the entries for a dog that occurred before today""" 
  
  past_entries_joined = Entry.query.join(User).add_columns(Entry.entry_name, Entry.time_happen, Entry.entry_type, Entry.notes, Entry.flag, User.first_name, User.last_name).filter(Entry.time_happen +timedelta(days=1) <= datetime.now()).filter(Entry.dog_id == dog_id).order_by(Entry.time_happen).all()

  return past_entries_joined

def get_dog_entries_by_day(dog_id, time_happen):

  working = Entry.query.join(User).add_columns(Entry.entry_name, Entry.time_happen, Entry.entry_type, Entry.notes, Entry.flag, User.first_name, User.last_name).filter(cast(Entry.time_happen, Date) == time_happen.strftime("%m/%d/%Y")).filter(Entry.dog_id == dog_id).order_by(Entry.time_happen).all()

  return working



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



if __name__ == '__main__':
    from server import app
    connect_to_db(app)
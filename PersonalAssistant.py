class PersonalAssistant:
  # Add an __init__ function here
  def __init__(self, todos, birthdays, contacts):
    self.todos = todos #todos variable holds the JSON data
    self.birthdays = birthdays
    self.contacts = contacts 

  def get_contact(self, name):
    if(name in self.contacts):
      return self.contacts[name]
    else:
      return "No contact with that name exists."

  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
    # Get the todo_item index in list
      index = self.todos.index(todo_item)
    # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todo(self):
    return self.todos

  def get_birthdays(self):
    return self.birthdays

  def get_birthday(self, name):
    if(name in self.birthdays):
      return f"{name}'s birthday is on {self.birthdays[name]}."
    else:
      return f"No birthday data for {name}."

  def add_birthday(self, name, date):
    if name in self.birthdays:
      return f"You have already entered {name}'s birthday."
    else:
      self.birthdays[name] = date
      return f"{name}'s birthday has been successfully added."

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      return f"{name}'s birthday has been successfully removed."
    else:
      return "No birthday data for that person exists."

  def get_contacts(self):
    return self.contacts

  def add_contact(self, name, title):
    if name in self.contacts:
      return f"You have already entered {name}'s contact information."
    else:
      self.contacts[name] = title
      return f"{name}'s contact information has been successfully added."

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      return f"{name}'s contact information has been successfully removed."
    else:
      return f"No contact information for that person exists."


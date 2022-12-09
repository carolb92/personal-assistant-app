#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant
import json
#open JSON file and pass data to PersonalAssistant class
#todos variable holds the JSON data
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
  #todo_list variable holds data converted from the JSON file using the load function
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)
  #assistant initiates a new instance of the PersonalAssistant class 
  #it is passed the todo_list and birthday_list variables which hold data from the JSON file
  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays ****
    4: Get birthday
    5: Add birthday 
    6: Remove birthday
    Select a number or type 'Exit' to quit: 
    **** Contacts ****
    7: Get a Single Contact
    8: Add a Contact 
    9: Delete a Contact
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # Get Birthday 
    elif user_command == "4":
      print("Your birthday contacts: \n")
      for name in assistant.get_birthdays():
        print(name)
      user_input = input("\nEnter a name ")
      print(f"\n {assistant.get_birthday(user_input)}") 
    # Add Birthday 
    elif user_command == "5":
      name = input("Name of the person: ")
      birthday = input("Their birthday (ex: 08/18/2000): ")
      print(f"\n{assistant.add_birthday(name, birthday)}")
    # Remove Birthday
    elif user_command == "6":
      print("Your birthday contacts: \n")
      for name in assistant.get_birthdays():
        print(name)
      user_input = input("Whose birthday do you want to remove? ")
      print(f"\n{assistant.remove_birthday(user_input)}")
    # Get Contact 
    elif user_command == "7":
      print("Your contacts: \n")
      for name in assistant.get_contacts():
        print(name)
      user_input = input("\nEnter a name ")
      print(f"\n{assistant.get_contact(user_input)}")
    # Add Contact
    elif user_command == "8":
      name = input("Name of the person: ")
      title = input("Their title (ex: software engineer): ")
      print(f"\n{assistant.add_contact(name, title)}")
    # Remove Contact 
    elif user_command == "9":
      print("Your contacts: \n")
      for name in assistant.get_contacts():
        print(name)
      user_input = input("Which contact do you want to remove? ")
      print(f"\n{assistant.remove_contact(user_input)}")
      
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

#write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todo(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)
#json.dump() converts the data from the assistant.get_todos() getter to the JSON file, using the write_todos variable


  
#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below:")
print("It is " + now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        #prvo otvorim fajl i ucitam ga u listu
        todos = functions.get_todos()

        #dodam na tu listu unos
        todos.append(todo)

        #upisem nazad celu moju listu
        functions.write_todos(todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        #new_todos = []
        #for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        #new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            row = f"{index+1}- {item.strip('\n')}"
            print(row)
        print("Length: ", len(todos))
    elif user_action.startswith('edit'):
        todos = functions.get_todos()
        try:
            number = int(user_action[5:])
            if number > len(todos):
                print(f"Todo with number {number} does not exist.")
                continue
            number = number - 1

            new_todo = input("Enter a new todo:")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            number = number - 1

            todos = functions.get_todos()

            completed_todo = todos.pop(number).strip('\n')
            print("You completed " + completed_todo)

            functions.write_todos(todos)

            message = f"Todo {completed_todo} was removed from the list"
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not valid.")

print("Bye")
import functions
import PySimpleGUI as sg
import time
import os

# creating file todos if it doesn't exists
if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", 'w') as file:
        pass

clock = sg.Text("", key='clock')

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button(key="Add", size=2, tooltip='Add an item to list', image_source='files/add.png', mouseover_colors="LightBlue2")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete", size=2, tooltip='Complete item', image_source='files/complete.png', mouseover_colors="LightBlue2")
exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App', layout=[[clock],
                                           [label],
                                           [input_box, add_button],
                                           [list_box, edit_button, complete_button],
                                           [exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                current_index = todos.index(todo_to_edit)
                todos[current_index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break


window.close()
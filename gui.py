import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', size=(45,10))

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button], [list_box]], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case sg.WIN_CLOSED():
            break


window.close()
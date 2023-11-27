FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """"Return the list from text file"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """"Insert a list into text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


print("hello from functions")
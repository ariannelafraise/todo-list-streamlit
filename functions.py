FILEPATH= "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def add_todo(filepath=FILEPATH, todo="new todo\n"):
    current_todos = get_todos()
    current_todos.append(todo + "\n")
    with open(filepath, 'w') as file_local:
        file_local.writelines(current_todos)
    return 0

def complete_todo(completed_todo, filepath=FILEPATH):
    current_todos = get_todos()
    current_todos.pop(completed_todo)
    with open(filepath, 'w') as file_local:
        file_local.writelines(current_todos)

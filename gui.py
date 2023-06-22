import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values= functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

window = sg.Window("My To-Do App", 
                   layout=[[label], [input_box, add_button], [list_box, edit_button]], 
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values.get("todos", "NA"))
    
    if event == "Add":
        todos = functions.get_todos()
        new_todo = values.get("todo") + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        window["todos"].update(values=todos)
    
    elif event == "Edit":
        todo_to_edit = values.get("todos")[0]
        new_todo = values.get("todo")
        
        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)
        window["todos"].update(values=todos)
    
    elif event == "todos":
        window["todo"].update(value=values["todos"][0])
    
    elif event == sg.WIN_CLOSED:
        break

window.close()
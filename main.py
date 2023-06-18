todos = []

while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)

    elif user_action == "show":
        for idx, item in enumerate(todos):
            print(f"{idx + 1} -- {item}")

    elif user_action == "edit":
        number = int(input("Choose the number of the todo to edit: "))
        new_todo = input("Enter new todo: ")
        todos[number -1]= new_todo

    elif user_action == "complete":
        number = int(input("Number of the todo completed: "))
        todos.pop(number-1)


    elif user_action == "exit":
        break


print("Bye!!")

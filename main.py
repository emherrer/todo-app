while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        #todo = input("Enter a todo: ") + "\n"
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for idx, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{idx + 1} -- {item}")

    elif "edit" in user_action:
        number = int(user_action[5:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ") + "\n"
        todos[number - 1] = new_todo

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_removed = todos[number-1].strip("\n")
        todos.pop(number-1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f"Todo {todo_removed} was removed from the list.")

    elif user_action == "exit":
        break

    else:
        print("Command is not valid!")


print("Bye!!")
print(todos)

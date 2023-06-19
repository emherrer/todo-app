while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for idx, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{idx + 1} -- {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ") + "\n"
            todos[number - 1] = new_todo

            with open("todos.txt", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Please enter a digit!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todo_removed = todos[number-1].strip("\n")
            todos.pop(number-1)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            print(f"Todo {todo_removed} was removed from the list.")
        except ValueError:
            print("Your command is not valid. Please enter a digit!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")


print("Bye!!")
print(todos)

while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action == "add":
        todo = input("Enter a todo: ") + "\n"

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "show":
        with open("todos.txt", "r") as file:
            todos = file.readlines()

        for idx, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{idx + 1} -- {item}")

    elif user_action == "edit":
        number = int(input("Choose the number of the todo to edit: "))

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ") + "\n"
        todos[number - 1] = new_todo

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action == "complete":
        number = int(input("Number of the todo completed: "))

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todo_removed = todos[number-1].strip("\n")
        todos.pop(number-1)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        print(f"Todo {todo_removed} was removed from the list.")

    elif user_action == "exit":
        break


print("Bye!!")
print(todos)

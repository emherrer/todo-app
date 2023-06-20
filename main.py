from functions import get_todos, write_todos

while True:
    user_action = input("Type: add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        todos = write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for idx, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{idx + 1} -- {item}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("Enter new todo: ") + "\n"
            todos[number - 1] = new_todo

            todos = write_todos(todos)

        except ValueError:
            print("Your command is not valid. Please enter the corresponding digit!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todo_removed = todos[number-1].strip("\n")
            todos.pop(number-1)

            todos = write_todos(todos)

            print(f"Todo '{todo_removed}' was removed from the list.")

        except ValueError:
            print("Your command is not valid. Please enter the corresponding digit!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid!")


print("Bye!!")
print(todos)

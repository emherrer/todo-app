todos = []

while True:
    user_action = input("Type: add, show, edit, complete or exit.")
    user_action = user_action.strip()

    if user_action == "add":
        todo = input("Enter a todo: ")
        todos.append(todo)

    elif user_action == "show":
        for idx, item in todos:
            print(f"{idx + 1} -- {item}")

    elif user_action == "edit":
        pass

    elif user_action == "complete":
        pass

    elif user_action == "exit":
        break


print("Bye!!")

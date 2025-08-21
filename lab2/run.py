import json
import os

FILE = "data.json"

# Ensure file exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)


def load_data():
    """Load data safely, even if file is empty"""
    if os.path.getsize(FILE) == 0:  # if file is empty
        return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []  # return empty list if invalid JSON


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def create(item):
    data = load_data()
    data.append(item)
    save_data(data)
    print("Item added:", item)


def read():
    data = load_data()
    return data


def update(index, new_item):
    data = load_data()
    if 0 <= index < len(data):
        print("Updated:", data[index], "→", new_item)
        data[index] = new_item
        save_data(data)
    else:
        print("Invalid index")


def delete(index):
    data = load_data()
    if 0 <= index < len(data):
        removed = data.pop(index)
        save_data(data)
        print("Deleted:", removed)
    else:
        print("Invalid index")


# -------------------------
# Menu with match-case
# -------------------------
if __name__ == "__main__":
    while True:
        print("\n--- JSON CRUD Menu ---")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        match choice:
            case "1":
                task = input("Enter task: ")
                create({"id": len(read()) + 1, "task": task})

            case "2":
                print("All items:", read())

            case "3":
                index = int(input("Enter index to update: "))
                task = input("Enter new task: ")
                update(index, {"id": index + 1, "task": task})

            case "4":
                index = int(input("Enter index to delete: "))
                delete(index)

            case "5":
                print("Exiting...")
                break

            case _:
                print("Invalid choice, try again.")


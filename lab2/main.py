import json
import os
from jsonschema import validate as jv, ValidationError

file_path = "data.json"
schema_path = "schema.json"

# func to load data
def load_data():
    # check file exist or is not empty
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
    f = open(file_path, "r")
    try:
        return json.load(f)
    except json.JSONDecodeError:
        return []
    finally:
        f.close()

def validate_json(data_file, schema_file):
    s = open(schema_file, "r")
    schema_data = json.load(s)
    f = open(data_file, "r")
    file_data = json.load(f)
    try:
        jv(instance=file_data, schema=schema_data)
        print("data.json validated against schema.json")
    except ValidationError as e:
        print("Validation error:", e.message)
    finally:
        s.close()
        f.close()

def create(book, author):
    data = load_data()
    new_entry = {"book":book, "author": author}
    data.append(new_entry)
    f = open(file_path, "w")
    json.dump(data, f, indent=4)
    print("added new entry")
    f.close()

def delete_title(book_title):
    data = load_data()
    new_data = []
    removed = None

    for i in data:
        if i["book"] == book_title:
            removed = i
        else:
            new_data.append(i)
    if removed:
        f = open(file_path, "w")
        json.dump(new_data, f, indent=4)
        print(f"title {removed} removed!!")
        f.close()
    else:
        print("no entry found for the title")

def update(index, new_book, new_author):
    data = load_data()

    if 0 <= index < len(data):
        old = data[index]
        data[index] = {"book": new_book, "author": new_author}
        f = open(file_path, "w")
        json.dump(data,f , indent=4)
        print(f"updated data {data} at index {index}")
        f.close()
    else:
        print("invalid index to update")

def update_title(title, new_book, new_author):
    data = load_data()
    updated = False

    for i in range(len(data)):
        entry = data[i]
        if entry["book"] == title:
            old = entry.copy()

            data[i]["book"] = new_book
            data[i]["author"] = new_author

            updated = True
            break
    if updated:
        f = open(file_path, "w")
        json.dump(data,f, indent=4)
        f.close()
    else:
        print("no title found to update")

while True:
    print("\nMenu:")
    print("0. Validate")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choose an option (0-5): ")

    match choice:
        case "0":
            validate_json(file_path, schema_path)
        case "1":
            title = input("Enter the title: ")
            author = input("Enter the author: ")
            create(title, author)
        case "2":
            print(load_data())
        case "3":
            title = input("Enter the title to update: ")
            book = input("Enter the book: ")
            author = input("Enter the author: ")
            update_title(title,book,author)
        case "4":
            title = input("Title to be deleted: ")
            delete_title(title)
        case "5":
            print("Exiting...")
            break
        case _:
            print("Invalid choice, try again.")


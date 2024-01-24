Granth = {}

def add():
    key = input("Enter key: ")
    value = input("Enter value: ")
    Granth[key] = value
    print(f"Added Key: {key} , Value: {value}")

def search():
    key = input("Enter key to search: ")
    if key in Granth:
        value = Granth[key]
        print(f"{key}: {value}")
    else:
        print(f"'{key}' doesn't exist")

def remove():
    key = input("Enter key to remove: ")
    del Granth[key]
    print(f"'{key}' is removed")

while True:
    print("Add(1); Search(2); Remove(3); End(4)")
    choice = input("Select One : ")
    if choice=="1":
        add()
    elif choice=="2":
        search()
    elif choice=="3":
        remove()
    elif choice=="4":
        break
    else:
        print("Invalid Input!")

contacts = {}
id = 1

def menu():
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Search contacts")
    print("4. Remove contact")
    print("5. Edit contact")
    print("6. Exit")

def add_contact():
    global id

    firstname = input("first name: ")
    lastname = input("last name: ")
    phone = input("phone: ")
    email = input("email address: ")

    if not phone.isdigit():
        print("your phone number is not a number")
        return
    if "@" not in email:
        print("your email is not valid")
        return

    contacts[id] = {"firstname": firstname, "lastname": lastname, "phone": phone, "email": email}
    print(f"contact added successfully with id: {id}")
    id += 1

def show_contacts():
    if not contacts:
        print("o contacts added")
        return

    print("contacts list:")
    for contact_id, data in contacts.items():
        print(f"id: {contact_id}")
        print(f"firstname: {data['firstname']}")
        print(f"lastname: {data['lastname']}")
        print(f"phone: {data['phone']}")
        print(f"email: {data['email']}")

def search_contacts():
    value = input("search contact: ")
    found = False

    for contact_id, data in contacts.items():
        if data["firstname"] == value or data["lastname"] == value:
            print(f"id: {contact_id}")
            print(f"firstname: {data['firstname']}")
            print(f"lastname: {data['lastname']}")
            print(f"phone: {data['phone']}")
            print(f"email: {data['email']}")
            found = True

    if not found:
        print("Contact not found")

def remove_contact():
    try:
        contact_id = int(input("enter contact id: "))
        if contact_id not in contacts:
            print("contact not found")
        else:
            del contacts[contact_id]
            print(f"contact removed successfully with id: {contact_id}")
    except ValueError:
        print("ID not a number")

def edit_contact():
    try:
        contact_id = int(input("enter contact id: "))
        if contact_id not in contacts:
            print("contact not found")
            return

        newfirstname = input("first name: ")
        newlastname = input("last name: ")
        newphone = input("phone number: ")
        newemail = input("email address: ")

        if newfirstname:
            contacts[contact_id]["firstname"] = newfirstname
        if newlastname:
            contacts[contact_id]["lastname"] = newlastname
        if newphone:
            contacts[contact_id]["phone"] = newphone
        if newemail:
            contacts[contact_id]["email"] = newemail
        print(f"contact edited successfully with id: {contact_id}")

    except ValueError:
        print("ID not a number")

while True:
    menu()
    choice = input("enter choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        remove_contact()
    elif choice == "5":
        edit_contact()
    elif choice == "6":
        break
    else:
        print("invalid choice")
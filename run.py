import hashlib

def register_user(name, email, password):
    if email in users:
        return False # User already exists
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    users[email] = {'name': name, 'password': hashed_password}
    return True

def login_user(email, password):
    if email in users:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if users[email]['password'] == hashed_password:
             return users[email]['name']
    return None

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if register_user(name, email, password):
            print("Registration successful!")
        else:
            print("User already exists.")

    elif choice == '2':
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = login_user(email, password)
        if user:
            print(f"Welcome, {user}!")
        else:
            print("Login failed.")

    elif choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please choose again.")   
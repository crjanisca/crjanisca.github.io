# User Input

username = input("Enter a username: ")

username.find(" ")

username.isalpha()

if len(username) > 12:
    print("Username can't be more that 12 characters")
elif not username.find(" ") == -1 or not username.isalpha():
    print("Username cannot contain invalid characters (spaces, numbers)")
else:
    print(f"Welcome {username}")
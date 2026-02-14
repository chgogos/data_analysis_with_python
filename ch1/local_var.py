def greet():
    message = "Hello, world!"  # τοπική μεταβλητή 
    print(message)  


greet()  # ok
print(message)  # Error: NameError: name 'message' is not defined

name = input("Enter your name ")
len = len(name)
if len < 3:
    print("name must be al least 3 characters long")
elif len > 50:
    print("name can be a maximum of 50 characters long")
else:
    print("name looks good")
user = "Ali Akbar"

print(user)
print(user.upper())
print(user[0])
print(user.find("ali")) #-1 not found

users = ["Ali", "Akbar", "Imran Khan"]

print(users)

joined = "-"

print(joined.join(users))

say = "He said, \"I am learning Python\""

print(say)

# for paths we can use raw string
raw_string = r"c:\user\py\projects"

print(raw_string)

auth = "User is authenticate"

print("Auth" in auth)
users = ["Akbar", "Imran", "Ali", "Misbah"]

print(users)
print(users[-1])
print(users[2])
print(users[1:3])
print(users[:2])
print(users[2:])
print(users[3])

# users[1:3] = "Ronaldo"
users[1:3] = ["Ronaldo"]

for user in users:
    print(user)
    # print(user, end="-")

if "Akbar" in users:
    print("user logged in")

users.append("Ali Akbar")

print(users)

users.pop()

print(users)

users.remove("Akbar")

print(users)

users.insert(1, "New_User")
  
print(users)

# Separate ref in memory
users_copy = users.copy()

print(users_copy)
print(users_copy + users)
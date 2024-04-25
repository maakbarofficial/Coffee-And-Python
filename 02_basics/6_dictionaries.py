users = {"Akbar": "Admin", "Imran": "Mentor", "Misbah": "Coach"}
# users_2 = dict({"Akbar": "Admin", "Imran": "Mentor", "Misbah": "Coach"})

print(users)
# print(users_2)

print(users["Akbar"])

print(users.get("Akbar"))

for user in users:
    print(user, users[user])

for key, value in users.items():
    print(key, value)

if "Akbar" in users:
    print("Yes user available")

print(len(users))

users["Ronaldo"] = "GOAT"

print(users)

print(users.pop("Akbar"))

print(users)

print(users.popitem())

print(users)

del users["Misbah"]

print(users)

squared_nums = {x: x**2 for x in range(10)}

print(squared_nums)

squared_nums.clear()

print(squared_nums)

keys = ["Admin", "Mentor", "Coach"]
default_values = "Ali"
new_dict = dict.fromkeys(keys, default_values)

print(new_dict)

new_dict_2 = dict.fromkeys(keys, keys)

print(new_dict_2)

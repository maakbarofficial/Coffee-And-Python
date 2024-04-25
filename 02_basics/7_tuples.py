user_roles = ("admin", "user", "customer", "vendor", "marketer")

print(user_roles)

print(user_roles[0])
print(user_roles[1])
print(user_roles[-1])
print(len(user_roles))
# user_roles[0] = "super admin" # its immutable (fix in memory) so its can't change
print(user_roles)

more_users = ("regular customer", "new customer")

all_users = user_roles + more_users

print(all_users)

if "admin" in user_roles:
    print("Admin available")

print(user_roles.count("admin"))

print(type(user_roles))

print(("string", (1, 2, 3), ""))

# Tuples can also be nested like lists and dicts

# difference between tuple and list is, list is mutable and tuple is immutable

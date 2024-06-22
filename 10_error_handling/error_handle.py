# Two ways to handle files
file = open("youtube.txt", "w")

try:
    file.write("test")
finally:
    file.close()

with open("youtube.txt", "w") as file:
    file.write("test")

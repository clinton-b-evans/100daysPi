with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# W for write, A for append
with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")
with open("shopping_list.txt", "w") as f:
    f.write("apples\n")
    f.write("bananas\n")
    f.write("oranges\n")
    f.write("milk\n")
    f.write("bread\n")

with open("shopping_list.txt", "r") as f:
    print(f.read())

with open("shopping_list.txt", "a") as f:
    f.write("eggs\n")

with open("shopping_list.txt", "r") as f:
    print(f.read())

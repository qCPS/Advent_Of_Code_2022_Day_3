contents_file = open("contents.txt", "r")

backpacks = contents_file.readlines()

# test separating into groups of 3

groups = []

group_to_add = []

for i in range(len(backpacks)):
    backpack = backpacks[i].strip()
    group_to_add.append(backpack)
    if 2 == i % 3:
        groups.append(group_to_add)
        group_to_add = []

for group in groups:
    if len(group) != 3:
        print(group)

contents_file = open("contents.txt", "r")

backpacks = contents_file.readlines()


# Create a function to find the common item in a backpack
def get_common_item(backpack_to_check):

    # Finds the length of the backpack
    capacity = len(backpack_to_check)

    # Split the backpack in half
    compartment1 = backpack_to_check[0:capacity // 2]
    compartment2 = backpack_to_check[capacity // 2:]

    # Find the common item in both compartments
    for i in range(len(compartment1)):
        if compartment1[i] in compartment2:
            return compartment1[i]


# part 1

# Create a list to store the priorities of the common items
priorities = []

# Iterate over the elves' backpacks
for backpack in backpacks:

    backpack = backpack.strip()

    # Find the common item
    common_item = get_common_item(backpack)

    # Add the priority to the list of priorities
    if common_item.islower():
        priorities.append(ord(common_item) - 96)
    else:
        priorities.append(ord(common_item) - 38)

print(sum(priorities))

# Part 2

# Reset the list of priorities to empty
priorities = []

# Iterate over the elves' backpacks
for i in range(len(backpacks)):

    # Only check once per group
    if i % 3 == 0:

        # Set the backpack to be tested
        backpack = backpacks[i].strip()

        # Find the common item in the group
        for item in backpack:
            if item in backpacks[i + 1] and item in backpacks[i + 2]:
                common_item_in_group = item
                break

        # Add the priority of the item to the list of priorities
        if common_item_in_group.islower():
            priorities.append(ord(common_item_in_group) - 96)
        else:
            priorities.append(ord(common_item_in_group) - 38)

print(sum(priorities))

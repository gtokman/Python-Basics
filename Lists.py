# Lists

my_list = [1, 2, 3]

my_list += [4, 5]

print(my_list)

# Add items to list

# single item
my_list.append(6)

# Multiple items
my_list.extend([7, 8])

# Remove

my_list.remove(8)

print(my_list)

# List function - can send iterable objects into the list()

hello_list = list("hello")
print(hello_list)

# Split - breaks up a string

students = "gary ross luke".split()
colors = "red:green:blue".split(":")
print(colors)
print(students)

# Join() List to string only join string
flavors = ["chocolate", "mint", "strawberry"]
flavors_string = ", ".join(flavors)
print(flavors_string)

# Index

alpha = "abcd"
index = alpha.index("a")
index = alpha.index("c")
print(index)

# Delete

trash = 99
del trash

new_list = [1, 3, 2, 3]

print(new_list)


# Challenge 1

colors = ["red", "blue", "green", "yellow", "orange"]

states = [
    'ACTIVE',
    ['red', 'green', 'blue'],
    'CANCELLED',
    'FINISHED',
    5,
]

# Actual value to remove not index
states.remove(5)
states.remove(["red", "green", "blue"])


print(states)

# Challenge 2

available = "banana split;hot fudge;cherry;malted;black and white"

sundaes = available.split(";")

menu = "Our available flavors are: {}."

ice_cream = ", ".join(sundaes)

menu = menu.format(ice_cream)
print(ice_cream)

# Challenge 3

messy = [5, 2, 8, 1, 3]

del messy[2]
del messy[1]

print(messy)










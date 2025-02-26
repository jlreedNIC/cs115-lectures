# -----
# Data types and lists
# -----

a = 3
# b = "my name is jordan"
b = 6.5
c = "my name"

if a > b:
    print("something here")

print(type(a))
print(type(b))
print(type(c))

c = 5
print(type(c))

my_list = ["another string", 5, "my age", 5.67]
print(type(my_list))

# accessing a list
print(my_list[0])
print(my_list[3])

my_list.append("milk")
print(my_list)

# access first character in string
print(my_list[0][0])

# remove from string
my_list.remove(5)
print(my_list)
my_list.pop(2)
print(my_list)

# get length of list
print(len(my_list))

# exercise with list
todo_list = ["call mom", "walk the dog", "go to store"]
todo_list.append("read a book")
todo_list[1] = "finish homework"
todo_list.remove("call mom")
print(len(todo_list))

print(todo_list)

coordinates = [(100, 200), (200, 300)]

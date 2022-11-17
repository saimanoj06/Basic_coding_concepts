# print("Hello world")

# variables
x = "name"
x = 4
y = 22
z = 22.6
print(type(x))

# Assigning multiple values
x, y, z = ("John", '21', '21.5')
print(y)

# One value to multiple values

x = y = z = "Orange"
print(y)

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# print(x+y+z)
# print(x,y,z)

# Global Variables
z = 22
def myfun():
    print("My age is:", z)
myfun()

#######

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

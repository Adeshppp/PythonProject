print("hello world!")

print(4+553)

if(5>2):
    print("in if block")


x=5
y="hello"
print(x) # output integer
print(y) # output string

# This is comment


# print("dummy")
# print("dummy")
# print("dummy")
# print("dummy")
# print("dummy")



x,y,z = "orange","banana","apple"
print(z)

x=y=z = "orange"
print(x)
print(y)
print(z)


# unpack collection
fruits = ["orange","banana","apple"]
x,y,z = fruits
print(x)
print(y)
print(z)


# Output multiple variables
x="Python"
y="is"
z="Awesome!"
print(x,y,z)
print(x+y+z)

x = "awesome"
def myfunc():
    x="fantastic"
    print("Python is "+x)

myfunc()


def myfunc():
     global x
     x="fantastic"

myfunc()
print("Python is "+x)

print('hello','world')


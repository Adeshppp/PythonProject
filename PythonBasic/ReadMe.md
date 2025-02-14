Variable name rules:

1. must start with a letter or an underscore
2. cannot start with number
3. can only contain alphanumeric characters or underscore
4. Names are case-sensitive

Multiword variable names:
1. camel case : myVariableName
2. Pascal case : MyVariableName
3. snake case : my_variable_name

# Unpack collection
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




# Local varible
    def myfunc():
        x="fantastic"
        print("Python is "+x)
    myfunc()

# Global variable
    x = "awesome"
    def myfunc():
        print("Python is "+x)
    myfunc()

# with global keyword
    def myfunc():
        global x
        x="fantastic"
    
    myfunc()
    print("Python is "+x)


# Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

    Text Type:	str
    Numeric Types:	int, float, complex
    Sequence Types:	list, tuple, range
    Mapping Type:	dict
    Set Types:	set, frozenset
    Boolean Type:	bool
    Binary Types:	bytes, bytearray, memoryview
    None Type:	NoneType


# Python Numbers
There are three numeric types in Python:

    int : Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
    float : Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
    complex : Complex numbers are written with a "j" as the imaginary part:


Note: You cannot convert complex numbers into another number type.


### example
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

# String

strings in Python are arrays of bytes representing unicode characters.

    a = "Hello, World!"
    print(a[1])

### Looping through Strings

    for x in "banana":
        print(x)

### length in Strings

    a = "Hello, World!"
    print(len(a))

### check String

    txt = "The best things in life are free!"
    print("free" in txt)


#### example
    txt = "The best things in life are free!"
    if "free" in txt:
      print("Yes, 'free' is present.")


### Check if NOT

    txt = "The best things in life are free!"
    if "expensive" not in txt:
      print("No, 'expensive' is NOT present.")

### Slicing

    b = "Hello, World!"
    print(b[2:5])   // op : llo

Note: The first character has index 0.

### Slice From the Start
    b = "Hello, World!"
    print(b[:5]) // op: Hello

### Slice To the End

    b = "Hello, World!"
    print(b[2:]) // op: llo, World!

### Negative Indexing

    b = "Hello, World!"
    print(b[-5:-2]) // OP: ORL


## Modify strings
    a = "   Hello, World!"
    print(a.upper())
    print(a.lower())
    print(a.strip()) # remove whitespaces from start and end of a string
    print(a.replace("H", "J")) # Jello, World!
    print(a.split(",")) # returns ['Hello', ' World!']

## String Concatenation
    a = "Hello"
    b = "World"
    c = a + " " + b
    print(c)

## F-Strings
    age = 36
    txt = f"My name is John, I am {age}"
    print(txt)

## Placeholders and Modifiers
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print(txt) // op: The price is 59.00 dollars

A placeholder can contain Python code, like math operations:

    txt = f"The price is {20 * 59} dollars"
    print(txt) // op: The price is 1180 dollars

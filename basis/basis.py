# One line comment
'''
Multiline comment
'''

# It gets the type of a constant or variable. (int, float, boolean, etc)
type(2.2) 

# Assigning values tu variables
# a = 1
# a = "ff"
# a = b = c = 33
# z, x, y = 1, "hi", True


# Especial Python Operators 
print(2**5) # 2 power of 5
print(23//5) # division rounded down (4 instead of 4.6)

# Precedence
# () ** * / % + -

# Strings
example = "Hi people!"
print(len(example)) # 10
print(example[0]) # H
print(example[-1]) # !
print(example[0:4]) # the same as example[:3] (substring from one index to the other - 1)
print(example[3:]) # from one index to the end
print(example + " Yeah!")
print(example * 2) # concat repeating the string x times

print("Today I had {0} of {1}".format(2, "coffee"))
print("Today I had {x} of {y}".format(x = 2, y="coffee"))
print("{when} I had {0} of {1}".format(2, "coffee", when='Today'))

print("Fill the left with spaces {0:5}".format(1)) # The same as {:5}
print("{:<5} Fill the right with spaces".format(1))
print("{:f<5} Fill the right with f".format(1))

print("{:b}".format(21)) # Binary format
print("{:x}".format(21)) # Hexadecimal format
print("{:o}".format(21)) # Octadecimal format

# Raw strings and scape characters
print("I'm a string in python")
print("\"Something\"")
print(r"c:\nfdf\fdsf")

# multiline strings
print("""
        Something
        """)


# logica operators
# precedence (not, and, or) 
a = True
b = False

print( not a and b or b)

# If
if True:
    print("Something")
elif True:
    print("Something 2")
else :
    print("Something 3")

# Ternary operator
me = "Hi" if True else "Ha"
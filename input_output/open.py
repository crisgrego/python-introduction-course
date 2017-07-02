#open(filename, access mode, buffering)

## Read all file
# file = open("text.txt","r")
# print(file.read())
# file.close()

## Read certain number of characters
# file = open("text.txt","r")
# print(file.read(3)) # read 3 letters
# print(file.tell()) # indicates where's the cursor position
# file.close()

## Move cursor
# file = open("text.txt","r")
# file.seek(3) #moves the cursor to where we want
# print(file.read())
# file.close()

## Read line by line
# file = open("text.txt","r")
# for line in file:
#     print(line)
# file.close()

## Read attributes
# file = open("text.txt","r")
# print("File Name: " + file.name)
# print("Is closed: " + str(file.closed))
# print("Mode " + file.mode)
# file.close()

## Write to a file
# file = open("text2.txt","w+")
# file.write('Hey you!')
# file.seek(0)
# print(file.read())
# file.close()
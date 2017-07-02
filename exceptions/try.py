# try:
#     a = 5/0
# except Exception as e:
#     print(e)

# try:
#     n = int(input("Enter an Integer: "))
# except ValueError:
#     print("That is not an integer")

# try:
#     sum = 0
#     file = open('numbers.txt', 'r')
#     for number in file:
#         sum = sum + 1.0 / int(number)
#     print(sum)
# except ZeroDivisionError:
#     print("Number in fail equal to zero")
# except IOError:
#     print("File DNE")
# finally:
#     print(sum)
#     file.close()

0
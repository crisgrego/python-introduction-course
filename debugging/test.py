# To debug code directly from command prompt:
#   python -m pdb file_name.py
# or import pdb in the file and use "pdb.set_trace()" where you want the debugger to start
# then call the file from the console like:
#   python file_name.py
# commands:
# where - tells where we are in the code (alias: w)
# list - list 5 lines of code before and after the line where de debugger is activated
#   + list 3,6 - shows lines from line 3 to 6
#   + list 3,2 - show 2 lines starting at 3
# up - move to older procedures calls
# down - to move into new procedures calls
# args - give us the current scope variables
#   + to change de value of one of those variables we can use:
#     !variable_name = value
# step - continues de execution step by step moving into function bodies
# next - moves to the next statement
# until -
# return -
# l starting_line,ending_line - it shows a block of code
# continue - resumes de execution
# break line_number | function_name - creates a break point where we want
#   + break line_number, condition - to break only if a variable  fullfits a condition
# break - shows all the breakpoints in our program
# tbreak line_number | function_name - temporal break point
# disable break_point_num - disable one break point
# enable break_point_num - enables one break point
# clear break_point_num - it deletes a break point
# ignore break_point_num number_of_ignores - it ignores the break point certain amount of time
# commands break_point_num - executes a script when the execution reaches a break point
# jump line_number - skips other lines

import pdb

def fun1(a):
    if a % 2:
        return True
    else:
        return False
def fun2(x):
    if type(x) is int:
        pdb.set_trace()
        print(fun1(x))
    else:
        print('Not defined')

fun2(3)
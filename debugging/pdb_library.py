# To use the debug modul from our code
import pdb

print('Statement 1')
for i in range(5):
    print('Statement ' + str(i + 2))
# pdb.set_trace() # Call the debugger when the interpreter reach this code
print('Statement 7')
pdb.pm() # Calls the debugger after a crash
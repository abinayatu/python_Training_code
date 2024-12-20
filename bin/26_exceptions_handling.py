"""
Exceptions Handling
"""

# print("Without Handling Exceptions")
# print("-"*20)
# # --------------
#
# a = 10
# b = 0
# c = a/b # Program will terminate abruptly
# print("Value of c:", c)
#
# print("#"*40, end="\n\n")
# ################################

print("Handling Exceptions Using 'try-except'")
print("-"*20)
# --------------

try:
    # Keep the code which we are planning to monitor for error
    # If some error occurs here then it will execute 'except' block
    # If no error then 'except' block will be skipped
    pass
except:
    # Here, write code to solve error occurred in try
    pass


try:
    a = 10
    b = 0
    c = a/b # Program will NOT terminate, Instead it will goto except block
    print("Value of c:", c) # This statement will never execute because control will never comeback here
except:
    print("Reached except block")
    print("Here, we will write logic to solve error occurred in try")

print("#"*40, end="\n\n")
################################
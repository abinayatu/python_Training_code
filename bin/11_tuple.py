"""
Tuple:
        -- To keep multiple values like list of employee names
        -- We can keep duplicate values
        -- Automatically index number will be assigned to each value
"""

print("Tuple PART-1")
print("Store Multiple Values")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", (100, 200))
# It will create object of builtin class 'tuple' and store the values
print("my_tuple:", my_tuple, end="\n\n")

print("#"*40, end="\n\n")
################################

print("Tuple PART-2")
print("Indexes are similar to strings")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", (100, 200, "Java"))
print("my_tuple:", my_tuple, end="\n\n")

print("Course Name:", my_tuple[2]) # "python"
print("2nd char in Course Name:", my_tuple[2][1], end="\n\n") # "y"

print("Inner Tuple:", my_tuple[3]) # (100, 200, "Java")
print("Course name in Inner Tuple:", my_tuple[3][2]) # "Java"
print("2nd char in Course name in Inner Tuple:", my_tuple[3][2][3]) # "a"

print("#"*40, end="\n\n")
################################
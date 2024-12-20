print("Strings PART-7")
print("-ve Step Value: We can traverse in reverse direction")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Example: 6 to 1 in reverse direction
# Mandatory Steps:
# Condition-1: start index should be 6
# Condition-2: end index should be 1
# Condition-3: step value should be present and it should be negative step value
# If we miss any condition then we will not get OUTPUT

# Refer Example-3 in 5_strings.xlsx
print("sub string from index-6 to 1 using +ve index number, step by -1:", my_string[6:1:-1])
print("sub string from index-6 to 1 using -ve index number, step by -1:", my_string[-2:-7:-1], end="\n\n")
# Character at start index 6 will be included
# Character at end index 1 will be excluded

print("#"*40, end="\n\n")
################################
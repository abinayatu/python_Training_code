print("Strings PART-6")
print("Step Value: We can skip characters")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")

# Refer Example-2 in 5_strings.xlsx

print("Substring from index 1 to 6 using +ve index number, default step by 1:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index number, default step by 1:", my_string[-7:-2], end="\n\n")
# default step=1, which means from index-1 to 6, give me every character

print("Substring from index 1 to 6 using +ve index number, step by 1:", my_string[1:6:1])
print("Substring from index 1 to 6 using -ve index number, step by 1:", my_string[-7:-2:1], end="\n\n")
# step=1, which means from index-1 to 6, give me every character

print("Substring from index 1 to 6 using +ve index number, step by 2:", my_string[1:6:2])
print("Substring from index 1 to 6 using -ve index number, step by 2:", my_string[-7:-2:2], end="\n\n")
# step=2, which means from index-1 to 6, give me every 2nd character
# by default character at start index-1 will be included
# by default character at end index-6 will be excluded

print("#"*40, end="\n\n")
################################
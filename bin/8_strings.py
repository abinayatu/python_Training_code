print("Strings PART-5")
print("Slicing: We can get sub string")
print("-"*20)
# --------------

my_string = "WEL COME"
print("my_string:", my_string, end="\n\n")


print("Substring from index 1 to 6 using +ve index number:", my_string[1:6])
print("Substring from index 1 to 6 using -ve index number:", my_string[-7:-2], end="\n\n")
# always in slicing character at last index will not come
# Here, char at index-6 will not come
# If we want index-6 also then end index we need provide one extra i.e 7

print("Substring from index 1 to END using +ve index number:", my_string[1:])
print("Substring from index 1 to END using -ve index number:", my_string[-7:], end="\n\n")

print("Substring from BEGINNING to 6 using +ve index number:", my_string[:6])
print("Substring from BEGINNING to 6 using -ve index number:", my_string[:-2], end="\n\n")


print("#"*40, end="\n\n")
################################
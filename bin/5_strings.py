
print("Strings PART-2")
print("How to store values")
print("-"*20)
# --------------

my_file_path_1 = "C:\newfolder\test.py"
# By default: \n\t etc are having special meaning, \n will get replace witn newline
print("my_file_path_1 in non-raw format=", my_file_path_1, sep="\n", end="\n\n")


my_file_path_2 = r"C:\newfolder\test.py"
# r -> raw string -> No special meaning for \n\t etc
print("my_file_path_2 in raw format=", my_file_path_2, sep="\n", end="\n\n")

my_file_path_3 = repr(my_file_path_1) # convert to raw format
print("my_file_path_3: convert to raw format=", my_file_path_3, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
################################
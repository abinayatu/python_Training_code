print("using 'if-block' with str, list, tuple or any other collections")
print("-"*20)
# --------------

my_string = "Python"
my_list = ["Java", "C", 200, "Python"]

if (my_string != "Java") and (my_string.startswith("Pyt")) and ("tho" in my_string):
    print("All conditions are true for my_string:", my_string)

if "C" in my_list:
    print("Condition True for my_list:", my_list)

# if "Pyt" in my_list # WRONG, Exact value we can check

print("#"*40, end="\n\n")
################################

print("if block with dictionary")
print("-"*20)
# --------------

my_dictionary = {"duration": 5, "course": "python", "mode": "online"}
print("my_dictionary:", my_dictionary, sep="\n", end="\n\n")

# >>> my_dictionary.keys()
# dict_keys(['duration', 'course', 'mode'])
# >>>
if "course" in my_dictionary.keys():
    print("Key 'course' present")

# >>> my_dictionary.values()
# dict_values([5, 'python', 'online'])
# >>>
if "online" in my_dictionary.values():
    print("Value 'online' present")

# >>> my_dictionary.items()
# dict_items([('duration', 5), ('course', 'python'), ('mode', 'online')])
# >>>
if ('duration', 5) in my_dictionary.items():
    print("Item '('duration', 5)' Found")

print("#"*40, end="\n\n")
################################
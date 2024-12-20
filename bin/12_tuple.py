
print("Tuple PART-3")
print("Methods inside tuple class")
print("-"*20)
# --------------

print(dir(tuple))
# OR
# print(dir(tuple))

print("#"*40, end="\n\n")
################################

print("Tuple PART-4")
print("'count' and 'index' method")
print("-"*20)
# --------------

my_tuple = (10, 12.5, "python", "python", "python", (100, 200, "Java", "Java", "Java"))
print("my_tuple:", my_tuple, end="\n\n")

count_of_python = my_tuple.count("python")
index_of_python = my_tuple.index("python")
print("count_of_python:", count_of_python)
print("index_of_python:", index_of_python)


# my_tuple[-1] = (100, 200, "Java", "Java", "Java")
count_of_java = my_tuple[-1].count("Java")
index_of_java = my_tuple[-1].index("Java")
print("count_of_java:", count_of_java)
print("index_of_java:", index_of_java)

print("#"*40, end="\n\n")
################################
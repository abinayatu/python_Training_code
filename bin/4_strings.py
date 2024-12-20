"""
- Strings:
    -- We have option to store text data like name, email-id, word, sentence etc
    -- Automatically index number will be assigned to each character
"""

print("Strings PART-1")
print("How to store values")
print("-"*20)
# --------------

a = 'PERSON'
b = "PERSON'S"
c = 'PERSON\'S'
d = """PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)"""
e = '''PERSON'S HEIGHT IS XYZ" (" REPRESENTS INCHES)'''
f = """a"""

# In all the above cases, it will create object of builtin class 'str'
# and store the values

print(a, b, c, d, e, f, sep="\n")

print("#"*40, end="\n\n")
################################
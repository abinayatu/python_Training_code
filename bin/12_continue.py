print("# Case-2: 'continue-statement': We can skip the current iteration")
print("-"*20)
# --------------

my_courses_list = ["C++", "Java-1", "Python", "Java-2", "Perl"]
print("my_courses_list:", my_courses_list, end="\n\n")

for each_course in my_courses_list:
    # Below code till end of for-loop, will be applicable for java course
    # So, from this line, other than java course are not required
    if not each_course.startswith("Java"):
        continue
    print("This JAVA course name is:", each_course)
    print("This is one version of java")
    print("This Java course duration is 5 days", end="\n\n")

print("#"*40, end="\n\n")
################################
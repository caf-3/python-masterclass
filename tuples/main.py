# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Tomás", 21, "Male")

print(student.count("Tomás"))
print(student.index("Male"))

for x in student:
    print(x, end=", ")

if 21 in student:
    print()
    print("This student is 21 years old!")
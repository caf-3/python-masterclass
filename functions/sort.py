# sort = a method for lists
# sorted = a function for any iterable

students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krabs']
students_list = ('Squidward 01', 'Sandy 01', 'Patrick 01', 'Spongebob 01', 'Mr.Krabs 01')

students.sort(reverse=True)
sorted_students = sorted(students_list, reverse=True)

# for i in sorted_students:
#     print(i)

students_2d = [('Squidward', 'F', 60), ('Sandy', 'A', 33), ('Patrick', 'D', 36), ('Spongebob', 'B', 20), ('Mr.Krabs', 'C', 78)]
students_2d_list = (('Squidward', 'F', 60), ('Sandy', 'A', 33), ('Patrick', 'D', 36), ('Spongebob', 'B', 20), ('Mr.Krabs', 'C', 78))


age = lambda ages: ages[2]
# students_2d.sort(reverse=True)
students_2d.sort(key=age)
sorted_students_2d_list = sorted(students_2d_list, reverse=False, key=age)

for i in sorted_students_2d_list:
    print(i)
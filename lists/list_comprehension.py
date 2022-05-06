# formulas:
# list = [expression for item in iterator]
# list = [expression for item in iterator if conditional]
# list = [expression if/else for item in iterator]
#

students_marks = [20, 12, 16, 11, 5, 8, 9, 11, 7, 10, 8.2, 9.7 ]

squares = [i * i for i in range(1, 11) ]

# marks above 8
approved_marks = [i for i in students_marks if i > 8]

# renamed marks
results = [i if i > 8 else 'FAILED' for i in students_marks]

print(results)
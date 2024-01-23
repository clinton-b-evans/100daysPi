import random
numbers = [1,2,3,5,11]
new_numbers = [n * 3 for n in numbers]
print(numbers)
print(new_numbers)


name = "Clinton"
new_list = [letter for letter in name]
print(name)
print(new_list)

for n in range(1,5):
    n *= 2
    print(n)


range_list = [n * 2 for n in range(1,5)]
print(range_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_case_names = [name.upper() for name in names if len(name) > 5]

student_scores = {student:random.randint(1,100) for student in names}

passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)

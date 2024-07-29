# List comprehension day-26

numbers = [1, 2, 3]
# new_list = [new_item for item in list]
new_list = [ n+1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

number_range = range(1, 5)
numbers_list = [n*2 for n in number_range]
print(numbers_list)

# Conditional List Comprehension

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]
short_names = [name for name in names if len(name) <5]

long_names_upper = [name.upper() for name in names if len(name) >=5]
print(long_names_upper)

# Squaring Numbers

number_range_A = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
numbers_list_A = [n*n for n in number_range_A]
print(f"Squaring Numbers {numbers_list_A}")

# Filtering Even Numbers

filtered_numbers_list = [n for n in number_range_A if (n%2 == 0)]
print(f"Filtering Even Numbers {filtered_numbers_list}")

# Data Overlap

with open("file1.txt") as file1:
    list1 = file1.readlines()
    filtered_numbers_list_1 = [n.strip() for n in list1]
    print(filtered_numbers_list_1)

with open("file2.txt") as file2:
    list2 = file2.readlines()
    filtered_numbers_list_2 = [n.strip() for n in list2]
    print(filtered_numbers_list_2)

result = [int(num) for num in filtered_numbers_list_1 if num in filtered_numbers_list_2]

print(f"Data Overlap {result}")

# Dictionary Comprehension
import random
# new_dict = {new_key : new_value for item in list}

# new_dict = {new_key : new_value for (key, value) in dict.items()}
# new_dict = {new_key : new_value for (key, value) in dict.items() if test}

names_1 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie" ]

students_score = { student: random.randint(30, 100) for student in names_1}

print(students_score)

passed_students= { student:score for (student, score) in students_score.items() if score>= 65

}

passed_students_1= { key:value for (key, value) in students_score.items() if value>= 65

}
print(passed_students)
print(passed_students_1)

# Dictionary comprehension example 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_1 = sentence.split()
new_dict = { item : len(item) for item in list_1}
print(new_dict)


weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day : (temp_c*9/5)+32 for (day, temp_c) in weather_c.items()}
print(weather_f)

questions = [
  "Hello World",
  "Idle ",
  " Geometry "
]

# Map
cleaned_questions = list(map(lambda q: q.strip().capitalize(), questions))
print(cleaned_questions)

# Map One-Line
cleaned_questions_one_line = [q.strip().capitalize() for q in questions]

print(cleaned_questions_one_line)

# Filter
numbers = [1,2,3,4,5,6,7]
filtered_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(filtered_numbers)

# Filter One-Line
filtered_numbers_one_line = [n for n in numbers if n % 2 == 0]
print(filtered_numbers_one_line)


# Zip
x_axis = [0, 1, 2]
y_axis = [10, 30, 50]

xy_coordinates = list(zip(x_axis, y_axis))

print(xy_coordinates)

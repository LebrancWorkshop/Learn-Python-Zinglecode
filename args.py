# args kwargs

# args -> receive arguments and return as a tuple.

def sum_of_all(*numbers):
  return sum(numbers)

print(sum_of_all(1,2,5))

# kwargs -> receive argunemts and return as a dictionary
def get_user_information(**users):
  name = users.get('name')
  level = users.get('level')
  is_valid = False

  if name is not None and len(name) > 0 and len(name) <= 20:
    is_valid = True
  if level is not None and level >= 0 and level < 100:
    is_valid = True

  print(is_valid)

get_user_information(name='John', level=10)

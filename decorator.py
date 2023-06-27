import math

def capsule(function):
  def new_function():
    print("Armored Equiped")
    function()
    print("Equiped Success")
  return new_function

@capsule
def megaman():
  print("Megaman")

@capsule
def zero():
  print("Zero")

megaman()
zero()

def summation(function):
  def result(*args, **kwargs):
    return sum(function(*args, **kwargs))
  return result 

@summation
def numbers(operand1, operand2):
  return operand1, operand2

@summation
def infinite_numbers(*operands):
  return operands


print(numbers(1, 2))

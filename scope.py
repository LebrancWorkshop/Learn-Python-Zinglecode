global01 = "Global 01"

def scope_test():
  local01 = "Local 01"
  local02 = "Local 02"
  print(global01 + local01)
  print(global02 + local02)

global02 = "Global 02"

scope_test()
# print(local01)

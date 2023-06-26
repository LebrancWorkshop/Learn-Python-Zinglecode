import time

start = time.time()

for i in range(10000000):
  print(i)

end = time.time()

time_count = end - start
print("Time taken: {}".format(time_count))

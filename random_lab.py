import random

for i in range(1, 1000):
  result = random.randint(1, 100)
  print(result)

datasets = []
for i in range(1, 1000):
  data = random.uniform(0, 100)
  datasets.append(data)

print(datasets)

members = ["Iori", "Hina", "Miko", "Ueno", "Sakurakoji"]
result = random.choice(members)
print(result)

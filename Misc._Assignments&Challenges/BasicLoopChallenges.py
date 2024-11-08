i = 1

#While Loops

while i < 6:
  print(i)
  i += 1

print("-----Next Statement-----")

i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1

print("-----Next Statement-----")

i = 0
while i < 6:
  i += 1
  if i == 3:
    print("3, then continue")
    continue
  print(i)

print("-----Next Statement-----")

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

print("-----Next Statement-----")

#For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print("-----Next Statement-----")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("-----Next Statement-----")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    print("banana, then continue")
    continue
  print(x)

print("-----Next Statement-----")

for x in range(2, 6):
  print(x)

print("-----Next Statement-----")

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("-----Next Statement-----")

#Loop an Array Challenge

name = 'Python'

print(len(name))

for i in enumerate(name):
    print(i)



























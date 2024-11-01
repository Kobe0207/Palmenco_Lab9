rows = input("Enter the number of rows: ")

p = 1
for i in range(int(rows)):
  for j in range(i + 1):
    print(p , end=" ")
    p += 1
  print()
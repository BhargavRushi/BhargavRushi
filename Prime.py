def Prime(n):
  count = 0
  for i in range(2,n//2):
    if n%2 == 0:
      count = 0
      break;
  if count == 0:
    print('Prime')
  else:
    print('Not Prime')

print(prime(11))
print(prime(10))

increment = True
a = 1
counter = 0
primes = 0
while increment == True:
  a = a + 1
  b = a 
  checking_prime = True
  while checking_prime == True:
    c = a % b
    if c == 0:
      counter = counter + 1
      if counter == 2 and b == 1:
        counter = 0
        primes = primes + 1
        print(a)
        checking_prime = False
      elif counter > 2:
        checking_prime = False
        counter = 0
    elif primes == 100:
      increment = False
    b = b - 1
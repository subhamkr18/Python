def fizzbuzz(n: int) -> None:
  if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
  elif n % 3 == 0:
    print("Fizz")
  elif n % 5 == 0:
    print("Buzz")
  else:
    print(n)

fizzbuzz(15) 
fizzbuzz(9)   
fizzbuzz(10)  
fizzbuzz(7)   
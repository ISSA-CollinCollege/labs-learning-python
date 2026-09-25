# For a number that is divisble by 3, say Fizz.
# For a number that is divisible by 5, say Buzz.
# For a number divisible by both, say FizzBuzz

def Fizz_Buzz():
    i = 0
    while i < 51:
        
        if i % 3 == 0 and i % 15 == 0:
            print("FizzBuzz")
            i+=1
        elif i % 3 == 0:
            print("Fizz")
            i+=1
        elif i % 5 == 0:
            print("Buzz")
            i+=1
        else:
            print(i)
            i+=1
        

Fizz_Buzz()
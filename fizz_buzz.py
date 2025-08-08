#Declaración de variables
num=1
limit=1000
while num <= limit:
    if num%3 == 0 and num%5==0:
        print("Fizz Buzz")
    elif num%5 == 0:
        print("Fizz")
    elif num%3 == 0:
        print("Buzz")
    else:
        print(num)
    num = num + 1
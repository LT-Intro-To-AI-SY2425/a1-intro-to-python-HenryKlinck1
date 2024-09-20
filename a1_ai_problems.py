# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
print("all tests good")

def celsius_calculation(celsius):
    return (celsius * 9/5) + 32

def calculate():
    celcius = 0
    celsius = float(input("Enter temperature in Celsius: "))
    while celcius != 0
        fahrenheit = celsius_calculation(celsius)
        print(celcius_calculation)
    else:
        print("use a real number.")




def sum_of_digits(n):
    lst = []
    return sum(int(digit) for digit in lst(n))
    result = sum_of_digits(number)
    print("The sum of the digits of {number} is {result}.")

assert sum_of_digits[1,2,3] == 6, "sum of digits failed"
print("test worked")



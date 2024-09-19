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

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("use a real number.")

if __name__ == "__main__":
    calculate()

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
    result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {result}.")

    
    assert sum_of_digits[1,2,3] == 6, "sum of digits failed"



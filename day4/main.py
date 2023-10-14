def sayHello():
    # print('Bussiness logic here!')
    return 'Hello return'

sayHello()
sayHelloVariable = sayHello()
print(sayHelloVariable)

# def square(number):
#     result = number * number
#     return result

# # You can call the function like this:
# number = 5
# result = square(number)
# print(f"The square of {number} is {result}")

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# # You can call the function like this:
# number = 6
# if is_even(number):
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# def factorial(n):
#     if n < 0:
#         return "Factorial is undefined for negative numbers."
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # You can call the function like this:
# number = 3
# result = factorial(number)
# print(f"The factorial of {number} is {result}")


def hello(name):
    return 'Hello ' + name + '!'

helloAmin = hello('Fajri')
print(helloAmin)


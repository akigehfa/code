# def sayHello():
#     # print('Bussiness logic here!')
#     return 'Hello return'

# sayHello()
# sayHelloVariable = sayHello()
# print(sayHelloVariable)

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


# def hello(name):
#     return 'Hello ' + name + '!'

# helloAmin = hello('Fajri')
# print(helloAmin)

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print(f"{self.name} is barking")

# my_dog = Dog("Fido", "Labrador")
# my_dog.bark()

# class MyClass:
#     def __init__(self):
#         self.public_var = 42
#         self._protected_var = 23
#         self.__private_var = 15

# obj = MyClass()
# print(obj.public_var)      # Accessible
# print(obj._protected_var)  # Accessible, but conventionally considered protected
# print(obj.__private_var)   # Name mangling, not directly accessible


# def average(listInput):
#     sum = 0
#     for element in listInput:
#         sum = sum + element
#     return sum / len(listInput)
# print(average([1,2,3,4,5]))

# def maximum(listData):
#     if not listData:
#         return None
#     maximum = listData[0]
#     for number in listData:
#         if number > maximum:
#             maximum = number
#     return maximum

# print(maximum([12,32,43,13,75,42]))

def add(a, b):
    return a + b

print(add(5, 2))

def decrease(a, b):
    return a - b

print(decrease(9, 4))

def divide(a, b):
    return a / b

print(divide(8, 2))

def multiplication(a, b):
    return a * b

print(multiplication(78, 23))


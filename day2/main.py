import os
# print (list(range(10)))

# print(list(range(2,8)))

# print(tuple(range(2,20,3)))

# for i in range(4):
#     print(i)

# for i in range(2,5):
#     print(i)

# for i in range(2,10,2):
#     print(i)

# i = 5
# while i > 0:
#     print(i)
#     i = i - 1

# i = 0
# while True:
#     print(i)
#     i= i + 1
#     if i == 10:
#         break


# while True:
#     os.system('clear')
#     print('=========================================Welcome=========================================')
#     print('Options : ')
#     print('1. Enter your name : ')
#     print('2. Exit')
    
#     option = input('Input your option : ')
#     if option == '2':
#         print('Thank you!')
#         break

# sum = 0
# i = 1
# n = 4
# statement = True
# while i <= n and statement : 
#     sum = sum + 1
#     i = i + 1

# print('The sum is', sum)

# items = {'banana', 'apple', 'grapes'}
# for data in items :
#     print(data)
#     for item in items :
#         print(item)

# name = 'Derta Isyajora'
# for character in name :
#     print(character.upper())

# colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# print(colors[3])

# colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
# colors[2] = 'purple'

# print(colors[3])

# del colors[2]
# print(colors)

# nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(nums[4: 1: -1])
# nums[:4] = [1, 2, 3, 4]
# print(nums)

nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# del nums[3: 7]
# print(nums)
del nums[1:7:2]
print(nums)

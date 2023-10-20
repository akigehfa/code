# data = 10
#  print(data)

# randomList = ['a', 0, 2]

# try:  
#     print(randomList[3])

# except Exception as e:
#     print("some error")
#     print(e.__class__)


# x = 5
# a = 0
# try:
#     y
#     xx = int(input("Enter a number: "))
#     x == '5'
#     x / a

# except ValueError:
#     print("value")
#     pass

# except (TypeError, ZeroDivisionError):
#     print("tes")
#     pass

# except:
#     print('general')
#     pass


# numbers = [1, 10, -1, 11]
# # try:
# for number in numbers:
#     if number <= 0:
#         raise ValueError("That is not a positive number!")
# # except ValueError as ve:
#     # print(ve)


# try:
#     # 2 / 0
#     numbers = [1, 10, -1, 11]
#     for item in range(4):
#         print(numbers[item])
# except Exception as e:
#     print(e)
# finally:
#     print("all is well")


class Hero():
    def __init__(self, name, attribute, type):
        self.name = name
        self.attribute = attribute
        self.type = type
 
sniper = Hero("Sniper", "Agility", "Ranged")
print("Hero : {}".format(sniper.name))
print("Attribute : {}".format(sniper.attribute))
print("Type : {}".format(sniper.type))
# class Dog :

#     eye = 2
#     leg = 4

#     def __init__(self, name) :
#         self.name = name

#     def introduce(self) :
#         print("Hi this dog is called {}".format(self.name))

# cerberus = Dog('jahannam cerberus')
# print(cerberus.introduce())

# attributes = dir(cerberus)
# print(attributes)

# empty_obj = object()
# cerberus_attributes = [attr for attr in dir(cerberus) if attr not in dir(empty_obj)]
# print(cerberus_attributes)

# cerberus.name = 'bleki'
# print(cerberus.name)


class Dog :

    __ordo = 'Carnivora'

    def __init__(self, name) :
        self.name = name 
        # self.introduce()

    def sound(self) :
        print('hoff hoff')

    def introduce(self) :
        print("His name is {}".format(self.name))
        return 1

    def setOrdo(self, ordo) :
        self.__ordo = ordo
    
    def getOrdo(self) :
        print(self.__ordo)



dog = Dog("buddy")
# print(dog.introduce())


# dog.sound()

# dog.ordo = 'Herbivora'

# print(dog.ordo)
dog.getOrdo()

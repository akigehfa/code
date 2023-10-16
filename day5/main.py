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


# class Dog :

#     __ordo = 'Carnivora'

#     def __init__(self, name) :
#         self.name = name 
#         # self.introduce()

#     def sound(self) :
#         print('hoff hoff')

#     def introduce(self) :
#         print("His name is {}".format(self.name))
#         return 1

#     def setOrdo(self, ordo) :
#         self.__ordo = ordo
    
#     def getOrdo(self) :
#         print(self.__ordo)



# dog = Dog("buddy")
# print(dog.introduce())


# dog.sound()

# dog.ordo = 'Herbivora'

# print(dog.ordo)
# dog.getOrdo()


# class Parent:
#     def __init__(self) -> None:
#         self.var = 10
#         pass
    
#     def method1(self):
#         print('Hello')
#         pass

#     def method2(self):
#         pass

# class Child(Parent):

#     def childMethod(self):
#         print('Anak')
#         pass

# child = Child()
# child.method1()
# child.childMethod()

# class Hero:

#     basicMovementSpeed = 10

#     def __init__(self, basicAttack = 10) -> None:
#         self._basicAttack = basicAttack
#         pass

#     def hit(self):
#         print('Hit')
#         pass

#     def spell(self):
#         print('Spell')

# invoker = Hero()
# invoker.hit()
# invoker.spell()

# class HeroRange(Hero):

#     def hit(self):
#         print('Throw attack')

#     def hit(self, range):
#         print('Throw attack with bonus damage', range)


# drowRanger = HeroRange()
# # drowRanger.hit()
# # drowRanger.hit()
# print(drowRanger._basicAttack)

# class Kasur(Hero):

#     def sayHello(self):
#         hero = Hero()
#         print('Hello', hero._basicAttack)

# kasur = Kasur()
# kasur.sayHello()
# print(kasur._basicAttack)

# class Person:
#     def __init__(self, name) -> None:
#         self.name = name
#         self._age = 10
#         pass

# class Employee(Person):
#     def introduce(self):
#         print("Hello everyone, my name is {}".format(self.name))

# derta = Employee("derta isyajora")
# print(derta._age)

# class NotChild:
#     def sayHello(self):
#         joko = Employee("Joko")
#         print("hellok", joko._age)

# desta = NotChild()
# print(desta.sayHello())

class MyClass:
    def __init__(self):
        self._protected_variable = 42

    def _protected_method(self):
        print("This is a protected method.")

class SubClass(MyClass):
    def __init__(self):
        super().__init__()

    def call_protected(self):
        print(self._protected_variable)
        self._protected_method()

# Outside the class
my_instance = SubClass()
my_instance.call_protected()

class Parent:
    classmethods and attrs
class Child(Parent):
    classmethods and attrs
class Parent:
    classmethods and attrs
class Child(Parent):
    classmethods and attrs
class Human:
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass
nick = Student(Human)
ann = Worker(Human)
print(nick.height)
print(ann.height)
class Grandparent:
    height = 170
    satiety = 100
    age = 60
class Parent(Grandparent):
    age = 40
class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)
nick = Child()
class Hello_world:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"
    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)
class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_print()

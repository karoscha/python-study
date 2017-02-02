# -*- coding: utf-8 -*-
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def personInfo(self):
        print('name={}, age={}, gender={}'.format(self.name,self.age,self.gender))

person = Person('karoscha', '36', '남')
person.personInfo()


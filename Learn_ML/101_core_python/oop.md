# OOP
```
class Person(object):
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.instance_method()

    def instance_method(self):
        print('success!')

personObj = Person()
```

> Object -> Class -> Metaclass
```
__new__
__init__
```

# str() vs repr()
```
s = 'Hello'
> str(s)    #-> 'Hello'
> repr(s)   #-> "'Hello'"  official str representation 

class A:
    def __str__(self):
        return ""

    def __repr__(self):
        return ""

o = A()
str(o)
repr(o)
```


# Operator Overloading: [when we use + operator, the magic method __add__ is automatically invoked]
```
dir(int) or dir(float)

> print(1 + 2)
> print("1" + "2")

> v1 = int(6)
> v2 = int(5)
> v1.__add__(v2)


import operator
print (operator.add(a, b))
operator.pow(a,b)
```


# Inheritance
```
1. Single
2. Multiple
3. Multilevel
4. Hierarchical
5. Hybrid

class A:
    def __init__(self):
        pass

class B(A):
    def __init__(self):
        A.__init__(self)
        pass
```


# Encapsulation
```
1. Private
2. Protected
3. Public

class A:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 50 

o = A()
o.a     # ok
o._b    # ok
o.c     # not ok
```


# Class method
```
class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
```


# Static method
```
class C(object):
    @staticmethod
    def fun(arg1, arg2, ...):
```


# Polymorphism
Method Overriding: It is Run time polymorphism.
```
class A:
    def m(self);
        pass
class B(A):
    def m(self):
        pass
```
Method Overloading: It is Compile time polymorphism. Python does not support method overloading
```
m(1, 2)
m(20)
```


# Abstract Classes
A class which contains one or more abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have an implementation.
```
from abc import ABC, abstractmethod

class A:
    @abstractmethod
    def m(self):
        pass
```


# The @property Decorator
```
property(fget=None, fset=None, fdel=None, doc=None)

class A:
    def __init__(self):
        self.age = 0

    def get_age(self):
        return self.age
     
    def set_age(self, a):
        print("setter method called")
        self._age = a
  
    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age) 


######  OR  ######

class A:
    def __init__(self):
        self.age = 0

    def get_age(self):
        return self.age
    
    @age.setter
    def set_age(self, a):
        print("setter method called")
        self._age = a
  
    def del_age(self):
        del self._age


mark = A()
mark.age = 10
print(mark.age)
```


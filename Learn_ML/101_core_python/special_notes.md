# How a Python code works?
When you execute the python app.py command, Python interpreter (CPython) compiles 
the app.py into machine code.
The operating system (OS) needs to load the program into the memory (RAM) to run the program.
Once the OS loads the program to memory, it moves the instructions to the CPU for execution via bus.
In general, the OS moves the instructions to a queue, also known as a pipeline. Then, the CPU will execute the instructions from the pipeline.
By definition, a process is an instance of a program running on a computer. And a thread is a unit of execution within a process.

https://www.pythontutorial.net/python-concurrency/differences-between-processes-and-threads/


# Namespace
```
    Namespace: built-in -> global -> local
```

# what is __ name __ ?
```
# File1.py 
print ("File1 __name__ = %s" %__name__)  # __main__  during direct
if __name__ == "__main__": 
    print ("File1 is being run directly")
else: 
    print ("File1 is being imported")


import File1 
print ("File2 __name__ = %s" %__name__)  # File1  during imported
if __name__ == "__main__": 
    print ("File2 is being run directly")
else: 
    print ("File2 is being imported")
```

# Monkey Patching
```
# monk.py
class A:
	def func(self):
		print ("func() is being called")

import monk
def monkey_f(self):
     print ("monkey_f() is being called")

monk.A.func = monkey_f
obj = monk.A()
obj.func() # -> monkey_f() is being called
```


# Method used for List, Tuple, Dict, Set
```
List.append('value')
List.index(0, 'value')
List.extend([100000, 'v1'])
List.reverse()
List.remove('value')
List.pop(0)
List.clear()
List.sort()
List.copy()
List.reverse()

len(List)
sum(List)
max(List)
enumerate(List)
List5 = List1 + List2
```

```
len(Tuple)
sum(Tuple)
max(Tuple)
enumerate(Tuple)
Tuple5 = Tuple1 + Tuple2
```

```
Set = set()
Set.add('value')
Set.update(['v1', 'v2'])
Set.remove('value')
Set.pop()
Set.copy()
Set.clear()
```

```
Dict = dict(v1='k1', v2='k2')
Dict = {'v1': 'k1', 'v2': 'k2'}
Dict.update({'key': 'Value'})
Dict.get('v1')
Dict.items()
Dict.keys()
Dict.values()

>>> for k, v in d1.items():
...     print(k, v)

Dict.copy()
Dict.pop()
```


# global variables
```
h=6

def m():
    h=9
    print(h) # -> 9 

m()
print(h) # -> 6
```

```
h=6

def m():
    global h
    h = h + 1
    print(h) # -> 7

m()
print(h) # -> 7
```


# Python Function notes
1. Python functions are first class objects
```
def m2():
    retun "Hello World"

m2()
ref = m2
ref()
```
2. Functions can be passed as arguments to other functions. Functions that can accept other functions as arguments are also called higher-order functions 
[Known as Python Closures]
```
def m2():
    retun "Hello World"

def m1(fun):
    res = fun()
    print(res)
  
m1(m2)
```
3. Functions can return another function
```
def m1(x):
    def m2(y):
        return x+y
    return m2
  
m5 = m1(15)
print(m5(10))
```

> Dunder Methods
Dunder methods or Magic methods are those that have two underscores __ before and after the method


> Anonymous Function
```
z = lambda x, y: x+y
z(5, 5)
```


> Generator Function
1. Memory Efficient
2. Represent Infinite Stream
3. Pipelining Generators
```
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))
```

```
>>> def gf():
...     yield 1
...     yield 2

x=gf()
x.__next__()
x.__next__()


for i in gf():
    print(i)
```

> Filter/Map Function
```
a = [100, 2, 8, 60, 5, 4, 3, 31, 10, 11]
filtered = filter (lambda x: x % 2 == 0, a)
print(list(filtered))


mapped = map (lambda x: x % 2 == 0, a)
print(list(mapped))
```

> Decorator
```
@demo_decorator
def hello_decorator():
    print("Gfg")

Equivalent to:

ref = demo_decorator(hello_decorator)
ref()



@decorator(params)
def func_name():
    ''' Function implementation'''


Ex-1:
def print_time(func):
    def wrap():
        print(1)
        func()
        print(2)
    return wrap

@print_time
def m():
    print("=======")
    return 55

m()


Ex-2:
def print_time(func):
    def wrap(x, y):
        print(1)
        func(x, y)
        print(2)
    return wrap

@print_time
def m(x1, y1):
    print("=======", x1*y1)
    return 55

m(5, 10)
```

> iter/next
```
>>> def gf():
...     yield 1
...     yield 2

x=gf()
x.__next__()
x.__next__()

l = [4, 7, 0, 3]
my_iter = iter(l)
my_iter.__next__()
```



# File Handling
>  there is no need to call file.close() when using with statement. The with statement itself ensures proper acquisition and release of resources
```
fp = open("path/file-name.txt", 'r')  OR  fp = open("path/file-name.txt", 'rb')
fp.write()
fp.tell()
fp.seek(0)
fp.read(5)
fp.readline()
fp.readlines()
fp.close()

with open("path/file-name.txt", 'w') as fp  OR  with open("path/file-name.txt") as fp:
    fp.write(data)
    fp.writelines(data)
```


# Collections
> Counter
```
from collections import Counter 

l = ['B','B','A','B','C','A','B','B','A','C']
counter = Counter()
print(counter)
```

> OrderedDict/defaultdict
```
from collections import OrderedDict, defaultdict

od = OrderedDict()
od['k'] = 'v'

dd = defaultdict(list) 
print(dd['key']) # [] --> default one
```

> Deque
```
from collections import deque

l = ['B','B','A','B','C','A','B','B','A','C']
dequeue = deque(l)
dequeue.append(4)
dequeue.appendleft(4)
dequeue.pop()
dequeue.popleft()
```


# Exception Handling
```
try:
    # Some Code
except:
    # Executed if error in the try block
else:
    # execute if no exception
finally:
    # Some code .....(always executed)

if x>y:
    raise ValueError('custom message')


class CustomError(Exception):
    pass

raise CustomError("custom message")
```


# Multi-threading
In context switching, the state of a thread is saved and state of another thread is loaded whenever any interrupt (due to I/O or manually set) takes place. Context switching takes place so frequently that all the threads appear to be running parallelly (this is termed as multitasking)

threading module provides a Lock class to deal with the race conditions. Lock is implemented using a Semaphore object provided by the Operating System

```
import threading

def print_cube(num):
    print("Cube: {}" .format(num * num * num))
    print(threading.current_thread().name)
    lock.acquire()
    increment()
    lock.release()

lock = threading.Lock()
t1 = threading.Thread(target=print_cube, args=(10, lock), name='t1')
t2 = threading.Thread(target=print_cube, args=(20,), name='t2')
t1.start()
t2.start()

# wait until thread 1 is completely executed
t1.join()
```


# Multi-Processing
```
import multiprocessing

def print_cube(num):
    print("Cube: {}" .format(num * num * num))

p1 = multiprocessing.Process(target=print_square, args=(10, ))
p2 = multiprocessing.Process(target=print_cube, args=(10, ))
p1.start()
p2.start()

# wait until process 1 is finished
p1.join()
```


# Python Package
```
game
|
├── image
│   ├── change.py
│   ├── __init__.py
│   └── open.py
├── __init__.py
├── level
│   ├── __init__.py
│   ├── load.py
│   └── start.py
└── sound
    ├── __init__.py
    ├── load.py
    └── play.py

from game.level import start
from game.level.start import function_name
```



# async
```
import asyncio

async def square(number):
    return number*number

square(10) # don't wait

result = asyncio.run(square(10))  # wait
print(result)

###### OR ######

async def main():
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')

    task_1 = asyncio.create_task(call_api())
    task_2 = asyncio.create_task(call_api())

    if not task2.done():
        print('Cancelling the task...')
        task2.cancel()

asyncio.run(main())
```


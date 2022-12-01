import sys
import timeit
a = (1,2,3,4,5,6,7,8,9)
b = list(a)

def func_1(a,b):
	print('#1')
	print(type(a),type(b))
	print(sys.getsizeof(a),sys.getsizeof(b))

def func_2(a,b):
	print('#2')
	c = a + a;
	d = b + b;
	print(type(c),type(d))
	print(sys.getsizeof(c),sys.getsizeof(d))

def func_3(a):
	print('#3')
	c = set(a)
	d = frozenset(a)
	print(type(c),type(d))
	print(sys.getsizeof(c),sys.getsizeof(d))

def func_4():
	print('#4')
	class Point: 
		x: int 
		y: int
		def __init__(self,x,y):
			self.x = x;
			self.y = y;
	class Base:
		__slots__ = ('x','y',)
		x:int
		y:int
		def __init__(self,x,y):
			self.x = x;
			self.y = y;
	a = Point(1,1)
	b = Base(1,1)
	print(type(a),type(b))
	print(sys.getsizeof(a),sys.getsizeof(b))

def test1(input_str: str):
    splits = []
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         splits.append(input_str.split(char))
    return splits

def test2(input_str: str):
    splits = []
    append = splits.append
    split = input_str.split
    for char in (' ', ',', ';', ':', '.', '-', '_'):
         append(split(char))
    return splits

func_1(a,b)
func_2(a,b)
func_3(a)
func_4()

print(timeit.timeit(lambda: 'test1("123123,ewe,w.,w,ewe")',number=1))
print(timeit.timeit(lambda: 'test2("123123,ewe,w.,w,ewe")',number=1))


'''
#1
<class 'tuple'> <class 'list'>
112 136
#2
<class 'tuple'> <class 'list'>
184 200
#3
<class 'set'> <class 'frozenset'>
728 728
#4
<class '__main__.func_4.<locals>.Point'> <class '__main__.func_4.<locals>.Base'>
48 48
'''
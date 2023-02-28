Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> stu1={"Name": "Prince","Course":"Eng"}
>>> print(stu1["Name"])
Prince
>>> print(stu1["Course"])
Eng
>>> stu1["age"]=20
>>> len(stu1)
3
>>> stu1["Name"]="Prince Singh"
>>> print(stu1)
{'Name': 'Prince Singh', 'Course': 'Eng', 'age': 20}
>>> stu1.pop("age")
20
>>> print(stu1)
{'Name': 'Prince Singh', 'Course': 'Eng'}
>>> #set
>>> course=("a","b","c","d")
>>> print(course)
('a', 'b', 'c', 'd')
>>> 
KeyboardInterrupt
>>> course=("apple","boy","cat","dog")
>>>  print(course)
 
SyntaxError: unexpected indent
>>> print(course)
('apple', 'boy', 'cat', 'dog')
>>> course.add("mango")
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    course.add("mango")
AttributeError: 'tuple' object has no attribute 'add'
>>> course.add("Mango")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    course.add("Mango")
AttributeError: 'tuple' object has no attribute 'add'
>>> course1=("apple","boy","cat","dog")
>>> print(course1)
('apple', 'boy', 'cat', 'dog')
>>> course1.add("hoolo")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    course1.add("hoolo")
AttributeError: 'tuple' object has no attribute 'add'
>>> extra={"moomoo","xyz")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
>>> extra={"moomoo","xyz"}
>>> course1.update(extra)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    course1.update(extra)
AttributeError: 'tuple' object has no attribute 'update'
>>> 
>>> 

>>> 
>>> 
>>> 
>>> #frojen set
>>> 
>>> x=frozenset(("apple","boy","cat","dog"))
>>> x.add("xyz")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.add("xyz")
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
>>> #boolean
>>> a=True
>>> a
True
>>> a=10<20
>>> a
True
>>> s10>20
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s10>20
NameError: name 's10' is not defined
>>> s=10>20
>>> s
False
>>> type(s)
<class 'bool'>
>>> 
>>> #binary
>>> a=b"Hello"
>>> print(a)
b'Hello'
>>> 
>>> #byte arry
>>> ba=bytearray(5)
>>> ba
bytearray(b'\x00\x00\x00\x00\x00')
>>> x=memoryview(bytes(5)
	     x
	     
SyntaxError: invalid syntax
>>> x=memoryview(bytes(5))
>>> x
<memory at 0x040B48C8>
>>> 
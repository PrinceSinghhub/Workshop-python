Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> course={"Bio","Eng","Micro","Pharma"}
>>> course
{'Eng', 'Bio', 'Pharma', 'Micro'}
>>> course.add("b.tech")
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'Micro'}
>>> extra={"abc","xyz"}
>>> course.update(extra)
>>> course
{'Eng', 'b.tech', 'Pharma', 'abc', 'Bio', 'Micro', 'xyz'}
>>> course.remove("abc")
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'Micro', 'xyz'}
>>> course.discard("xyz")
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'Micro'}
>>> course.add("xyz")
>>> coures
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    coures
NameError: name 'coures' is not defined
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'Micro', 'xyz'}
>>> course.discard("apple")
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'Micro', 'xyz'}
>>> course.remove("micro")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    course.remove("micro")
KeyError: 'micro'
>>> course.remove("Micro")
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'xyz'}
>>> course.pop(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    course.pop(3)
TypeError: pop() takes no arguments (1 given)
>>> course.pop
<built-in method pop of set object at 0x03ADA808>
>>> course
{'Eng', 'b.tech', 'Pharma', 'Bio', 'xyz'}
>>> course.pop()
'Eng'
>>> course.pop(1)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    course.pop(1)
TypeError: pop() takes no arguments (1 given)
>>> course
{'b.tech', 'Pharma', 'Bio', 'xyz'}
>>> course.pop()
'b.tech'
>>> course
{'Pharma', 'Bio', 'xyz'}
>>> 
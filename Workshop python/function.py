Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================= RESTART: C:/Users/hp/OneDrive/Desktop/list.py ================
>>> print(len(cre))
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(len(cre))
NameError: name 'cre' is not defined
>>>  print(len(crs))
 
SyntaxError: unexpected indent
>>> print(len(crs))
3
>>> crs[0]
'eng'
>>> crs[1]
'mba'
>>> crs[2]
'hooo'
>>> crs[-1]
'hooo'
>>> crs[1:2]
['mba']
>>> crs[:1]
['eng']
>>> crs[:]
['eng', 'mba', 'hooo']
>>> stu1=["Prince",256354024,"Eng"]
>>> stu1
['Prince', 256354024, 'Eng']
>>> crs.insert(1,"programming")
>>> crs
['eng', 'programming', 'mba', 'hooo']
>>> crs.append("comm")
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm']
>>> crsl=["xyz","abc","bnc"]
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm']
>>> crs1
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    crs1
NameError: name 'crs1' is not defined
>>> crs1
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    crs1
NameError: name 'crs1' is not defined
>>> crs1=["xyz","abc",","uvw"]
      
SyntaxError: invalid syntax
>>> crs1=["xyz","abc","uvw"]
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm']
>>> crs1
['xyz', 'abc', 'uvw']
>>> crs.append(crs1)
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm', ['xyz', 'abc', 'uvw']]
>>> crs[6]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    crs[6]
IndexError: list index out of range
>>> crs[4]
'comm'
>>> crs[5]
['xyz', 'abc', 'uvw']
>>> crs.extends(crs1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    crs.extends(crs1)
AttributeError: 'list' object has no attribute 'extends'
>>> 
KeyboardInterrupt
>>> crs.extend(crs1)
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm', ['xyz', 'abc', 'uvw'], 'xyz', 'abc', 'uvw']
>>> crs.remove("xyz")
>>> crs
['eng', 'programming', 'mba', 'hooo', 'comm', ['xyz', 'abc', 'uvw'], 'abc', 'uvw']
>>> crs[2]="XYZ"
>>> crs
['eng', 'programming', 'XYZ', 'hooo', 'comm', ['xyz', 'abc', 'uvw'], 'abc', 'uvw']
>>> crs[0]=crs[3]="AAAA"
>>> crs
['AAAA', 'programming', 'XYZ', 'AAAA', 'comm', ['xyz', 'abc', 'uvw'], 'abc', 'uvw']
>>> tup=("amit","hudfh","diufyh","dsufhiudfhu")
>>> tup
('amit', 'hudfh', 'diufyh', 'dsufhiudfhu')
>>> tup[3]
'dsufhiudfhu'
>>> len(tup)
4
>>> tup.insert(1,"kjdhfiuh")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tup.insert(1,"kjdhfiuh")
AttributeError: 'tuple' object has no attribute 'insert'
>>> 
>>> 
>>> 
>>> print(range(0,6))
range(0, 6)
>>> 
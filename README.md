# 你不该用它 YouShallNotUseIt
    允许使用者简单的锁定、解锁或是永久禁用Python中的内置函数/内置类
    easily lock &amp; unlock BIF in python.  
## 它如何工作？ How It works
    内置类/函数通常存在于__builtins__模块，这是每个脚本运行时虚拟机自动导入的模块。当修改了该模块的内容，运用内置类/函数便会受到影响。
    Builtin types or functions exist in module named '__builtins__', which imported automatically by python vm when running a script.
    BIF/T may be edited as we change __builtins__'s content.
## 如何使用 Quick start
```python
>>> from youshallnotuseit import *

>>> print('hello world')
hello world
>>> lock(print)
>>> print('hello world')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Projects\PythonProject\youshallnotuseit\covers\Functions.py", line 7, in LockedFunction
    raise YouShallNotUseIt(lang.func.locked)
youshallnotuseit.covers.Exceptions.YouShallNotUseIt: This Function is Locked

>>> help(print)
Help on function LockedFunction in module youshallnotuseit.covers.Functions:

LockedFunction(*args, **kwargs) -> NoReturn
    This Function is Locked


>>> unlock('print')
>>> print('hello world')
hello world
```
支持自定义报错信息和文档
allow user to modify error info & doc

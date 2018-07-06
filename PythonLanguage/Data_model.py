# Data model 数据模型  语义层定义的对象在内存中的数据模型(对比java)
# Objects, values and types
# 对象是Python对数据的抽象。 Python程序中的所有数据都由对象或对象之间的关系来表示
# 每个对象都有一个标识，一个类型和一个值。 对象的身份一旦创建就不会改变;
# 你可能会认为它是内存中的对象地址。 'is'运算符比较两个对象的身份（是不是同一个对象）; id（）函数返回一个表示其身份的整数。
# For CPython, id(x) is the memory address where x is stored
# The type() function returns an object’s type . Like its identity, an object’s type is also unchangeable

def  x():
     x = 1

# <class 'function'>
print(type(x))


# <class 'object'>
print(type(object()))

# 对象值的可变性问题
#  for instance, numbers, strings and tuples are immutable, while dictionaries and lists are mutable.
#  对象的引用，数字，字符串，元组不可以变，map list 可变
# 对象的生命周期  垃圾收集器进行收集
#  CPython 使用 reference-counting （引用计数算法计算对象是否可达）
#  考虑 cyclic garbage（循环引用的问题）
#  详细的 gc 信息 https://docs.python.org/3.6/library/gc.html#module-gc
#  请注意，使用实现的跟踪或调试工具可能会使对象保持活动状态，这通常是可收集的。
#  还要注意，使用'try ... except'语句捕获异常可能会使对象保持活动状态
#  有些对象包含的资源的引用 如打开的文件或 窗口，gc不能保证收集，要显示的调用方法释放资源
#  如 close()方法  推荐使用语法 ‘try…finally’ or with
#  对象引用其他的，容器，Examples of containers are tuples（元组）, lists and dictionaries
#  类型几乎影响对象行为的所有方面。 即使对象身份的重要性也在某种意义上受到影响：对于不可变类型，
# 计算新值的操作实际上可能会返回对具有相同类型和值的任何现有对象的引用，而对于可变对象则不允许。 例如，在a = 1之后; b = 1，a和b可能或不可能引用具有值1的同一对象，具体取决于实现，
# 但在c = []之后; d = []，c和d保证引用两个不同的唯一的新创建的空列表。 （请注意，c = d = []将同一个对象分配给c和d）。

# python 内置的对象

# None
# NotImplemented
# Ellipsis  或 ...

# 数字类的体系结构 定义在文件  Lib/numbers.py
# numbers.Number  抽象的父类
# numbers.Integral  包含 Integers (int)，Booleans (bool)  整数
# numbers.Real (float)                                    实数
# numbers.Complex (complex)                               虚数

# 字符串
# 内置方法 built-in function len()  索引 0-n-1
s = '99490343'
print(s[0])
print(s.__len__())
# 字符串支持切片 a[i:j]表达意思(i <= k < j)  a[i:j:k]  表达意思 x = i + n*k, n >= 0 and i <= x < j
print(s[0:5])
# 不可变字符串
#  strings
#  Tuples 元组 ()
#  Bytes

# 可变的字符串
#  Lists
#  Byte Arrays

#  集合类型 Set types
#  可变  built-in set() constructor and can be modified afterwards by several methods, such as add()
#  不可变 Frozen sets created by the built-in frozenset()

#  Mappings
#  Dictionaries  字典

# Callable types
# 1.User-defined functions
"""
A user-defined function object is created by a function definition
方法的定义创建一个 function object

方法对象 有很多属性
如:
__name__
具体查看 https://docs.python.org/3.6/reference/datamodel.html
"""
def func():
     x = 1

print(func.__code__)


# 2 Instance methods  实例方法
"""
 An instance method object combines a class, 组成对象的方法
 Special read-only attributes: 
         1）__self__ is the class instance object,
         2）__func__ is the function object
         3）__doc__ is the method’s documentation
         4） __name__ is the method name (same as __func__.__name__)
         5） __module__ is the name of the module the method was defined in, or None if unavailable.
 实例方法： __self__ 参数列表 和java 的实现类似 this
    类方法：
 
"""
# 3 Generator functions  A function or method which uses the  yield statement
"""
 Generator functions 详细查看 Expressions.py
"""
# 4 Coroutine functions 协程方法 async def
# 5 Asynchronous generator functions 上面两个组合
# 6 Built-in functions  A built-in function object is a wrapper around a C function
# 7 Built-in methods
"""
# 他实际上是一个内置函数的伪装(对Built-in functions 的封装)，
# 这次包含一个传递给C函数的对象作为一个隐含的额外参数。
#  假设alist是一个列表对象，内置方法的一个例子是alist.append（）。
# 在这种情况下，将特殊只读属性__self__设置为由alist表示的对象。
"""


# 8 Classes  __new__() __init__()
"""
 创建对象 构造方法
  __new__ ：创建对象是调用，如果没有返回 cls对象不会调用__init__方法
                           返回了 cls 对象 则调用 __init__方法，第一个参数就是实例化的对象
  
  初始化函数
  __init__：没有返回值
  
"""
class sud :
      def __new__(cls, *args, **kwargs):
           print("new")
           return object.__new__(cls) #有返回值调用 __init__方法

      def __init__(self):
           print("init")

sud()


# 9 Class Instances Class 的实例类似java的  __call__()
"""
通过在类中定义__call __（）方法，可以使任意类的实例可调用。
"""
# class 对象 反射
object().__class__
#  10 Modules  模块
"""
Modules are a basic organizational unit of Python code
模块是组织python代码的基础单元并通过import 系统各个模块可以相互调用
import 系统包括
指令： import statement 
方法调用: importlib.import_module() and built-in __import__()

A module object has a namespace implemented by a dictionary object 
(this is the dictionary referenced by the __globals__ attribute of functions defined in the module)
模块对象含有一个命名空间，它的实现是通过dict对象
m.__dict__ 

模块对象的属性
__name__
__doc__ 
__file__ 等
"""

m = __import__("clz")
print(m.__name__ )
print(m.__dict__ )
# A module object has a namespace implemented by a dictionary object
# (this is the dictionary referenced by the __globals__ attribute of functions defined in the module)

# 11 Custom classes 自定的Class
"""
A class has a namespace implemented by a dictionary object
C.__dict__
查找过程: When the attribute name is not found there, the attribute search continues in the base classes
python 的集成是多继承的 和java不同

__self__属性 
在不同的方法下回自动换行，分实例方法和静态方法

特殊属性: Special attributes
 __name__ is the class name; 
 __module__ is the module name in which the class was defined; 
 __dict__ is the dictionary containing the class’s namespace; 
 __bases__ is a tuple containing the base classes, in the order of their occurrence in the base class list; 
 __doc__ is the class’s documentation string, or None if undefined

"""

# 12 Class instances
"""
A class instance is created by calling a class object  class对象 
可以查看  9 Class Instances Class
 If the class has a __setattr__() or __delattr__() method, 
 this is called instead of updating the instance dictionary directly.
 Special attributes: __dict__ is the attribute dictionary; __class__ is the instance’s class
"""

# 13 I/O objects
"""
A file object represents an open file. Various shortcuts are available to create file objects: 
the open() built-in function,
 and also os.popen(), os.fdopen(), and the makefile() method of socket objects
 
 标准输入输出：
 sys.stdin, sys.stdout and sys.stderr
"""

# 14 Internal types  interpreter 解释器内部的类型

# 1）Code objects
"""
Code objects represent byte-compiled executable Python code, or bytecode.

"""
# 2) Frame objects 栈帧

# 3） Traceback objects 异常
"""
Traceback objects represent a stack trace of an exception. A traceback object is created when an exception occurs
"""
# 4) Slice objects
"""
Slice objects are used to represent slices for __getitem__() methods.
 They are also created by the built-in slice() function
 Special read-only attributes: start is the lower bound; stop is the upper bound; 
 step is the step value; each is None if omitted. These attributes can have any type
 开始，结束，步长
 slice.indices(self, length)
"""
# 5）Static method objects
"""
Static method objects are created by the built-in staticmethod() constructor
"""

# 6) Class method objects
"""
Class method objects are created by the built-in classmethod() constructor

"""
# 15 Special method names

# 1）object.__new__(cls[, ...])
"""
Called to create a new instance of class cls. __new__() is a static method
 superclass’s __new__() method using super().__new__(cls[, ...])
 If __new__() returns an instance of cls（返回了对象实例）, then the new instance’s __init__() method will be invoked
 If __new__() does not return an instance of cls, then the new instance’s __init__() method will not be invoked.

"""











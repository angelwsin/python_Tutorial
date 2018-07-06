#  python 表达式
#  语法提示： extended BNF notation will be used to describe syntax

# 1 # Arithmetic conversions 算数转换 隐式转换 （类比java）

# If either argument is a complex number, the other is converted to complex;
# otherwise, if either argument is a floating point number, the other is converted to floating point;
# otherwise, both must be integers and no conversion is necessary.


# 2  Atoms
# 原子是表达的最基本的元素。 最简单的原子是标识符或文字。 括号或大括号中的形式也可以在语法上归类为原子

#  Identifiers 标识符

#  Literals  字面量
#  Python supports string and bytes literals and various numeric literals:

#  Parenthesized forms  括号
# 一个带括号的表达式列表产生表达式列表产生的任何结果：
# 如果列表至少包含一个逗号，则产生一个元组; 否则，它会生成组成表达式列表的单个表达式
# 一对空括号产生一个空的元组对象。 由于元组是不可变的，因此适用文字规则
# （即，空元组中的两次出现可能会或可能不会产生相同的对象）。
# 请注意，元组不是由括号组成，而是由逗号运算符组成。
#  例外是需要括号的空元组 - 允许表达式中没有“没有”会导致含糊不清，并允许常见的拼写错误未被捕获。
#

# Displays for lists, sets and dictionaries  list,set dict 的定义 并且他们都是可变的对象
"""
为了构造一个列表，一个集合或一个字典Python提供了一种称为“显示”的特殊语法，每种语法都有两种形式：
1)容器内容被明确列出，或者 直接写出如 list [0,1,2,3,4,5,6,7,8,9]
2)它们通过一组循环和过滤指令来计算，称为理解
"""
# 显示列出容器中的内容
# 通过循环loop和过滤指令

# 1）List displays
"""
list_display ::=  "[" [starred_list | comprehension] "]"
"""
str = [0,1,2,3,4,5,6,7,8,9]
list1 = [i for i in range(10)]
list1 = [(i) for (i) in ((9),(0))]
print(list1)

# Set displays 集合 类似java的Set
"""
set_display ::=  "{" (starred_list | comprehension) "}"
"""
set1 = {2,8,4,5,5,6}
set2 = {i for i in range(10)}
print(set2)
# 注意：An empty set cannot be constructed with {}; this literal constructs an empty dictionary.
# Dictionary displays 类似java map  key value

map = {"key":9,8:0}
print(map)
"""
 类似java 中的 hash
hashable
 (it needs a __hash__() method), and can be compared to other objects (it needs an __eq__() method)
 makes an object usable as a dictionary key and a set member
"""

# Generator expressions
#
# a)Yield expressions
# 当调用生成器函数时，它会返回一个称为生成器的迭代器。该生成器然后控制生成器函数的执行。
# 当一个生成器的方法被调用时执行开始。那时，执行进行到第一个yield表达式，在那里它再次被挂起，
# 将expression_list的值返回到生成器的调用者。通过暂停，我们的意思是保留所有本地状态，包括局部变量的当前绑定，
# 指令指针，内部评估堆栈以及任何异常处理的状态。当通过调用其中一个生成器的方法来恢复执行时，
# 该函数可以像yield yield表达式只是另一个外部调用一样进行。恢复后的yield表达式的值取决于恢复执行的方法。
# 如果使用__next __（）（通常通过for或next（）内建函数），则结果为None。否则，如果使用send（），那么结果将是传递给该方法的值。

def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    try:
        while True:
            try:
                value = (yield value)
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

# 调用Yield 的方法生成迭代器
generator = echo(1)
#  generator.__next__() 通过内建的方法 typically via either a for or the next() builtin 调用迭代器方法
print(next(generator))
#  result is None
print(next(generator))

# if send() is used, then the result will be the value passed in to that method
print(generator.send(2))

# generator.close()
generator.close()

# 斐波拉契数列
#  1 1 2 3 5

def su(i):
    f1 = 1
    f2 = 1
    for k in range(i):
        f3 = f1+f2
        f1 = f2
        f2 = f3
        yield f3

print(su(2))

for f in su(2):
    print(f)


def sux(i):
        yield from su(i)
print(sux(5))
for f in sux(5):
    print(f)

"""
generator functions与协同程序非常相似。 他们产生多次，他们有不止一个入口点，
他们的执行可以被暂停。 唯一的区别是生成器函数无法控制执行结束后应继续执行的地方; 该控件总是被传送给发生器的调用者。

yield表达式在try结构中的任何位置都是允许的。 如果在生成器未完成之前（通过达到零引用计数或通过垃圾收集），
生成器迭代器的close（）方法将被调用，从而允许执行任何挂起的finally子句

When yield from <expr> is used, it treats the supplied expression as a subiterator. 
All values produced by that subiterator are passed directly to the caller of the current generator’s methods

具体 https://docs.python.org/3.6/reference/expressions.html#generator-iterator-methods
"""

# b) Asynchronous generator functions
async def suxa(i):
          yield su(i)
print(suxa(5))


#  Comparisons 比较
#  类似C 的 运算符具有优先级的顺序
#  Comparisons yield boolean values: True or False.
# 1 Value comparisons
#  The operators <, >, ==, >=, <=, and != compare the values of two objects.
#  The objects do not need to have the same type.
#  Because all types are (direct or indirect) subtypes of object, 所有对象都是object的子类 可以通过
#  复写 方法完成比较  查看 object中的方法 https://docs.python.org/3.6/reference/datamodel.html#customization
#  object 默认只实现 == and !=  是根据地址判断是不是同一个对象 （类比java的equels方法）
#  默认相等比较的行为，具有不同身份的实例总是不相等的，可能与需要具有对象值和基于值的相等的明确定义的类型形成对比。
#  这些类型需要定制它们的比较行为，实际上，一些内置类型已经完成了这些
#  内置对象实现比较方法
# 1） 内置数字类型（数字类型 - int，float，complex）和
# 标准库类型fraction.Fraction和decimal.Decimal的数量可以在它们的类型内和跨越它们的类型进行比较，
# 限制条件是复数不支持顺序比较。 在涉及的类型范围内，它们在数学上（算法上）比较正确，而不会损失精度
# a)非数字 The not-a-number values float('NaN') and Decimal('NaN') are special
# (x is x is true) but are not equal to themselves (x == x is false).
# comparing any number to a not-a-number value will return False
# b)二进制 二进制序列（instances of bytes or bytearray）可以在它们的类型之内和之间进行比较。 他们使用元素的数字值按字母顺序进行比较
# c)字符串（str的实例）按字典顺序使用字符的数字Unicode代码点（内置函数ord（）的结果）进行比较
# Strings and binary sequences cannot be directly compared
# d)序列（instances of tuple, list, or range）只能在每种类型中进行比较，限制range不支持顺序比较。
# 这些类型之间的平等比较会导致不平等，并且跨这些类型的排序比较会引发TypeError
# e)Mappings (instances of dict) compare equal if and only if they have equal (key, value) pairs
# f) Sets (instances of set or frozenset) can be compared within and across their types
# g) Most other built-in types have no comparison methods implemented, so they inherit the default comparison behavior.
#  自反性，对称性，传递性
# 其他的 查看 https://docs.python.org/3.6/reference/expressions.html#value-comparisons

# 2 Membership test operations 成员
# a) x in s evaluates to True if x is a member of s
class S :
    x = 9;

s = S();

# b) All built-in sequences and set types support this as well as dictionary,
# for which in tests whether the dictionary has a given key. For container types such as list,
#  tuple, set, frozenset, dict, or collections
a = [9,8,7]
print(9 in a)
map = {"k":"9"}
print("k" in map)
# c)For the string and bytes types, x in y is True if and only if x is a substring of y.
#  An equivalent test is y.find(x) != -1
str = "89489343"
print("89" in str)
# d) For user-defined classes which define the __contains__() method
#   For user-defined classes which do not define __contains__() but do define __iter__()
#  Lastly, the old-style iteration protocol is tried: if a class defines __getitem__(), x in y is True
# The operators in and not in test for membership

# 3. Identity comparisons 同一对象（地址一致）
# The operators is and is not test for object identity: x is y is true if and only if x and y are the same object.
# Object identity is determined using the id() function. x is not y yields the inverse truth value
x = 8;
y = x;
print(x is y)

# 4 Boolean operations
"""
 a)False:False,None,numeric zero of all types,and empty strings 
 and containers (including strings, tuples, lists, dictionaries, sets and frozensets)
 b)True:除了上面的False
 与 and  或 or   非 not 
 c) User-defined objects can customize their truth value by providing a __bool__() method
"""
# 5 Conditional expressions 条件表达式
# conditional_expression ::=  or_test ["if" or_test "else" expression]

# 6 Lambdas 表达式
"""
Lambda expressions (sometimes called lambda forms) are used to create anonymous functions.
 The expression lambda parameters: expression yields a function object
 lambda_expr        ::=  "lambda" [parameter_list]: expression
"""
f = lambda x,y: x+y

print(f(8,9))

# 7 Expression lists
# expression_list    ::=  expression ( "," expression )* [","]

#  Evaluation order 运算顺序
"""
Python evaluates expressions from left to right. Notice that while evaluating an assignment, 
the right-hand side is evaluated before the left-hand side.

https://docs.python.org/3.6/reference/expressions.html#operator-precedence
"""

# Python float is an IEEE 754 double-precision number
















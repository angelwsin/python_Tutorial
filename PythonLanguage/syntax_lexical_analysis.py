# python 的语法规范和词法规范 https://docs.python.org/3.6/tutorial/index.html
# python 的实现
# CPython 普遍使用的实现(类似java中jvm的实现有HotSpot)
# Jython
# ....
# BNF grammar notation  python 使用 BNF范式描述词法和语法
# Notation 符号
# name      ::=  lc_letter (lc_letter | "_")*
# lc_letter ::=  "a"..."z"

_x = "xxx"
a = 4
# Lexical analysis  词法

# Line structure 行结构含有多个多个逻辑行
# Logical lines  逻辑行的多个物理行使用 \
# Physical lines 回车换行
# Comments  注释 使用 # 开头的物理行
# 多行注释用三个单引号 ''' 或者三个双引号 """ 将注释括起来

# Encoding declarations 编码声明
# 如果Python脚本的第一行或第二行中的注释匹配正则表达式编码[=：]\s*（[-\w.]+），则该注释将作为编码声明处理;
# 该表达式的第一组命名为源代码文件的编码。 编码声明必须出现在它自己的一行上。 如果是第二行，则第一行也必须是仅限注释行。
#  编码表达式的推荐形式是
# 例如 # -*- coding: <encoding-name> -*-


# 逻辑行的
# 显式行加入
# if 1900 < year < 2100 and 1 <= month <= 12 \
#         and 1 <= day <= 31 and 0 <= hour < 24 \
#         and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
# return 1
# 隐式行加入
# month_names = ['Januari', 'Februari', 'Maart',      # These are the
#                'April',   'Mei',      'Juni',       # Dutch names
#                'Juli',    'Augustus', 'September',  # for the months
#                'Oktober', 'November', 'December']   # of the year

# 空白行
# 仅包含空格，制表符，换页符和可能的注释的逻辑行将被忽略（即，不会生成NEWLINE标记）。
# 在交互式输入语句期间，根据read-eval-print循环的实现情况，处理空白行可能会有所不同。 在标准的交互式解释器中，一个完全空白的逻辑行（即不包含空格或注释的逻辑行）终止多行语句。

# Indentation  缩进
# 使用spaces and tabs 缩进来组织代码块

# Identifiers and keywords 标识符和关键字
# Identifiers 字母数字下划线，开头 字母下划线

# Keywords
# False      class      finally    is         return
# None       continue   for        lambda     try
# True       def        from       nonlocal   while
# and        del        global     not        with
# as         elif       if         or         yield
# assert     else       import     pass
# break      except     in         raise

# Reserved classes of identifiers 预留的标识符类
# 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，
# 需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
# 以双下划线开头的 __foo 代表类的私有成员；
# 以双下划线开头和结尾的 __foo__
# 代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数。

# Literals 字面量

# String
# 单引号 双引号 三引号
# stringprefix     r/R(屏蔽转义)b/B（二进制标示ASCII）  u/U（unicode）  f/F（参考Formatted string）
# 转义字符
x = r"895303333333\n\n"
# String literal concatenation 字符拼接  '"这种编译时，+ 运行时
b = 'dsds''hdsss'"9049343"'''9090'''+"jdlsj"
print(b)

# Formatted string literals


# Numeric literals ： Integer literals ，Floating point literals ， Imaginary literals（虚数）


# Operators  操作符
# +       -       *       **      /       //      %      @
# <<      >>      &       |       ^       ~
# <       >       <=      >=      ==      !=


# Delimiters 分隔符
# (       )       [       ]       {       }
# ,       :       .       ;       @       =       ->
# +=      -=      *=      /=      //=     %=      @=
# &=      |=      ^=      >>=     <<=     **=



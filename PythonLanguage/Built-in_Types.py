# 内置类型

# boolean false
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)

# Boolean Operations — and, or, not

# Comparisons
print("xxx">0)
# 两个对象类型不一样 不可以比较 异常TypeError
# 对象之间可以重新 __eq__()方法比较

class  stud:

       x = 1

       def __eq__(self,other):
          return self.x == other.x
       

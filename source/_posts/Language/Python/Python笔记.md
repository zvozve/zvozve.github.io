---
title: Python笔记
auther: zvozve
comments: false
categories:
  - Language
  - Python
tags: Python
date: 2022-03-19 16:16:21
---

[教程链接](https://www.bilibili.com/video/BV1u741157TW?p=1)
## 1

### 1.1单引号和双引号一样的

```python
print('hello world')
Print("hello world")
```

### 1.2三个单引号起换行效果

```python
Print('''hello world
hello world
hello world
''')

# output
# hello world
# hello world
# hello world
```

### 1.3 注释

```python
# 注释
# Pycharm注释快捷键  ctrl+/
```

## 2

### 2.1变量

```python
a = b = 2
print(a)
print(b)
 
a=2,b=2
print( "a="+str(a))#str强制类型转换
print( "b="+str(b))
greeting="hello"
print(greeting)
greeting="world"
print(greeting)
```

### 2.2变量的命名规则

```python
# 可以用数字字母下划线，不能以数字开头
# 关键字不能作为变量名字
```

### 2.3数字类型int float

```python
'''
在Python中，有两种主要的数字类型：
整数和浮点数。
它们之间最重要的区别是浮点数是具有小数点的数字，而int是没有小数点的数字。
'''
number = 9
print(type(number))# print type of variable "number"
float_number = 9.0
print(type(float_number))
print( number+1)
print(float_number+1)
```

### 2.4数据类型转换int float str

```python
# 有几个内置函数可让您将一种数据类型转换为另一种数据类型。
# 这些函数返回一个表示转换后值的新对象
# “ int（x）”将x转换为整数。
# “ float（x）”将x转换为浮点数。
# “ str（x）”将对象x转换为字符串表示形式。
number =9
print(type(number))# print type of variable "number"
 
float_number = 9.0
print(float_number)
print(int(float_number))

#通过int(),float() , str()进行的转换成为显示类型转换
age = "10"
print(int(age)+1)
 
street_no = 101address ="北京西城"
print(address+str(street_no))
 
#隐式类型转换
float _number = 9.0print(float_number+1)
```

### 2.5算式运算符 + - * / ** %

```python
number = 9.0 #float number
#result =divide ' number' by two#
#remainder = calculate the remainder#
#print( " result =" + str(result))
#print( " remainder = " + str( remainder))
 
result = number/2
remainder = number % 2
print( "result =" + str( result))
print( " remainder =" + str(remainder))
 
num =9
print(num/2)
print(num %2)
print(num**3)
```

### 2.6赋值运算符+=  -=  *=  /=

```python
number = 9.0
print("number = " + str(number))
 
number -= 2
number = number - 2
print(number)
print( "number = " + str(number))
 
number operator 5
number += 5
print( "number = " + str(number))
 
Number *= 2
print(number)
```

### 2.7布尔运算符boolean True False == !=

```python
two = 2
three = 3
is_equal = two == three
print( is_equal)
is_equal = two != three
print( is_equal)
```

### 2.8比较运算符>=  <=  >  < 

```python
# 返回值boolean值只有True False
# 返回结果只有True Fasle
# 比较运算符具有同样的优先级并且可以组成任意链> >   < <
 
one = 1
two = 2
three = 3
print(one < two < three)
is_greater = three > two
print(is_greater)
flag = two >= three
print(flag)
```

## 3

### 3.1字符串连接

```python
hello = "Hello"
world = 'World'
hello_world = hello+world
print(hello_world) #Note: you should print "Hello World"
number = 9
print(hello+str(number))
hello_world = hello+" "+world
print(hello_world)
```

### 3.2字符串乘法运算

```python
hello = "hello"
ten_of_hellos = hello *10
print(ten_of_hellos)
#output:
#hellohellohellohellohellohellohellohellohellohello

star
empty = " "
print(empty*3+star)
print(empty*2+star*3)
print(empty+star*5)
#output:
#   *
#  ***
# *****
```

### 3.3 字符串索引

```python
python= "Python"
print("h" + python[3])
p_letter = python[0]
print (p_letter)
#output:
#h h
#p

print(python [51])
#python中字符串索引可以是正数,也可以是负数
print(python [-1])
#output:
#N
#N

print(python [51])
# python中字符串索引可以是正数，如果索引是正数那么索引值从0开始，从前往后数
#也可以是负数，如果索引值是负数,索引值从-1开始,从后往前数
print(python [-6])
#output:
#N
#p

#如何能够获得字符串中字符的索引值呢
print(python.index('h'))
#output:
#3

print(python.index('a'))
#报错
```

### 3.4字符串截取#默认从0开始，可以不写

```python
monty_python = "Monty Python"
monty = monty_python [:5]
print(monty)
#output:
# Monty

# #默认到结尾，可以不写
python = monty_python [6:]
print(python)
#output:
# Python
# #索引可以为负数

```

### 3.5字符串in操作符

```python
ice_cream = "ice cream"
print("cream" in ice_cream)
#output:
# Ture
contains = "ice" in ice_cream
print(contains)
#output:
# ture
contains = "ic e" in ice_cream
print(contains)
#output:
# False
contains = "ic e" not in ice_cream
print(contains)
#output:
# Ture
```

### 3.6 len方法（统计字符串中的字符数）注意类型转换

```python
#短语=这是一个非常长的字符串，用三引号引起来的字符串定义多行字符串
phrase = '''
It is a really long string
triple-quoted strings are used 
to define multi-line strings
'''
#取出上半部分  全部  全部/2  [0:全部/2]
first_half = phrase[0:int(len(phrase)/2)]
print(first_half)
#output:
#It is a really long string
#triple-quoted st
print( len(phrase))
#output:
# 88
```

### 3.7转义字符

\\" \t \n

```html
<html> 
Backslash is used to escape single or double quotation marks, for example 'It\'s me' or "She said \"Hello\"".
The special symbol '\n' is used to add a line break to a string. 
<br><br/>
Print out the following text using one string:<br/>
The name of this ice-cream is "Sweeet'n'Tasty" 
<br/>
</html>
```

```python
print("My name is \"Daniell"")
print("hello world!\t\t\tI am coming") 
print("hello world!AnI am coming")
```

3.8 string内置函数

```html
<html> 
There are a lot of useful string methods.
You can use the 'lower()' method to get rid of any capitalization in your strings.
The 'upper()' method is used to make a string uppercase. To call any string method, type a dot after the string (or a variable containing the string)
and the method name after it, e.g. "John".upper().
In PyCharm, you can explore all available string methods by using Ctrl+Space after a dot.
<br><br/>
Print monty_python in upper case. 
</html>
```

```python
monty_pytnon = "Monty Python"
print(monty_python)
# lower函数将字符串字符转换成小写
print (monty_python. lower())
# upper函数将字符串中字符转换成大写
print (monty_python.upper())
# print (upper cased monty_python) 
#output:
# Monty Python
# monty python 
# MONTY PYTHON
```

```python
# find函数 查找某个字符在字符串中的索引，如果没有返回—1
print(monty_python. find('M'))
print(monty_python. find( 'm'))
# find函数在查找过程中返回的是查找字符串中第一个字符出现的索引
print(monty_python. find('o'))
# output:
# 0
# -1
# 1
```

```python
# count函数，计算字符串中一个字符出现的次数
print(monty_python. count('n'))
#output: 2

# rfind 查找字符串中字符出现的最后一次位置索引
print(monty_python. count('n'))
#output: 11

# replace 替换
#将o换成a
print(monty_python. replace('o', 'a')) 

# split 字符串的分割
print(monty_python.split(" ")) 
['Monty', 'Python']

goods = "apple, orange" 
print(goods.split(",")) 
['apple', 'orange']
```

### 3.9字符串格式化

```python
“%s” %变量名
%d
%f %.1f
format
```

```python
name = "Daniel"
print("Hello, PyCharm! My name is %s!" % name) 
#output: Hello, PyCharm! My name is Daniel!
```

```python
years = 28
print("I'm special symbol years old %d" % years) 
price = 2.4
print（“这个商品的价格为%.2f元” % price）
# output: 
# I'm special symbol years old 28 
# 这个商品的价格为2.40元
```

```python
print("[0) is [1) years old". format ("Daniel", 28)) 
print("[name) is fage) years old". format(name="Daniel", age=28))
# output: 
# Daniel is 28 years old
```

```python
# 二进制，十进制，八进制，十六进制
print("[:b)". format (11)) 
print("[:d]".format (11))
print("[:o)".format (11)) 
print("[:x)".format (11)) 
# output: 
# 1011
# 11 
# 13
# b
```

## 4

### 4.1 list

```html
<html> 
A list is a data structure you can use to
store a collection of different pieces of information under a single variable name.
A list can be written as an array of comma-separated values (items) between square brackets, e.g. lst = [iteml, item2].
Lists might contain items of different types,
but usually all the items in the list ar of the same type. Like strings, lists can be indexed and sticed (see Lesson 3). 
<br><br/>
Use list slicing to print [4, 9, 16]. 
</html>
```

```python
squares = [1, 4, 9, 16, 25] 
print(squares)
#列表索引
print(squares [0]) 
print(squares [-2]) 
print (squares [:3]) 
# output: 
# [1, 4, 9, 16, 25]
# 1
# 16
# [1, 4, 9]
```

### 4.2 list 操作 1

列表项的追加 += append（）
修改列表项值 list[index] = new item

```html
<html>
You can add new items at the end of the list, by using the append () method and concatenation.
Unlike strings, lists are a mutable type, i.e.
it is possible to change their content using lst [index]= new_item 
<br><br/>
Replace 'dino' with "dinosaur" in the "animals" list. 
<br/>
</html>
```

```python
animals = ['elephant', 'lion', 'tiger', "giraffe"] # create new list 
print (animals)

animals += ["monkey", 'dog'] # add two items to the list 
print (animals)

animals.append ("dino") # add one more item to the list using append() method 
print(animals)

# replace 'dino' with 'dinosaur' 
# print (animals)

print (animals. index("dino"))
animals [animals. index("dino")] = "dinosaur" 

print (animals)

# output: 
# ['elephant', 'lion', 'tiger', 'giraffe']
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog']
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog', 'dino'] 
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog', 'dinksaur'] 
```

### 4.3 list 操作2

通过切片可以完成列表项的修改

clear可以清空列表

sort进行排序， reverse反转排序

insert方法可以按索引插入列表项

pop方法按索引删除列表项

remove方法按照列表值进行删除

```python
print(animals)

animals [1:3] = ['cat'] # replace 2 items - 'lion' and 'tiger' with one iter 
print(animals)

animals [1:3] = [] # remove 2 items - 'cat' and 'giraffe' from the list 
print(animals)

# clear list 
# print(animals) 
animals.clear() 
print (animals)

# output: 
# ['elephant', 'lion', 'tiger', 'giraffe', 'monkey', 'dog'] 
# ['elephant', 'cat', 'giraffe', 'monkey', 'dog']
# ['elephant', 'monkey', 'dog']
# []
```

```python
# sort()
nums = [1, 3, 5, 9, 6, 10] 
nums sort（）
print(nums) 
# output: 
# [1, 3, 5, 6, 9, 10] 
```

```python
nums. reverse() 
print (nums) 
# output: 
# [10, 9, 6, 5, 3, 1]
```

```python
# insert()
nums insert(3, 7) 
print (nums)
# output: 
# [10, 9, 6, 7, 5, 3, 1]
```

```python
# pop（）参数是索引值
nums. pop (3)
print(nums)
# remove（）参数是列表项
nums, remove (10)
print (nums)
#pop 弹出对应位置的内容
#pop一般从最后一个开始弹出
# output: 
# [10, 9, 6, 5, 3, 1] [9, 6, 5, 3, 1]
```

### 4.4 元组Tuple

元组和列表很像，但是不能添加，删除，改变其中的值
tuple = (1.)

```python
alphabet = ('a', 'b', ... ,'y','z')
# print(alphabet length) 
print(len(alphabet)) 

nums = (1, 2, 8, 7) 
print (nums)

nums = (1,x) 
print(nums)

# output: 
# 26
# (1, 2, 8, 7) 
# (1,)
```

### 4.5 字典1

```python
字典声明 dict = ["key1":"item","key2":"item") 
dict["key3"]="item3"
del dict["key1"]
```

```python
# create new dictionary.
phone_book = ["John": 123, "Jane": 234, "Jerrard": 345] 
print(phone_book)

# Add new item to the dictionary 
phone_book ["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book del phone_book 
del phone_book ['John']
print(phone_book) 

# print (Jane's phone)
phone_book ["Rose"] = 789 
print(phone_book)

del phone_book ["Rose"] 
print(phone_book)

# output: 
# {'Jonn: 123, 'Jerrara': 345, Jane: 234}
# {'Jill': 345, 'John': 123, 'Jerrard': 345, 'Jane': 234}
# {'Jill': 345, 'Jerrard': 345, 'Jane': 234}
# {'Rose': 789, 'Jill': 345, 'Jerrard': 345, 'Jane': 234} 
# {'Jill': 345, 'Jerrard': 345, 'Jane': 234}
```

### 4.6 字典2

字典中的内置函数keys，values，items，copy，get

```python
grocery_list = ["fish", "tomato", 'apples'] # create new list
print("tomato" in grocery_list) # check that grocery_list contains "tomato" item 
grocery_dict = ["fish": 1, "tomato": 6, 'apples': 3] # create new dictionary 
print('fish' in grocery_dict. keys ())
print('Apple' not in grocery_dict.keys()) 
print(6 in grocery_dict.values ())
```

### 4.7 字典3

```python
# print (phone_book. keys ())
print (phone_book. keys()) 
print(phone_book.values ()) 
# print(phone_book values)

# phone_book.clear(); 
# print(phone_book)

# phone = phone_book.copy() 
# phone = phone_book.copy() 
# print (phone)

# print (phone_book.get("zhangsan", "demo")) 
print(phone_book.get("rose", 789))
print(phone_book. items ())
```

## 5

### 5.1逻辑运算符1

| and  | x and y | 布尔“与“ | 如果x为False， x and y 返回 False，必须同时为True返回True |
| ---- | ------- | -------- | --------------------------------------------------------- |
| or   | x or y  | 布尔“或“ | 只有一方为True返回True.                                   |
| not  | not x   | 布尔“非“ | 如果x为True，返回False。如果x为False，它返回True.         |

```python
name = "John" 
age = 17

print(name == "Rose" or age = 23) 
print (name = "John" and age == 23)
# print(John is not 23 years old)

print(not (name == "John" and age != 23)) 
print(name == "John" and age != 23)
# output: 
# False 
# False 
# False 
# True
```

### 5.2逻辑运算符顺序

逻辑运算符顺序
逻辑运算符的顺序不是从左到右，顺序是先not再and最后or

```python
name = "John" 
age = 17

print(name == "John" or not age > 17)

# print("name" is "Ellis" or not ("name" equal "John" and he is 17 years old)) 
print (name == "Ellis" or not (name= "John" and age == 17))

# output: 
# True 
# False 
```

### 5.3 if

```python
name = "John" 
age = 17
if name== "John" and age == 18: # check that name 
    print("name is John")
	print("John is 17 years old")
    
tasks = ['taskl', 'task2'] # create new list 

# check if 'tasks' is empty
# print("empty") 
if len(tasks) != 0: 
    print ("have something") 
```

### 5.4..elif..else 条件语句

```python
x= 28

if x< o:
	print('x < 0')
elif x == 1:
    print('x is zero') 
elif x == 1:
    print('dx == 1')
else:
	print('non of the above is true')
```

### 5.5 for

```python
for i in range(5): 
    print(i)
    
primes = [2, 3, 5, 7] # create new list 
# iterate over primes using for loop 
# print(prime) 
for i in primes: 
    print(i)
```

### 5.6字符串迭代

```python
hello_world = "Hello, World!"

for ch in hello_world: # print each character from hello_world 
    print(ch)
    
length = 0 # initialize length variable

# count how many characters are in the hello_world using loop 
# length += 1 # add 1 to the length on each iteration 
# print(len(hello_world) == length)

for ch in hello_world: 
    length += 1 
print (length)
if len（hello_world） == length：
	print（“这是正确的”）
else:
	print（"这是错误的"）
```

## 6

### 6.1 while

```python
square = 1

while square <= 10:
	print(square) # This code is executed 10 times 
    square += 1   # This code is executed 10 times 
    
print("Finished") # This code is executed once
square = 0 
number = 1

# print all squares from O to 99 
# square = number ** 2
# print(square)
# number += 1 ###

while number <= 99: 
    square = number **2 
    print(square)
	number += 1 
```

### 6.2 break

```python
while True: # this condition cannot possibly be false 
    print(count)
	count += 1 
    if count >= 5: 
        break		# exit loop if count >= 5

zoo = ["lion", 'tiger', 'elephant']
# while True:  # this condition cannot possibly be false
# 	  animal = zoo.pop()		# extract one element from the list end
# 	  print(animal)
# 	  if exit loop if animal is 'elephant': 
# 	      break    # exit loop

while True:
	animal = z00.pop() 
    print (animal) 
    if animal == 'lion': 
        break
```

### 6.3 continue跳出当前循环中的剩余代码，回到下一次循环中

```python
for i in range(5):
	if i== 3:
		continue # skip the rest of the code inside loop for current i value 
    print(i)
    
# for x in range (10):
# 	if Check if x is even:
# 		continue 	# skip print(x) for this loop 
#	print(x)

for x in range (10): 
    if x % 2 == 0: 
        continue
	print(x) 
```

## 7

### 7.1 函数def函数名（函数体，代码块）：

```python
def hello_world(): # function named my_function
	print（“Hello， World！”）
    
for i in range(5):
	hello_world（）# call function defined above 5 times
```

### 7.2函数的参数

```python
def foo(x):  #x is a function parameter 
	print("x = " + str(x))
    
foo(5) # pass 5 to foo(). Here 5 is an argument passed to function foo. 
foo(10)

# define a function named 'square' that prints square of passed parameter 
# print(x ** 2)

def square(x): 
    print(x ** 2) 
    
square(4)
square(8) 
square(15) 
square(23) 
square(42)
```

### 7.3 函数返回值

```python
def sum_two_numbers (a, b):
    return a + b	# return result to the function caller
c= sum_two_numbers (3, 12) # assign result of function execution to variable 'c'
def fib(n):
	result = [] # 存储所有的斐波那契数列值
    a = 0
	b=1
	while a < n:
		result.append (a) 
        tmp_var = b 
        b=a+b 
        a = tmp_var 
    return result 
print(fh(10))
```

### 7.4 函数默认参数

```python
def hello(subject, name="Daniel"):
	printHeltos y name is s % (subject, name) 

hello("pycharm", "Jane")
hello("pycharm")
```

## 8

### 8.1 面向对象

对象 object
	客观存在的，具象的
类class
	抽象的概念

### 8.2 类

class MyClass：变量，函数
对象 myClass = MyClass（）
myClass.调用 变量及方法

```python
class MyClass: 
    variable = 10
	def foo(self): # we'll explain self parameter later in task 4 
        print("Hello from function foo")
        
my_object = MyClass() # variable "my_object" holds an object of the 
my_object. foo()

class Student: 
    name = 'Rose' 
    age =10
	def display(self):
		print("This is display function") 

student = Student()
student.display()
```

### 8.3 变量的访问

```python
class MyClass: 
    variablel = 1 
    variable2 = 2
    
	def foo(self): # we'll explain self parameter later in task 4 
        print("Hello from function foo")
        
my_object = MyClass() 
my_object1 = MyClass () 
my_object.variable2 = 3
# change value stored in variable2 in my_object 

print(my_objkct.variable2)
print(my_object1.variable2) 
my_object. foo()
# call method foo() of object my_object 
# print(value of variablel from my_object)
```

### 8.4类中变量的访问练习

```python
class Car:
	color = "
	def description(self):
		description_string = "This is a %s car." & self.color 
        return description_string
    
car1 = Car() 
car2 = Car()

rl.color = "blue" 
car2.color = "red"

print(car1.description())
print(car2pdescription())
```

### 8.5 self 关键字

python中的约定
在类的定义中，定义的方法第一个参数一定是self，表示的是对当前创建对象的引用

```python
class Complex:
	def create(self, real_part, imag_part): 
        self.r = real_part
		self.i = imag_part
class Calculator: 
    current = 0
	def add (self, amount): 
        # add number to current 
        self.current += amount
	def get_current (self): 
        return self.current
    
calculator = Calculator()
calculator.add (100)
print(calculator.gelt_current()) 
```

### 8.6 init方法

def_init_(self)
_init_方法 在对象创建过程中自动执行

```python
class Square:
    
	def init_(self):
	# special method init 
    	self.sides = 4
        
square = Square() 
print(square.sides) 

class Car:
	def init_(self, color): 
        self.color = color
        
car = Car("blue") # Note: you should not pass self 
print(caf.collor)
```

## 9

### 9.1 模块 

```html
<html>
Modules in Python are simply Python files with the .py extension containing oo0 Python definitions and statements.

Modules can be handy when you want to use your
function in a number of programs without copying its definition into each program. 

Modules are imported from other modules using the
"import" keyword and the file name without arr extension. 

The first time a module is loaded into a running Python script, it is initialized by executing the code in the module once. 
<br><br/>
Import the module my_module and use the hello_world function. 
<br/>
</html>
```

Calculator.py

```python
class Calculator:
    def init_(self):
        self.current = 0
    def add (self, amount):
        self.current += amount
    def get_current(self):
        return self.current
```

my_module.py

```python
def hello_world (name):
	print("Hello, World! My name is %s" % name)
```

imports.py

```python
import calculator my_module sson3

calc = calculator.Calculator()		# create new 
calc.add (2) 
print(calc.get_current()) 

# here import my_module
# call function hello_world from my_module

my_module.hello_world(“Daniel”)	
```

### 9.2 from...import 

```html
<html>
One form of the import statement imports names from a module directly 
into the importing module's symbol table.
This way you can use the imported name directly without the module_name prefix. 
<br><br/>
Import hello_world function from my_module. Check the difference with taskl.     
<br/>
</html>
```



```python
from calculator import Calculator

calc = Calculator() # here we can use Calculator class directly without 
calc.add (2)
print(calc.get_current())

from my_module import hello_world:
print (hello_world()) # Note: hello_world function used without prefix
```

### 9.3 内建模块

```python
import datetime random, math
print(datetime.datetime. today())
print (random. randint(1000, 9999)) 
print(math.pow(2, 3))
```

## 10

### 10.1 写文件

```html
<html>
If you open a file using "w" (write) as the second argument, 
a new empty file will be created.
Note that if another file with the same name exists,f it will be deleted. 
If you want to add some content to an existing file,
you should use the "a" (append) modifier. 
<br><br/>
Add elements from the "zoo" list to "output.txt". 
<br/>
</html>
```

```python
# 替换原有内容
zoo = ['lion', "elephant", 'monkey']
# if name== "main":
# f = open ("output.txt", add modifier) 
# for i in zoo:
# 		add the whole zoo to the output.txt 
# 		close the file

if _name== "_main_": 
    f = open("output.txt", 'w') 
    for i in zoo:
		f.write(i) 
	f.close()
    
# 在源文件内容后增加
zoo = ['lion', "elephant", 'monkey']
# if name== "main":
# f = open ("output.txt", add modifier) 
# for i in zoo:
# 		add the whole zoo to the output.txt 
# 		close the file

if _name== "_main_": 
    f = open("output.txt", 'a') 
    for i in zoo:
		f.write(i) 
	f.close()
```

### 10.2 读文件

```html
<html>
Python has a number of built-in functions to read and write information from a file on your computer. 
The "open" function is used to open a file.

The file can be opened in read mode (using "r" as the second argument) or 
in write mode (using "w" as the second argument).
The "open" function returns the file object. 
You need to store it to close the file later. 
<br/><br/>
Print the contents of "input.txt" to output. Print the first line of "input1.txt". 
<br>
</html>
```

```python
f = open("input.txt", "r")

for line in f. readlines (): 
    print(line)
aclose()

# fl = open("input1.txt", "r") 
# print only first line of fl 
# do not forget to close file 
f1 = open("input1.txt", "r") 
for line in f1. readlines (): 
    print(line)
f1.close()
```

print(type('hello'))
print(type(10))
print(type(True))
print(type(3.14))
print(type(None))

num = -100
print(type(num))


# 判断数据类型
print(isinstance(123,int))
print(isinstance('123',int))
print(isinstance(True,bool))


# 字符串的三种类型 单引号 双引号 三双引号(三引号可以多行显示)
str1 = '1223'
str2 = "1234"
str3 = """123
          456
          789     """

print(str1,str2,str3)

# 输出  大家好，我是李依诚，今年18岁，学习的专业是计算机科学与技术，爱好python，java
name = '李依诚'
age = 18
zhuan = '计算机科学与技术'
aihao = 'python,java'
print('大家好,我是' + name + ',今年' + str(age) + '岁，学习的专业是' + zhuan + ',爱好' + aihao)

print('大家好,我是%s,今年%s岁,学习的专业是%s,爱好是%s' % (name,age,zhuan,aihao))

print(f'大家好，我是{name}，今年{age}岁，学习的专业是{zhuan}，爱好{aihao}')
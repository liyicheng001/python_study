# 字面量的写法 
print(100)
print(3.14)
# 布尔型首字母要大写
print(True)
print(False)
# 字符串类型要用引号
print('hello world')
print('-------------')

print(None)

# 布尔类型本质也是整数类型
print(True + 1)
print(False - 1)




# 变量 py是动态类型语言 一个变量可以存储多种数据类型 但是平时使用一般只存储一种类型
num = 1114.1
print(num)

num = num + 1000
print(num)

num = "ok"
print(num)

# 案例 基础播放量20.7万 每个月增加50万播放 两个月后播放量为多少
base = 20.7
add = 50
sum = base + 2 * add
print('两个月后的播放总量为：',sum,'万')
print('两个月后的播放总量为：' + str(sum) + '万')


# 汉字也可以用来当标识符 但是不仅建议用
哈哈 = 123
print(哈哈)

#a=10 b=20 将两个变量赋值交换 输出
a = 10
b = 20
c = a
a = b
b = c
print(a,b)
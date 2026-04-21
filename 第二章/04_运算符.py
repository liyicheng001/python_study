# a = 10
# b = 20
# print(a == b)
# print(a != b)
# print(a < b)
# print(a > b)


# 输入一个数字，判断这个数字是否在10-20之间
num = int(input('请输入一个整数：'))
print(num >= 10 and num <= 20)


#输入一个数字,判断这个数字是否不在10-20之间
print(not(num >= 10 and num <= 20))
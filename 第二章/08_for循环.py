#遍历输入的字符串
# str = input('请输入字符串:')
# for i in str:
#     print(i)

# 计算1-100所有奇数之和
sum = 0
# for i in range(1,101):
#     if i % 2 != 0:
#         sum += i
for i in range(1,101,2):
    sum += i
print(sum)    

# 计算100-500之间所有3的倍数的数字之和
jum = 0
for i in range(100,501):
    if i % 3 == 0:
        jum += i 
# for i in range(102,501,3):
#     jum += i

print(jum)
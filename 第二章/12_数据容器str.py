# s = 'hello-python'

# print(s[4])
# print(s[6])

# for i in s:
#     print(i)


# print(s[0:5:1])

# print(s[6:12:1])

# # 如果是截取到末尾 直接省略就行
# print(s[6::1])

# # 步长为负数 从后往前截取 开始索引和结束索引都要反着来 可以实现反转字符串

# print(s[6:0:-1])

# # 整个字符串反转的话 两个索引全部省略就行
# print(s[::-1])


# 用户输入一个邮箱，验证邮箱格式是否正确（包含一个@和至少一个.）如果输入正确 输出正确

# while True:
#     email = input('请输入邮箱：')

#     if email.count('@') == 1 and email.find('.') >= 0:
#       print('输出正确')
#       break
#     else:
#       print('输出错误')


# while True:
#     email = input('请输入邮箱：')

#     if email.count('@') == 1 and "." in email:
#       print('输出正确')
#       break
#     else:
#       print('输出错误')


# 判断是否是回文
# str = input('请输入字符串：')

# for i in range(len(str)):
#     if str[i] != str[-i-1]:
#         print('该字符串不是回文')
#         break
# else:
#     print('该字符串是回文')

arr = []

for i in range(10):
   str = input('请输入字符串')
   
#    反转
   str1 = str[::-1]
   arr.append(str1)


for i in arr:
   print(i)

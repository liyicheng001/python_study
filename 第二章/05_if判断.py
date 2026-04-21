#分数超过650 就上清华
# num = int(input('请输入分数：'))
# if num >= 650:
#    print('上清华')
# else:
#    print('回家种地')

   
# print('123')


# 完成登录 测试账户为 18888888888 666888
# username = input('请输入用户名：')
# password = input('请输入密码：')
# if username == '18888888888' and password == '666888' :
#     print('登录成功')
# else:
#     print('用户名密码错误，请重新输入')
  

#根据用户输入的年份,判断这一年是闰年还是平年
 #非整百年份,且能被4整除的年份是闰年
 #整百年份(1900,2000)必须能被400整除才是闰年
# year = int(input('请输入年份:'))

# if (year % 100 !=0 and year % 4 == 0) or year % 400 == 0:
#     print('闰年')
# else:
#     print('平年')


#根据用户输入的数字，判断数字是奇数还是偶数
# num = int(input('请输入数字：'))
# if num % 2 == 0:
#     print('输入的数字为偶数')
# else:
#     print('输入的数字为奇数')

#根据用户输入的年龄，判断是否已经成年 >= 18
# age = int(input('请输入年龄：'))
# if age >= 18:
#     print('已成年')
# else:
#     print('未成年')

#根据用户输入的数字，判断数字是正数还是负数 不考虑0
# num1 = int(input('请输入数字：'))
# if num1 > 0:
#     print('输入的数字为正数')
# elif num1 < 0: 
#     print('输入的数字为负数')
# else:
#     print('输入的数字为0')

#根据用户输入的考试分数，判断该分数是否及格>=60
# fen = int(input('请输入成绩:'))
# if fen >= 60:
#     print('成绩合格')
# else:
#     print('成绩不合格')

#登录 用户名是 admin/666888  root/654321  ceshi/123456都可以登录
# username = input('请输入用户名:')
# password = input('请输入密码:')
# if username == 'admin' and password == '666888':
#     print('登录成功')
# elif username == 'root' and password == '654321':
#     print('登录成功')
# elif username == 'ceshi' and password == '123456':
#     print('登陆成功')
# else:
#     print('用户名密码错误')

# if (username == 'admin' and password == '666888') or (username == 'root' and password == '654321') or (username == 'ceshi' and password == '123456'):
#     print('登录成功')
# else:
#     print('用户名密码错误')

# 根据输入的三个边的边长(正整数) 判断是等边三角形 等腰三角形 普通三角形 还是不能构成三角形
  #构成三角行的条件 两边之和大于第三边
  #三个边相等 等边
  #两个边相等 等腰
  #都不相等  普通

# a = int(input('请输入边长a:'))
# b = int(input('请输入边长b:'))
# c = int(input('请输入边长c:'))

# if a + b <= c or b + c <= a or a + c <= b:
#     print('当前不是三角形')
# elif a == b == c:
#     print('当前为等边三角形')
# elif (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
#     print('当前为等腰三角形')
# else:
#     print('当前是普通三角形')

#match
a = int(input('请输入数字1-7:'))

match a:
    case 1:
        print('周一')
    case 2:
        print('周二')
    case 3:
        print('周三')
    case 4:
        print('周四')
    case 5:
        print('周五')
    case 6 | 7:
        print('周末休息')
    case _:
        print('输入错误')
# 打印一个长度为m 宽度为n的长方形
# m = int(input('请输入长度m:'))
# n = int(input('请输入宽度n:'))

# for i in range(n):
#     for j in range(m):
#         print('*', end=' ')
#     print()

#99乘法表
# for i in range(1,10):
#     for j in range(1,i + 1):
#       print(f'{j} * {i} = {j * i}' ,end = "\t")
#     print()

# 输入用户名和密码
# 1.正确的用户名明明是admin/666888,zhangsan/123456,taoge/888666
# 2.输入的用户名和密码进行登录，直到登录成功，程序结束运行，如果登陆失败，则继续输入用户名和密码
# 3.输入的用户名和密码不能为空
# 4.登录成功，输出 登录成功，进入b站首页
# 5.登录失败，输出 用户名或密码错误，请重新输入
# isLogin = False

# while not isLogin:
#   username = input('请输入用户名：')
#   password = input('请输入密码：')

#   if username and password:
#     if (username == "admin" and password == "666888") or (username == 'zhangsan' and password == '123456') or (username == 'taoge' and password == '888666'):
#        print('登录成功，进入b站首页')
#        isLogin = True
#        #break跳出循环时 else结束循环的代码块将不会被执行
#        break
#     else:
#        print('用户名和密码错误，请重新输入')


# 随机生成一个随机数
# 用户数根据提示数字，输入数字
# 如果猜错 系统提示是猜大了 还是猜小了 然后继续让用户输入
# 如果才对 系统退出 游戏结束

import random
rdm = random.randint(1,100)



while True:
    num = int(input('请输入数字：'))
    if rdm > num:
      print('猜小了')
    elif rdm < num:
      print('猜大了')
    else:
      print('猜对了，恭喜')
      break
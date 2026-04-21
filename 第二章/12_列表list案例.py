#将用户输入的10个数字 存储到一个列表中，将列表的数字进行排序 输出其中的最小值，最大值和平均值
# arr = []

# for i in range(10):
#     num = int(input('请输入数字：'))
#     arr.append(num)

# arr.sort()
# print(arr)

# print(f'最小值为：{min(arr)}')
# print(f'最大值为：{max(arr)}')




# print(f'平均值为{sum(arr) / len(arr)}')

#合并去重
# num_list1 = [19,23,54,64,875,20,109,232,123,54]
# num_list2 = [55,88,72,35,60,123,54,29,91]

# #合并
# # for i in num_list2:
# #     num_list1.append(i)

# # num_list1 = [*num_list1,*num_list2]
# num_list1 = num_list1 + num_list2

# print(num_list1)


# arr = []

# for i in num_list1:
#     # in 可以判断一个元素是否存在一个列表中
#     if i not in arr:
#         arr.append(i)


# print(arr)


#生成1-20的平方列表
# arr = []
# for i in range(1,21):
#    arr.append(i * i)
# [要插入的值 for i in 列表 if 条件]
# arr = [ i * i for i in range(1,21)]
# print(arr)


# #从如下数字列表中提取所有偶数 计算其平方 组成一个新的列表
# #[19,23,54,64,87,20,109,232,123,43,26,55,72]
# num = [19,23,54,64,87,20,109,232,123,43,26,55,72]
# # num1 = []
# # for i in num:
# #    if i % 2 == 0:
# #       num1.append(i * i)
# num1 = [i * i for i in num if i % 2 == 0]

# print(num1)




# 将如下列表合并为一个列表 并去除重复元素，拍好序列（升序）后输出
# list1 = ['A', 'C', 'F', 'B']
# list2 = ['D', 'A', 'G', 'E']
# list3 = ['B', 'H', 'F', 'D']

# list = list1 + list2 + list3

# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)

# new_list.sort()
# print(new_list)

#如下列表中能被3或5整除的元素提出来，并获取这些数字的平方 组成一个新的列表
# list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# new_list = [i * i for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(new_list)

import time

for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    time.sleep(0.05)
print()
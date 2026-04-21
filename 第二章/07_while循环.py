#打印10遍 人生苦短,我学python~
# a = 0
# while a < 10:
#    print('人生苦短,我学python~')
#    a += 1
# else:
#    print('循环结束')


#计算1-100之间所有偶数累加之和
a = 1
sum = 0
while a <= 100:
    if a % 2 == 0:
        sum += a
    a += 1    
else:
    print(f'和为{sum}')
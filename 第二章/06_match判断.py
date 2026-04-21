#计算器 用户输入+ - * / 和两个数字之后 进行计算输出结果
a = int(input('请输入数字A:'))
b = int(input('请输入数字B:'))

c = input('请输入运算符(+ - * /):')

match c:
    case '+':
        print(f'和为{a + b}')
    case '-':
        print(f'差为{a - b}')
    case '*':
        print(f'积为{a * b}')
    case '/':
        print(f'商为{a / b}')
    case _:
        print('输入错误,请输入正确的运算符')
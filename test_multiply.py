# -*- coding:utf-8 -*-
import os
import random

# 测试次数
count = 5

# 错误次数
fail = 0

# 错题集合
fail_set = []


def clear():
    os.system('clear')


def initialize():
    """
    初始化
    """
    clear()
    print('乘法口诀表考试开始，贝贝加油哦!\n')
    input('准备好了吗?')
    clear()


def test():
    """
    测试
    """
    global count
    global fail

    for i in range(1, count + 1):
        left = random.randint(1, 9)
        right = random.randint(1, 9)
        print(f'习题{i}: \n')
        print(f'{left} * {right} = \n')
        result = input('答案: ')
        if result != str(left * right):
            print(f'\033[1;31m错误！正确答案是: {left * right}\033[0m\n')
            fail += 1
            fail_set.append(f'{left} * {right} =')
        else:
            print(f'\033[1;32m回答正确\033[0m\n')

        input('进入下一题')
        clear()


def showScore():
    """
    显示得分
    """
    score = (count - fail) * 100.0 / count
    comment = '不及格'
    if score >= 90:
        comment = '优秀'
    elif score >= 70:
        comment = '良好'
    elif score >= 60:
        comment = '及格'
    print(f'考试完成，成绩{comment}, 分数:{score}!\n')


def showFailSet():
    """
    显示错题
    """
    if len(fail_set) == 0:
        return

    print('\033[1;31m错题列表:\033[0m\n')
    for s in fail_set:
        print(f'{s}\n')


initialize()
test()
showScore()
showFailSet()

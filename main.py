# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time
import threading


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sing():
    for i in range(5):
        print("正在唱歌")
        time.sleep(1)


def dance():
    for i in range(10):
        print("正在跳舞")
        time.sleep(1)


def main():
    # 多任务，时间片轮转, 线程调用无先后顺序
    t1 = threading.Thread(target=sing)  # sing 不能写成 sing()
    t2 = threading.Thread(target=dance)
    t1.start()  # 到这里就跳到 sing 单独执行
    print("1")

    t2.start()
    print("2")

    while True:
        print(threading.enumerate())
        time.sleep(1)


# class Cat:
#     def eat_fish(self):
#         print("%s eat fish" % self.name)
#
#     def drink(self):
#         print("drink")

# class Cat:
#     def __init__(self):
#         print("这是一个初始化方法")
#         self.name = "Tom"

class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


    # print_hi('PyCharm')
    #
    # # 运算
    # price_apple = float(input("苹果的单价 = "))
    # weight_apple = float(input("苹果的重量 = "))
    # money = price_apple * weight_apple
    # print(f"money = {money}")
    #
    # # 三种输出测试
    # name = input("Your name = ")
    # print("my name is %s" % name)
    # print(f"my name is {name}")
    # print("my name is {}".format(name))
    #
    # # if
    # age = int(input("your age = "))
    # # EE
    # if age >= 18:
    #     print("able")
    # else:
    #     print("unable")
    #
    # # 石头剪刀布
    # player = int(input("请出拳——石头（1）、剪刀(2)、布（3）= "))
    # computer = random.randint(1, 3)
    # if ((player == 1)
    #         or (player == 2)
    #         or (player == 3)):
    #     if ((player == 1 and computer == 2)
    #             or (player == 2 and computer == 3)
    #             or (player == 3 and computer == 1)):
    #         print("玩家获胜")
    #     elif (player == 1 and computer == 1) or (player == 2 and computer == 2) or (player == 3 and computer == 3):
    #         print("平局")
    #     else:
    #         print("电脑胜")
    # else:
    #     print("输入错误")

    # 分步编写代码

    # # 面向类的编程
    # tom = Cat()
    # print(tom.name)
    # # 不推荐的 外部添加属性的方法
    # # tom.name = "Xie"
    # tom.eat_fish()
    # tom.drink()
    #
    # print(tom)
    # addr = id(tom)
    # print("%d" % addr)
    #
    # lazy_cat = Cat()
    # lazy_cat.name = "大懒猫"
    # lazy_cat.drink()
    # lazy_cat.eat_fish()
    # print(lazy_cat)
    #
    # # lazy_cat2 和 lazy_cat 是同一只猫，见打印的地址
    # lazy_cat2 = lazy_cat
    # print(lazy_cat2)

    # # 不推荐的 外部添加属性的方法
    # tom.name = "Xie"

    # #使用外部传入对象的属性
    # tom = Cat("xie")
    # print(tom.name)

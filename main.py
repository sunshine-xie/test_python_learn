# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def main():
    print('Hello World!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    price_apple = float(input("苹果的单价 = "))
    weight_apple = float(input("苹果的重量 = "))
    money = price_apple * weight_apple
    print(f"money = {money}")

    name = input("Your name = ")
    print("my name is %s" % name)
    print(f"my name is {name}")
    print("my name is {}".format(name))

    age = int(input("your age = "))
    # EE
    if age >= 18:
        print("able")
    else:
        print("unable")

    player = int(input("请出拳——石头（1）、剪刀(2)、布（3）= "))
    computer = random.randint(1, 3)
    if((player == 1)
            or (player == 2)
            or (player == 3)):
        if ((player == 1 and computer == 2)
                or (player == 2 and computer == 3)
                or (player == 3 and computer == 1)):
            print("玩家获胜")
        elif (player == 1 and computer == 1) or (player == 2 and computer == 2) or (player == 3 and computer == 3):
            print("平局")
        else:
            print("电脑胜")
    else:
        print("输入错误")



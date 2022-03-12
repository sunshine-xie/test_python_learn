# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


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




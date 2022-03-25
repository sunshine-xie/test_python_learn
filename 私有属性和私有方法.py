# 在属性前增加两个下划线
class Man:
    def __init__(self, name):
        self.name = name
        self.age = 18

    def secret(self):
        print(f"年龄为{self.age}")


ming = Man("ming")
print(ming.age)
ming.secret()


class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 19

    def __secret(self):
        print(f"年龄为{self.__age}")


hong = Women("hong")
print(hong.__age)
hong.__secret()

# 可以这样但不要用
# hong._Women__secret()





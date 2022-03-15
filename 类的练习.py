"""
# 小明、小美跑步
class Person:
    def __init__(self, name, weight):
        # 属性
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，体重是%.2f公斤" %(self.name, self.weight)

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


ming = Person("小明", 100)
# weight = ming.run()
# print(weight)
print(ming)
ming.eat()
print(ming)

ming.eat()
print(ming)

ming.run()
print(ming)

mei = Person("小美", 45)
print(mei)

mei.run()
print(mei)
"""


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.unused_area = area
        self.furniture = []

    def __str__(self):
        return (f"房子的类型是：{self.house_type}\n总面积为：{self.area}\n"
                f"剩余面积为:{self.unused_area}\n家具有{self.furniture}")

    def add_furniture(self, furniture_name):
        self.furniture.append(furniture_name)
        if furniture_name == "bed":
            if self.unused_area >= 4:
                self.unused_area -= 4
            else:
                print("剩余面积不足")
                self.furniture.pop()

        elif furniture_name == "chest":
            if self.unused_area >= 2:
                self.unused_area -= 2
            else:
                print("剩余面积不足")
                self.furniture.pop()

        elif furniture_name == "table":
            if self.unused_area >= 1.5:
                self.unused_area -= 1.5
            else:
                print("剩余面积不足")
                self.furniture.pop()

        else:
            print("输入错误")
            self.furniture.pop()


xie_house = House("xie", 100)
xie_house.add_furniture("bed")
# xie_house.add_furniture("")

xie_house.add_furniture("chest")

xie_house.add_furniture("table")

print(xie_house)





















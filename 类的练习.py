# 小明、小美跑步
"""
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

# 不成功的类，家具房子
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
"""

# 类之间的调用，家具房子，房子类调用 家具类实例化的对象，在房子类中对家具类中的对象进行调用
# 如，在house.add_furniture中调用bed.furniture_name 和 bed.furniture_area
"""
class Furniture:
    def __init__(self, furniture_name, furniture_area):
        self.furniture_name = furniture_name
        self.furniture_area = furniture_area

    def __str__(self):
        return f"家具名称:{self.furniture_name}\n占地空间:{self.furniture_area}平米\n"


class House:
    def __init__(self, house_type, house_area):
        self.house_type = house_type
        self.house_area = house_area
        self.house_unused_area = house_area
        self.furniture_list = []

    def __str__(self):
        return (f"房子的类型：{self.house_type}\n"
                f"总面积：{self.house_area}平米\n"
                f"剩余面积:{self.house_unused_area}平米\n"
                f"家具名称列表：{self.furniture_list}\n")

    def add_furniture(self, furniture):
        if furniture.furniture_area > self.house_unused_area:
            print("剩余面积不足, 无法添加")
            return
        print(f"要添加的家具为{furniture}")
        self.furniture_list.append(furniture.furniture_name)
        self.house_unused_area -= furniture.furniture_area


bed = Furniture("席梦思", 4)
chest = Furniture("衣柜", 2)
desk = Furniture("餐桌", 1.5)
print(bed)
print(chest)
print(desk)

xiao_ming = House("别墅", 6)
print(xiao_ming)

xiao_ming.add_furniture(bed)
print(xiao_ming)

xiao_ming.add_furniture(chest)
print(xiao_ming)

xiao_ming.add_furniture(desk)
print(xiao_ming)
"""

# 士兵突击，有问题

class Soldier:
    def __init__(self, name, gun):
        self.name = name
        # self.gun = gun.gun_type
        # self.gun_unused_bullet = gun.gun_unused_bullet
        self.gun = gun
    def __str__(self):
        return f"我叫{self.name}\n我的武器是{self.gun.gun_type}\n剩余弹量：{self.gun.gun_unused_bullet}\n"
#这里自己写的有问题
    def fire(self, idx):
        if(idx == 0):
            print("正在开火")
            self.gun.gun_unused_bullet -= 1
            print(f"剩余子弹:{self.gun.gun_unused_bullet}\n")


class Gun:
    def __init__(self, gun_type, gun_bullet):
        self.gun_type = gun_type
        self.gun_bullet = gun_bullet
        self.gun_unused_bullet = 0

    def __str__(self):
        return (f"枪的名字：{self.gun_type}\n"
                f"枪的剩余子弹：{self.gun_unused_bullet}\n")

    def add_bullet(self, count):
        if self.gun_unused_bullet < self.gun_bullet:
            self.gun_unused_bullet += count
            print(f"剩余子弹:{self.gun_unused_bullet}\n")


xu = Soldier("许三多", Gun("AK47", 30))
print(xu)
xu.gun.add_bullet(30)
xu.fire(0)

#  此处的ak47和许三多拿的不是同一把
print(xu)


xu.fire(0)
print(xu)


# class Gun:
#     def __init__(self, gun_type):
#         # 枪的型号
#         self.gun_type = gun_type
#         # 枪的子弹数量
#         self.gun_bullet = 0
#
#     def __str__(self):
#         return (f"枪的名字：{self.gun_type}\n"
#                 f"弹夹剩余子弹数{self.gun_bullet}\n")
#
#     def add_bullet(self, count):
#         self.gun_bullet += count
#
#     def shoot(self):
#         if self.gun_bullet <= 0:
#             print("没有子弹了")
#         else:
#             self.gun_bullet -= 1
#             print(f"tu tu tu.....[{self.gun_bullet}]")
#
#
# class Soldier:
#     def __init__(self, name):
#         self.name = name
#         self.gun = None
#         self.a = 10
#         self.b = "s"
#         self.c = 10
#     # def __str__(self):
#     #     return f"我叫{self.name}\n"
#
#     def fire(self):
#         if self.gun is None:
#             print("我没有枪")
#             return
#         print("冲啊...")
#         self.gun.add_bullet(50)
#         self.gun.shoot()
#
#     def pr(self):
#         print(id(self.name))
#         print(self.name.__sizeof__())
#         print(self.a)
#
# ak47 = Gun("AK47")
# print(ak47)
#
# # ak47.add_bullet(50)
# # ak47.shoot()
#
#
# xu = Soldier("xu")
# print(xu)
# print(xu.__sizeof__())
#
# xu.gun = ak47
# # xu.fire()
# # xu.fire()
# na = "ss12"  # 字符串+string
# xu.pr()
# # print(na.__sizeof__())
# # xu.getsizeof()
# print(xu.__sizeof__())
#
#
# print(xu)


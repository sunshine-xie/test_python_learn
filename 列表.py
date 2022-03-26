# 列表 list 对应其他语言数组
name = ["zhu", "xie", "tang"]
#        |-------|-------|-------|-------------
#        |   0   |   1   |   2   |
#        |-------|-------|-------|-------------

# 方法
name_list = ["zhang san", "li si", "wang wu"]
print(name_list)

# 取值
print(name_list[0])

# 取索引
name_list.index("li si")
print(name_list.index("li si"))

# 使用index方法要注意，如果数据不在列表中会报错
# print(name_list.index("lisi321"))

# 修改某个指定位置的数据
name_list[1] = "李四"
print(name_list)

# 向列表中添加数据
# append insert extend
# append 向末尾添加数据
name_list.append("王小二")
print(name_list)
# insert 在指定索引位置前插入数据
name_list.insert(1, "小美")
print(name_list)
# extend 把另外一个列表的完整内容追加到当前列表末尾
name_list.extend(name)
print(name_list)

# 列表中删除数据

# remove clear pop
#   remove
name_list.remove("小美")
print(name_list)
#   pop 默认删除列表中最后一个元素
name_list.pop()
print(name_list)
#   clear 清空列表
# name_list.clear()
# print(name_list)

# del关键字 delete, 用来把变量从内存中删除
del name_list[0]
print(name_list)

# # 这样用是有报错的，del以后就不可以用了，在日常中建议使用list自带方法
# del name_list
# print(name_list)

# 查看长度 len count
# len
list_len = len(name_list)
print(list_len)
# count
count = name_list.count("zhu")
print(count)

# 排序 .sort（）, .sort(reverse = True), .sorted()
# 倒着打印列表 .reverse()


# 列表遍历
for i in name_list:
    # # 这样是错的，知道为什么！！！！！
    # print(name_list[i])
    print(i)

print(name_list)















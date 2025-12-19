# 数据结构练习
# 列表、元组、字典、集合的用法

# 列表操作
def list_operations():
    my_list = [1, 2, 3, 4, 5]
    # 添加元素
    my_list.append(6)
    # 删除元素
    my_list.remove(3)
    # 切片操作
    sliced = my_list[1:4]
    return my_list, sliced

# 元组练习
def tuple_example():
    coordinates = (10, 20)
    # 元组解包
    x, y = coordinates
    return x, y

# 字典操作
def dict_operations():
    student = {"name": "李四", "score": 85}
    # 添加键值对
    student["grade"] = "A"
    # 遍历字典
    for key, value in student.items():
        print(f"{key}: {value}")
    return student

# 集合练习
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    # 并集
    union = set1 | set2
    # 交集
    intersection = set1 & set2
    return union, intersection

if __name__ == "__main__":
    print("数据结构练习开始...")

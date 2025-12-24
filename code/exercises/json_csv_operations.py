# JSON和CSV文件处理练习
# C.14 JSON和CSV文件处理

import json
import csv

print("=== JSON和CSV文件处理练习 ===")
print("学习目标：掌握结构化数据文件的处理方法")

# 1. JSON文件操作 - 写入
print("\n1. JSON文件写入操作")

# 创建一些学生数据（字典格式）
students_data = [
    {"name": "张三", "age": 20, "major": "计算机科学", "courses": ["数学", "编程"]},
    {"name": "李四", "age": 19, "major": "物理学", "courses": ["物理", "数学"]},
    {"name": "王五", "age": 21, "major": "文学", "courses": ["文学", "历史"]}
]

# 将数据写入JSON文件
try:
    with open('students.json', 'w', encoding='utf-8') as json_file:
        json.dump(students_data, json_file, ensure_ascii=False, indent=2)
    print("✅ JSON文件写入成功！")
except Exception as e:
    print(f"❌ JSON写入失败: {e}")

# 2. JSON文件操作 - 读取
print("\n2. JSON文件读取操作")

try:
    with open('students.json', 'r', encoding='utf-8') as json_file:
        loaded_students = json.load(json_file)
        
    print("从JSON文件读取的学生数据：")
    for i, student in enumerate(loaded_students, 1):
        print(f"学生{i}: {student['name']}, {student['age']}岁, 专业: {student['major']}")
        print(f"   课程: {', '.join(student['courses'])}")
    
    print("✅ JSON文件读取成功！")
except FileNotFoundError:
    print("❌ JSON文件不存在")
except Exception as e:
    print(f"❌ JSON读取失败: {e}")

# 3. CSV文件操作 - 写入
print("\n3. CSV文件写入操作")

# 创建课程数据（表格格式）
courses_data = [
    ["课程编号", "课程名称", "教师", "学分"],
    ["CS101", "计算机基础", "张老师", "3"],
    ["MA201", "高等数学", "李老师", "4"],
    ["PH301", "物理学导论", "王老师", "3"],
    ["EN401", "英语写作", "赵老师", "2"]
]

try:
    with open('courses.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(courses_data)
    print("✅ CSV文件写入成功！")
except Exception as e:
    print(f"❌ CSV写入失败: {e}")

# 4. CSV文件操作 - 读取
print("\n4. CSV文件读取操作")

try:
    with open('courses.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        
        print("从CSV文件读取的课程数据：")
        for row_num, row in enumerate(reader):
            if row_num == 0:  # 表头
                print("表头:", " | ".join(row))
                print("-" * 40)
            else:
                print(f"课程{row_num}: {row[0]} | {row[1]} | {row[2]} | {row[3]}学分")
    
    print("✅ CSV文件读取成功！")
except FileNotFoundError:
    print("❌ CSV文件不存在")
except Exception as e:
    print(f"❌ CSV读取失败: {e}")

# 5. 字典格式的CSV操作（更实用的方式）
print("\n5. 字典格式的CSV操作")

student_records = [
    {"学号": "2023001", "姓名": "张三", "成绩": "85"},
    {"学号": "2023002", "姓名": "李四", "成绩": "92"},
    {"学号": "2023003", "姓名": "王五", "成绩": "78"}
]

try:
    # 写入字典格式的CSV
    with open('student_records.csv', 'w', encoding='utf-8', newline='') as csv_file:
        fieldnames = ["学号", "姓名", "成绩"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()  # 写入表头
        writer.writerows(student_records)  # 写入数据行
    
    print("✅ 字典格式CSV写入成功！")
    
    # 读取字典格式的CSV
    with open('student_records.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        
        print("字典格式CSV读取结果：")
        for record in reader:
            print(f"学号: {record['学号']}, 姓名: {record['姓名']}, 成绩: {record['成绩']}")
    
    print("✅ 字典格式CSV读取成功！")
    
except Exception as e:
    print(f"❌ 字典格式CSV操作失败: {e}")

print("\n=== JSON和CSV文件处理练习完成 ===")
print("请检查生成的文件，理解不同数据格式的特点")
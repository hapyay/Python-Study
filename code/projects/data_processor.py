# 数据处理项目
# 文件读写和数据处理练习

import csv
import json
from datetime import datetime

class DataProcessor:
    def __init__(self):
        self.data = []
    
    def read_csv(self, filename):
        """读取CSV文件"""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = list(reader)
            print(f"成功读取 {len(self.data)} 条数据")
            return True
        except FileNotFoundError:
            print(f"文件 {filename} 不存在")
            return False
    
    def process_data(self):
        """处理数据"""
        if not self.data:
            print("没有数据可处理")
            return
        
        # 简单的数据处理示例
        processed = []
        for item in self.data:
            # 这里可以根据实际数据结构进行处理
            processed_item = {**item, "processed_at": datetime.now().isoformat()}
            processed.append(processed_item)
        
        return processed
    
    def save_json(self, data, filename):
        """保存为JSON文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            print(f"数据已保存到 {filename}")
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False

def create_sample_csv():
    """创建示例CSV文件"""
    sample_data = [
        {"name": "张三", "age": "25", "city": "北京"},
        {"name": "李四", "age": "30", "city": "上海"},
        {"name": "王五", "age": "28", "city": "广州"}
    ]
    
    with open('sample_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age", "city"])
        writer.writeheader()
        writer.writerows(sample_data)
    
    print("已创建示例文件: sample_data.csv")

if __name__ == "__main__":
    processor = DataProcessor()
    
    # 创建示例文件
    create_sample_csv()
    
    # 处理数据
    if processor.read_csv('sample_data.csv'):
        processed_data = processor.process_data()
        processor.save_json(processed_data, 'processed_data.json')

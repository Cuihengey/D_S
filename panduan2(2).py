import pandas as pd

# 读取原始CSV文件
input_file = 'output_2020.csv'

# 创建一个新的DataFrame用于存储属性值全都不相同的行
unique_rows = []

with open(input_file, 'r') as file:
    header = file.readline()
    unique_rows.append(header)

    for line in file:
        row = line.strip().split(',')
        if row[1] != row[2] and row[2] != row[3] and row[1] != row[3]:
            unique_rows.append(line)

# 保存满足条件的行到新的CSV文件
output_file = 'unique_values_output_2020.csv'
with open(output_file, 'w') as file:
    file.writelines(unique_rows)

print(f"已提取并保存属性值全都不相同的行到 {output_file}")

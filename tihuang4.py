import csv

# 读取第一个文件
first_file = 'sample_1995.csv'  # 你需要替换成你的第一个文件路径
second_file = '1995_csj.csv'  # 你需要替换成你的第二个文件路径
output_file = 'uion_1995.csv'  # 保存结果的文件路径

# 创建一个字典来存储第二个文件的数据
replacement_data = {}
with open(second_file, 'r') as second_csv:
    second_reader = csv.reader(second_csv)
    next(second_reader)  # 跳过第一行（列名）
    for row in second_reader:
        if len(row) >= 2:
            sequence_number, attribute_value = row
            replacement_data[sequence_number] = attribute_value

# 逐行处理第一个文件，将第二个文件的数据替换进去并保存到输出文件
with open(first_file, 'r') as first_csv, open(output_file, 'w', newline='') as output_csv:
    first_reader = csv.reader(first_csv)
    output_writer = csv.writer(output_csv)

    # 跳过第一行（列名）
    next(first_reader)

    for row in first_reader:
        if len(row) >= 2:
            sequence_number, attribute_value = row
            # 如果在第二个文件中找到相同的序号，则替换为第二个文件的属性值
            if sequence_number in replacement_data:
                attribute_value = replacement_data[sequence_number]
            output_writer.writerow([sequence_number, attribute_value])

print("替换完成")










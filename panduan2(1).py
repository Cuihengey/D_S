import csv
from tqdm import tqdm

# 打开原始CSV文件和新的CSV文件
with open('output_2005.csv', 'r') as infile, open('sample_2005.csv', 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # 读取原始文件的列名
    header = next(reader)
    writer.writerow(['FID', 'uion'])

    # 初始化集合用于跟踪已经出现的属性值
    seen_values = set()

    # 获取原始文件的行数，用于创建进度条
    num_lines = sum(1 for line in open('output_2005.csv'))

    # 遍历原始文件的每一行，使用tqdm创建进度条
    for row in tqdm(reader, total=num_lines, desc="Processing"):
        # 提取第一列（序号）和第二到第四列的属性值
        index = row[0]
        values = row[1:4]

        # 检查是否有两两相同和三个都相同的属性值
        if len(set(values)) == 1:
            # 保存序号和相同的属性值到新文件
            writer.writerow([index, values[0]])
        else:
            # 保存序号和第二列的属性值到新文件
            writer.writerow([index, values[0]])

        # 将属性值添加到集合中
        seen_values.update(values)

# 关闭文件
infile.close()
outfile.close()

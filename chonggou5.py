import csv
import torch
from osgeo import gdal, gdalconst
from tqdm import tqdm

# 打开CSV文件并读取第二列数据
csv_file = 'uion_1995.csv'  # 请替换为您的大型CSV文件
data_column = []

# 获取遥感图像的信息
original_image_file = 'E:\\shiyan\\1\\LUCC\\2000\\csj_lucc_2000.tif'  # 请替换为您的遥感图像文件
original_ds = gdal.Open(original_image_file)
num_cols = original_ds.RasterXSize
num_rows = original_ds.RasterYSize

# 获取原始图像的数据类型
original_data_type = original_ds.GetRasterBand(1).DataType

# 创建一个二维数组来存储像素值，形状与遥感图像一致
pixel_array = torch.zeros((num_rows, num_cols), dtype=torch.float32)

with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 跳过列名行

    for i,  row in enumerate(tqdm(reader, desc="Processing Rows")):
        pixel_value = float(row[1])  # 从第二列读取数据
        row_idx = i // num_cols
        col_idx = i % num_cols
        pixel_array[row_idx, col_idx] = pixel_value

# 现在，pixel_array 包含了按照遥感图像形状重新排列的第二列数据

new_image_file = 'new_image_csj_1995.tif'

# 创建一个新的遥感图像文件，与原始图像一致
driver = gdal.GetDriverByName('GTiff')
new_ds = driver.Create(new_image_file, num_cols, num_rows, 1, original_data_type)  # 使用原始图像的数据类型

# 设置地理元数据信息（投影、地理变换等）
new_ds.SetProjection(original_ds.GetProjection())
new_ds.SetGeoTransform(original_ds.GetGeoTransform())

# 将PyTorch张量转换为NumPy数组并写入新图像
pixel_array_np = pixel_array.cpu().numpy()
new_ds.GetRasterBand(1).WriteArray(pixel_array_np)

# 关闭新图像文件
new_ds = None

print(f"新的遥感图像已成功创建并保存为 {new_image_file}，并具有与原始遥感图像相同的元数据和数据类型。")



from osgeo import gdal
import csv


# 定义三个影像文件的路径
image1_path = "E:\\shiyan\\1\\CLCD\\2000\\csj_re2000.tif"
image2_path = "E:\\shiyan\\1\\LUCC\\2000\\csj_lucc_2000.tif"
image3_path = "E:\\shiyan\\1\\GLC\\2000\\csj_glc_2000z.tif"

# 打开影像文件
image1_ds = gdal.Open(image1_path)
image2_ds = gdal.Open(image2_path)
image3_ds = gdal.Open(image3_path)

# 创建CSV文件并写入列名
csv_file = "output_2000.csv"
with open(csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["FID", "CLCD", "LUCC", "GLC"])

    # 逐行提取信息并写入CSV
    for row in range(image1_ds.RasterYSize):
        for col in range(image1_ds.RasterXSize):
            # 获取每个影像的像素值
            image1_value = image1_ds.GetRasterBand(1).ReadAsArray(col, row, 1, 1)[0, 0]
            image2_value = image2_ds.GetRasterBand(1).ReadAsArray(col, row, 1, 1)[0, 0]
            image3_value = image3_ds.GetRasterBand(1).ReadAsArray(col, row, 1, 1)[0, 0]

            # 写入CSV
            csvwriter.writerow([row * image1_ds.RasterXSize + col, image1_value, image2_value, image3_value])

# 关闭影像文件
image1_ds = None
image2_ds = None
image3_ds = None

print("CSV文件已创建并写入数据。")


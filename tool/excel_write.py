import openpyxl

# 创建一个新的工作簿
workbook = openpyxl.Workbook()

# 选择默认的工作表（通常是第一个工作表）
sheet = workbook.active

# 在单元格中写入数据
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# 保存工作簿到文件
workbook.save('excel_file/write_file.xlsx')

print("Excel文件创建并写入成功！")

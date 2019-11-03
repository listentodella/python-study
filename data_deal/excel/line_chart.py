# -*- coding:utf-8 -*-

import xlsxwriter

# read file, 按行创建一个列表
f0 = open('hall0.txt', 'r', encoding='utf-8')
content_list0 = [i for i in f0 if 'mag' in i]
f0.close()

f1 = open('hall1.txt', 'r', encoding='utf-8')
content_list1 = [i for i in f1 if 'mag' in i]
f1.close()

# 创建一个excel
workbook = xlsxwriter.Workbook("hall.xlsx")
# 单元格内容居中
contents = workbook.add_format({'align': 'center'})

# 创建一个sheet, 默认 Sheet1
worksheet = workbook.add_worksheet()
# 可以起名字
# worksheet = workbook.add_worksheet("hall")

# 自定义样式，加粗
# bold = workbook.add_format({'bold': 1})
headings = ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)']

# --------1、准备数据并写入excel---------------
# 向excel中写入数据，建立图标时要用到
# 第一行 写 抬头
worksheet.write_row('A1', headings)
# 写入正式数据
line = 1
for j in content_list0:
    # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
    line_list = [i for i in (j.strip(',').split(' ')) if i != '']
    # float, 将其内容转换为float,一定要记得转换为数字,否则后续画图时,
    # excel本身会将其识别为文本,无法作为数字解析出来导致无法画出正确的图
    worksheet.write(line, 0, float(line_list[1].strip(',')), contents)
    worksheet.write(line, 1, float(line_list[3].strip(',')), contents)
    worksheet.write(line, 2, float(line_list[4].strip(',')), contents)
    worksheet.write(line, 3, float(line_list[5].strip(',')), contents)
    line += 1

# 画折线图 0
line_base = 1
chart_line0 = workbook.add_chart({'type': 'line'})

# 设置图表的title 和 x，y轴信息
chart_line0.set_title({'name': 'Pos-Hall0'})
chart_line0.set_x_axis({'name': 'Pos: mm'})
chart_line0.set_y_axis({'name': 'Magnetic: uT'})

chart_line0.add_series({
    'name': '=Sheet1!$B$1',
    'line': {'color': 'red'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 1, line, 1], # 第2行第2列开始, 到 Line 行 第2列结束
    })
chart_line0.add_series({
    'name': '=Sheet1!$C$1',
    'line': {'color': 'blue'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 2, line, 2], # 第2行第3列开始, 到 Line 行 第3列结束
    })
chart_line0.add_series({
    'name': '=Sheet1!$D$1',
    'line': {'color': 'green'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 3, line, 3], # 第2行第4列开始, 到 Line 行 第4列结束
    })
# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('F1', chart_line0, {'x_offset': 25, 'y_offset': 10})

#===============================================================================
line += 2
worksheet.write_row(line, 0, headings)
#worksheet.write_row(line, 0, ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)'])

line += 1
line_base = line
for j in content_list1:
    # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
    line_list = [i for i in (j.strip(',').split(' ')) if i != '']
    # float, 将其内容转换为float,一定要记得转换为数字,否则后续画图时,
    # excel本身会将其识别为文本,无法作为数字解析出来导致无法画出正确的图
    worksheet.write(line, 0, float(line_list[1].strip(',')), contents)
    worksheet.write(line, 1, float(line_list[3].strip(',')), contents)
    worksheet.write(line, 2, float(line_list[4].strip(',')), contents)
    worksheet.write(line, 3, float(line_list[5].strip(',')), contents)
    line += 1

# 画折线图 1
chart_line1 = workbook.add_chart({'type': 'line'})

# 设置图表的title 和 x，y轴信息
chart_line1.set_title({'name': 'Pos-Hall1'})
chart_line1.set_x_axis({'name': 'Pos: mm'})
chart_line1.set_y_axis({'name': 'Magnetic: uT'})

# 设置图表的风格
# chart_line.set_style(2)
chart_line1.add_series({
    'name': '=Sheet1!$B$1',
    'line': {'color': 'red'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 1, line, 1], # 第2行第2列开始, 到 Line 行 第2列结束
    })
chart_line1.add_series({
    'name': '=Sheet1!$C$1',
    'line': {'color': 'blue'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 2, line, 2], # 第2行第3列开始, 到 Line 行 第3列结束
    })
chart_line1.add_series({
    'name': '=Sheet1!$D$1',
    'line': {'color': 'green'},
    'marker': {'type': 'diamond', 'size': 7},
    'categories': ['Sheet1', line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
    'values': ['Sheet1', line_base, 3, line, 3], # 第2行第4列开始, 到 Line 行 第4列结束
    })

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('N1', chart_line1, {'x_offset': 25, 'y_offset': 10})


workbook.close() 

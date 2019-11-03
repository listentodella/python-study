# -*- coding:utf-8 -*-

import xlsxwriter
#import re

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
# worksheet.write_row(0, 0, ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)'])
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

line += 2
worksheet.write_row(line, 0, headings)
#worksheet.write_row(line, 0, ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)'])

line += 1
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


'''
line=1
for j in content_list:
    line_list = [i for i in (j.split(' ')) if i != '']
    number_list = re.findall(r'[^\d](-?\d+)', line_list[-1])
    worksheet.write(line, 0, line_list[1], contents)
    worksheet.write(line, 1, line_list[3], contents)
    worksheet.write(line, 2, line_list[4], contents)
    worksheet.write(line, 3, line_list[5], contents)
    line += 1
'''


# 画折线图 0
chart_line0 = workbook.add_chart({'type': 'line'})

# 设置图表的title 和 x，y轴信息
chart_line0.set_title({'name': 'Pos-Hall0'})
chart_line0.set_x_axis({'name': 'Pos: mm'})
chart_line0.set_y_axis({'name': 'Magnetic: uT'})

# 设置图表的风格
# chart_line.set_style(2)

# 配置第1个系列数据
chart_line0.add_series({
    # 这里的Sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$8',
    'values':   '=Sheet1!$B$2:$B$8',
    'marker': {'type': 'diamond', 'size': 7},
    'line': {'color': 'red'},

})

# 配置第2个系列数据
chart_line0.add_series({
    'name': '=Sheet1!$C$1',
    'categories':  '=Sheet1!$A$2:$A$8',
    'marker': {'type': 'diamond', 'size': 7},
    'values':   '=Sheet1!$C$2:$C$8',
    'line': {'color': 'blue'},
})

# 配置第2个系列数据(用了另一种语法)
# chart_line.add_series({
#     'name': ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values': ['Sheet1', 1, 2, 6, 2],
#     'line': {'color': 'yellow'},
# })

# 配置第3个系列数据
chart_line0.add_series({
    'name': '=Sheet1!$D$1',
    'categories':  '=Sheet1!$A$2:$A$8',
    'marker': {'type': 'diamond', 'size': 7},
    'values':   '=Sheet1!$D$2:$D$8',
    'line': {'color': 'green'},
})

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('F1', chart_line0, {'x_offset': 25, 'y_offset': 10})

#===============================================================================

# 画折线图 1
chart_line1 = workbook.add_chart({'type': 'line'})

# 设置图表的title 和 x，y轴信息
chart_line1.set_title({'name': 'Pos-Hall1'})
chart_line1.set_x_axis({'name': 'Pos: mm'})
chart_line1.set_y_axis({'name': 'Magnetic: uT'})

# 设置图表的风格
# chart_line.set_style(2)

# 配置第1个系列数据
chart_line1.add_series({
    # 这里的Sheet1是默认的值，因为我们在新建sheet时没有指定sheet名
    # 如果我们新建sheet时设置了sheet名，这里就要设置成相应的值
    'name': '=Sheet1!$B$1',
    'categories': '=Sheet1!$A$2:$A$8',
    'values':   '=Sheet1!$B$2:$B$8',
    'marker': {'type': 'diamond', 'size': 7},
    'line': {'color': 'red'},
})

# 配置第2个系列数据
chart_line1.add_series({
    'name': '=Sheet1!$C$1',
    'categories':  '=Sheet1!$A$2:$A$8',
    'marker': {'type': 'diamond', 'size': 7},
    'values':   '=Sheet1!$C$2:$C$8',
    'line': {'color': 'blue'},
})

# 配置第2个系列数据(用了另一种语法)
# chart_line.add_series({
#     'name': ['Sheet1', 0, 2],
#     'categories': ['Sheet1', 1, 0, 6, 0],
#     'values': ['Sheet1', 1, 2, 6, 2],
#     'line': {'color': 'yellow'},
# })

# 配置第3个系列数据
chart_line1.add_series({
    'name': '=Sheet1!$D$1',
    'categories':  '=Sheet1!$A$2:$A$8',
    'marker': {'type': 'diamond', 'size': 7},
    'values':   '=Sheet1!$D$2:$D$8',
    'line': {'color': 'green'},
})

# 把图表插入到worksheet并设置偏移
worksheet.insert_chart('F10', chart_line1, {'x_offset': 25, 'y_offset': 10})




workbook.close() 

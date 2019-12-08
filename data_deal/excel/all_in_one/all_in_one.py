import os
import xlsxwriter

CONST_DIFF=(500)
CONST_UP_X_MIN=(8000)
CONST_UP_X_MAX=(15000)
CONST_UP_Y_MIN=(3800)
CONST_UP_Y_MAX=(10000)

CONST_DOWN_X_MIN=(5000)
CONST_DOWN_X_MAX=(8000)
CONST_DOWN_Y_MIN=(-5200)
CONST_DOWN_Y_MAX=(-2000)

# 递归检索
def listdir(path, list_name):
    for file in os.listdir(path):
            file_path = os.path.join(path, file)
            if os.path.isdir(file_path):
                listdir(file_path, list_name)
            elif os.path.splitext(file_path)[1]=='.txt':
                list_name.append(file_path)


def walkFile(file):
# 创建一个excel
    #workbook = xlsxwriter.Workbook("all_in_one_vba.xlsx")
    workbook = xlsxwriter.Workbook("all_in_one_vba.xlsm")
    # 条件格式 conditional format
    format_pass = workbook.add_format({'bg_color':   '#C6EFCE', 'font_color': '#006100'})
    format_warning = workbook.add_format({'bg_color':   'red', 'font_color': 'black'})
    format_highlight = workbook.add_format({'bg_color': 'orange', 'font_color': 'black', 'bold': 5})
# 单元格内容居中
    format_contents = workbook.add_format({'align': 'center'})
# 创建目录索引
    worksheet = workbook.add_worksheet("目录")
    workbook.add_vba_project('./vbaProject.bin')
    workbook.define_name('shname', '=MID(GET.WORKBOOK(1),FIND("]",GET.WORKBOOK(1))+1,99)&T(NOW())')
    # 注意 转义符 \
    #worksheet.write_formula('A1', '=IFERROR(HYPERLINK("#'"&INDEX(shname,ROW(A1))&"'!A1",INDEX(shname,ROW(A1))),"")')
    worksheet.write('A1', '=IFERROR(HYPERLINK("#\'"&INDEX(shname,ROW(A1))&"\'!A1",INDEX(shname,ROW(A1))),"")')
# 创建sheets
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        # for f in files:
        #     print(os.path.join(root, f))

        # 遍历所有的文件夹
        for d in dirs:
            #print(os.path.join(root, d))
            # 创建一个sheet, 默认 Sheet1
            if d == 'pos_hall':
                print("解析完本级目录!")
                break
            worksheet = workbook.add_worksheet(d)
            print("add worksheet start ========================:", d)
            # 自定义样式，加粗
            # bold = workbook.add_format({'bold': 1})
            headings = ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)', '', 'Δx(uT)', 'Δy(uT)', 'Δz(uT)']
            #for f in files:
            for dir_files in os.walk(d):
                #print(os.path.join(root, f))
                print("dir_files:",dir_files)
                file_list = []
                #print("file_list =",file_list)
                listdir(d, file_list)
                print("file_list =",file_list)
                for i in range(0, len(file_list)):
                    #file_path = os.path.join(d, file_list[i])
                    file_path = file_list[i]
                    #print("file_path", file_path)
                    if os.path.exists(file_path) and file_path.endswith('hall_calibration_data_0.txt'):
                        print("open file:", file_path)
                        f0 = open(file_path, 'r', encoding='utf-8')
                        content_list0 = [i for i in f0 if 'mag' in i]
                        f0.close()
                    if os.path.exists(file_path) and file_path.endswith('hall_calibration_data_1.txt'):
                        print("open file:", file_path)
                        f1 = open(file_path, 'r', encoding='utf-8')
                        content_list1 = [i for i in f1 if 'mag' in i]
                        f1.close()
                    if os.path.exists(file_path) and file_path.endswith('hall_diff_data_0.txt'):
                        print("open file:", file_path)
                        f2 = open(file_path, 'r', encoding='utf-8')
                        content_list2 = [i for i in f2 if 'diff' in i]
                        f2.close()
                    if os.path.exists(file_path) and file_path.endswith('hall_diff_data_1.txt'):
                        print("open file:", file_path)
                        f3 = open(file_path, 'r', encoding='utf-8')
                        content_list3 = [i for i in f3 if 'diff' in i]
                        f3.close()
            # --------1、准备数据并写入excel---------------
            # 向excel中写入数据，建立图标时要用到
            # 第一行 写 抬头
            worksheet.write_row('A1', headings)
            # 写入正式数据
            line = 1
            line_diff = line + 1
            for j in content_list0:
                # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
                line_list = [i for i in (j.strip(',').split(' ')) if i != '']
                # float, 将其内容转换为float,一定要记得转换为数字,否则后续画图时,
                # excel本身会将其识别为文本,无法作为数字解析出来导致无法画出正确的图
                worksheet.write(line, 0, float(line_list[1].strip(',')), format_contents)
                worksheet.write(line, 1, float(line_list[3].strip(',')), format_contents)
                worksheet.write(line, 2, float(line_list[4].strip(',')), format_contents)
                worksheet.write(line, 3, float(line_list[5].strip(',')), format_contents)
                line += 1

            for diff_j in content_list2:
                # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
                diff_list = [i for i in (diff_j.strip(',').split(' ')) if i != '']
                #worksheet.write(line_diff, 5, float(diff_list[1].strip(',')), format_contents)
                worksheet.write(line_diff, 5, float(diff_list[3].strip(',')), format_contents)
                worksheet.write(line_diff, 6, float(diff_list[4].strip(',')), format_contents)
                worksheet.write(line_diff, 7, float(diff_list[5].strip(',')), format_contents)
                line_diff += 1


            # 画折线图 0
            line_base = 1
            chart_line0 = workbook.add_chart({'type': 'line'})

            # 设置图表的title 和 x，y轴信息
            chart_line0.set_title({'name': 'Pos-Hall0'})
            chart_line0.set_x_axis({'name': 'Pos: mm'})
            chart_line0.set_y_axis({'name': 'Magnetic: uT'})
            chart_line0.set_size({'x_scale': 1.25})

            chart_line0.add_series({
                #'name': '=Sheet1!$B$1',
                'name': 'x(uT)',
                'line': {'color': 'red'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'red'}, 'fill': {'color': 'red'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 1, line, 1], # 第2行第2列开始, 到 Line 行 第2列结束
                })
            chart_line0.add_series({
                #'name': '=Sheet1!$C$1',
                'name': 'y(uT)',
                'line': {'color': 'green'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'green'}, 'fill': {'color': 'green'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 2, line, 2], # 第2行第3列开始, 到 Line 行 第3列结束
                })
            chart_line0.add_series({
                #'name': '=Sheet1!$D$1',
                'name': 'z(uT)',
                'line': {'color': 'purple'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'purple'}, 'fill': {'color': 'purple'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 3, line, 3], # 第2行第4列开始, 到 Line 行 第4列结束
                })
            # 把图表插入到worksheet并设置偏移
            worksheet.insert_chart('J1', chart_line0, {'x_offset': 25, 'y_offset': 10})

            #===============================================================================
            line += 2
            worksheet.write_row(line, 0, headings)
            #worksheet.write_row(line, 0, ['pos(mm)', 'x(uT)', 'y(uT)', 'z(uT)'])

            line += 1
            line_base = line
            line_diff = line + 1
            for j in content_list1:
                # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
                line_list = [i for i in (j.strip(',').split(' ')) if i != '']
                # float, 将其内容转换为float,一定要记得转换为数字,否则后续画图时,
                # excel本身会将其识别为文本,无法作为数字解析出来导致无法画出正确的图
                worksheet.write(line, 0, float(line_list[1].strip(',')), format_contents)
                worksheet.write(line, 1, float(line_list[3].strip(',')), format_contents)
                worksheet.write(line, 2, float(line_list[4].strip(',')), format_contents)
                worksheet.write(line, 3, float(line_list[5].strip(',')), format_contents)
                line += 1

            for diff_j in content_list3:
                # split(xxx):以 xxx 分割; strip(yyy):去除字段里的yyy
                diff_list = [i for i in (diff_j.strip(',').split(' ')) if i != '']
                #worksheet.write(line_diff, 5, float(diff_list[1].strip(',')), format_contents)
                worksheet.write(line_diff, 5, float(diff_list[3].strip(',')), format_contents)
                worksheet.write(line_diff, 6, float(diff_list[4].strip(',')), format_contents)
                worksheet.write(line_diff, 7, float(diff_list[5].strip(',')), format_contents)
                line_diff += 1

            # 画折线图 1
            chart_line1 = workbook.add_chart({'type': 'line'})

            # 设置图表的title 和 x，y轴信息
            chart_line1.set_title({'name': 'Pos-Hall1'})
            chart_line1.set_x_axis({'name': 'Pos: mm'})
            chart_line1.set_y_axis({'name': 'Magnetic: uT'})
            chart_line1.set_size({'x_scale': 1.25})

            # 设置图表的风格
            # chart_line.set_style(2)
            chart_line1.add_series({
                #'name': '=Sheet1!$B$1',
                'name': 'x(uT)',
                'line': {'color': 'red'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'red'}, 'fill': {'color': 'red'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 1, line, 1], # 第2行第2列开始, 到 Line 行 第2列结束
                })
            chart_line1.add_series({
                #'name': '=Sheet1!$C$1',
                'name': 'y(uT)',
                'line': {'color': 'green'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'green'}, 'fill': {'color': 'green'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 2, line, 2], # 第2行第3列开始, 到 Line 行 第3列结束
                })
            chart_line1.add_series({
                #'name': '=Sheet1!$D$1',
                'name': 'z(uT)',
                'line': {'color': 'purple'},
                'marker': {'type': 'circle', 'size': 4, 'border': {'color': 'purple'}, 'fill': {'color': 'purple'}},
                'categories': [d, line_base, 0, line, 0], # 第2行第1列开始, 到 Line 行 第1列 结束
                'values': [d, line_base, 3, line, 3], # 第2行第4列开始, 到 Line 行 第4列结束
                })

            # 把图表插入到worksheet并设置偏移
            worksheet.insert_chart('J16', chart_line1, {'x_offset': 25, 'y_offset': 10})
            # 设置返回目录按钮
            worksheet.write('E1', '=HYPERLINK("#目录!A1","前往目录")', format_highlight)

            # 条件格式 conditional format
            # format_pass = workbook.add_format({'bg_color':   '#C6EFCE', 'font_color': '#006100'})
            # format_warning = workbook.add_format({'bg_color':   'red', 'font_color': 'black'})
            # diff 满足区域
            worksheet.conditional_format('F1:H46', {'type': 'cell', 'criteria': '>=', 'value': CONST_DIFF, 'format': format_pass})
            # up init fail 值
            worksheet.conditional_format('B2:B2', {'type': 'cell', 'criteria': '<=', 'value': CONST_UP_X_MIN, 'format': format_warning})
            worksheet.conditional_format('B2:B2', {'type': 'cell', 'criteria': '>=', 'value': CONST_UP_X_MAX, 'format': format_warning})
            worksheet.conditional_format('C2:C2', {'type': 'cell', 'criteria': '<=', 'value': CONST_UP_Y_MIN, 'format': format_warning})
            worksheet.conditional_format('C2:C2', {'type': 'cell', 'criteria': '>=', 'value': CONST_UP_Y_MAX, 'format': format_warning})
            # down init fail 值
            worksheet.conditional_format('B26:B26', {'type': 'cell', 'criteria': '<=', 'value': CONST_DOWN_X_MIN, 'format': format_warning})
            worksheet.conditional_format('B26:B26', {'type': 'cell', 'criteria': '>=', 'value': CONST_DOWN_X_MAX, 'format': format_warning})
            worksheet.conditional_format('C26:C26', {'type': 'cell', 'criteria': '<=', 'value': CONST_DOWN_Y_MIN, 'format': format_warning})
            worksheet.conditional_format('C26:C26', {'type': 'cell', 'criteria': '>=', 'value': CONST_DOWN_Y_MAX, 'format': format_warning})
            print("add worksheet end    =======================:", d)
            print()
            print()
            print()
    print("生成目录完毕")

    workbook.close()

def main():
    walkFile(".")
    print("检索完成")


if __name__ == '__main__':
    main()

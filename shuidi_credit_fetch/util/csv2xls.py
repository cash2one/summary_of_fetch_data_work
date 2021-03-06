# -*- coding: utf-8 -*-

import os
import csv
import xlsxwriter


def change_csv_format(srcName, targetName, sheetName):
    tempDir = os.path.abspath('../')
    csv_file_name = os.path.join(tempDir, 'data', srcName)
    xls_file_name = os.path.join(tempDir, 'real_data', targetName)
    with open(csv_file_name, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        data = [row for row in reader]
        titles = data[0]
        # 将csv文件中的内容写入xls文件中
        workbook = xlsxwriter.Workbook(xls_file_name)
        worksheet = workbook.add_worksheet(name=sheetName)
        # Add a bold format to highlight cell text.
        bold = workbook.add_format({'bold': 1})
        for i in range(12):
            c = chr(65 + i)
            worksheet.set_column(c + ':' + c, width=20)
        # 写入标题
        for i in range(len(titles)):
            worksheet.write(0, i, titles[i], bold)
        # 写入代理人信息
        for i in range(1, len(data)):
            _data = data[i]
            for j in range(len(_data)):
                worksheet.write(i, j, _data[j])

        workbook.close()


'''
if __name__ == '__main__':
    # change_csv_format('company.csv', '四川泸州市企业信息.xls', '四川省_泸州市企业信息')
'''

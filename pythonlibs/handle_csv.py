# -*- coding: UTF-8 -*- 


"""
python: 3.6.0
author: Saitoler

#Python 操作CSV文件
#   - 读取：
#   - 写入：


1. 基本功能实现了 但是有点挫，待排序文件是写死了的路径和名称，每次都要手动修改很麻烦
2. add、del 文件的排序使用这份代码可以实现，但 mod 文件还需要修改 lambda 函数，复用性不强

"""


#导入csv模块
import csv

#定义待读取文件及待写入结果的文件
in_csv_file = "C:\\Users\\Saitoler\\Desktop\\apk\\del_compare_result.csv"
out_csv_file = "C:\\Users\\Saitoler\\Desktop\\apk\\del_compare_result_sorted.csv"


#读取csv文件
csv_file = csv.reader(open(in_csv_file, 'r'), delimiter=',')

all_data = []
for items in csv_file:  #将流中的数据分别写入all_data list里面，单独的每个item都是一个list
    all_data.append(items)

#保存csv文件中的标题栏并从待排序list中删除标题
title_list = all_data[0]
all_data.pop(0)

"""
使用内置sorted函数对所有数据进行排序，排序完将标题插入首位
这里的1指的是待排序数据是csv的第几列，列由0开始
这份代码适用于add、del两个文件，若要对mod文件排序，将此处的1改为3
"""
sorted_data = sorted(all_data, key = lambda x: int(x[1]))
sorted_data.insert(0, title_list)

#写入csv文件中
# newline='' 是为了解决写一行后有空行的问题

with open(out_csv_file, "w", newline = '') as f:
    file_writer = csv.writer(f, delimiter=',')
    for row in sorted_data:
        file_writer.writerow(row)


f.close()
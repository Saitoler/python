# -*- coding: utf-8 -*-

import csv
import datetime

"""
创建 csv 文件， 以当日时间戳自动命名

"""

def createCsv():
    filename = "{}.csv".format(datetime.datetime.now().strftime("%Y%m%d"))
    
    head = ["Time", "CPU", "MEM(MB)", "handles"]
    with open(filename, "w+", newline='') as f:
        csvFile = csv.writer(f)
        csvFile.writerow(head)


# if __name__ == "__main__":
#     cpufile = createCsv()

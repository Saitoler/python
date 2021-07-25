# -*- coding: utf-8 -*-

import time, datetime
import proInfoGet
import FileOperator
import csv, os


if __name__ == "__main__":

    # 待采集的程序名称
    processName = "winlogon.exe"


    # 采集间隔：10分钟
    sleepTime = 600

    while True:
        timeStamp = datetime.datetime.now()

        ymd = timeStamp.strftime("%Y%m%d")
        hms = timeStamp.strftime("%H:%M:%S")
        
        cpu = float(proInfoGet.getCpuPercentByName(processName))
        mem = float(proInfoGet.getMemSizeByName(processName))
        handle = proInfoGet.getHandlesByName(processName)

        if cpu > 15 or mem > 20 or handle > 700:
            notification.emailNotify("nac_agent.exe 当前资源占用为：CPU-%{}, MEM-{}MB, handles-{}".format(cpu, mem, handle))

        if not os.path.exists("{}.csv".format(ymd)):
            csvfile = FileOperator.createCsv()

        with open("{}.csv".format(ymd), "a+", newline='') as f:
            csvFile = csv.writer(f)
            csvFile.writerow([hms, cpu, mem, handle])

        time.sleep(sleepTime)
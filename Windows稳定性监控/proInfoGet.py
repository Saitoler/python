# -*- coding: utf-8 -*-

import psutil

"""
使用 psutil, 获取进程相关信息：
	* - 占用的 内存大小：  MB-两位小数
	* - 占用的 CPU百分比： % -两位小数
	* - 进程的 pid 
	* - 进程的 句柄数
"""


# 通过进程名，获取进程的 pids 信息
def getPidByName(processName):
	# 仅支持单进程的，暂不处理多进程的程序
	for process in psutil.process_iter(['name', 'pid']):
		if process.info['name'] == processName:
			return process.info['pid']


# 通过进程名，获取进程占用内存的信息
# 单位： MB
def getMemSizeByName(processName):
	meminfo = psutil.Process(getPidByName(processName)).memory_info()
	return "%.2f" % (meminfo.rss /1024/1024)


# 通过进程名，获取进程占用 CPU 百分比
# 单位： %， 结果取两位小数，四舍五入
def getCpuPercentByName(processName):
	cpuPercent = psutil.Process(getPidByName(processName)).cpu_percent()
	return "%.2f" % cpuPercent


# 通过进程名，获取进程打开的句柄个数
def getHandlesByName(processName):
	return psutil.Process(getPidByName(processName)).num_handles()



# 测试代码

# if __name__ == "__main__":
# 	processName = "winlogon.exe"
# 	print("{}'s pid is {}".format(processName, getPidByName(processName)))
# 	print("{}'s memoryUsage is {} MB ".format(processName, getMemSizeByName(processName)))
# 	print("{}'s cpuPercent is %{}".format(processName, getCpuPercentByName(processName)))
# 	print("{}'s handleNums is {}".format(processName, getHandlesByName(processName)))
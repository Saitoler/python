# -*- coding: utf-8 -*-

import configparser
import os
import shutil
import requests
import psutil
from multiprocessing import Pool



"""

************* 指标对比自动化 ***********
-@ 固化 1台 ATP： 10.130.17.115
-@ 固化 2台 低端设备：
-@ 固化 2台 中端设备：
-@ 高端平台的 指标对比自动化暂不加入，固化资源要求太高

"""

# atp 声明
atpIP = "10.130.17.115"

# 声明全局变量
# atp 的登录，拉起和停止需要有全局的 session 来操作，而我们固化了一台 ATP，这里声明成全局即可

# 登录 ATP 的账号密码
loginJson = {"name":"admin", "password":"admin", "opr":"login"}

# 登陆页面、atp 首页
loginPage = "http://" + atpIP
homePage = "http://{0}/src/home.html".format(atpIP)

# 操作测试集的请求地址：
testLink = "http://{}/src/scene_execute.php".format(atpIP)


# 声明全局 session
sess = requests.session()

# 登录 ATP 
def loginATP():
    sess.get(loginPage)
    sess.post(homePage, loginJson)

# 拉起测试集， 传入 ATP 上的 caseID, F12可以获取
def startATP(caseID):
    startJson = {"opr":"retry", "id":caseID}
    sess.post(testLink, startJson)


# 停止测试集
def stopATP(caseID):
    stopJson = {"opr":"stop", "id":caseID}
    sess.post(testLink, stopJson)


# 判断进程是否在运行, 存在则返回该进程的 pid 号
def proc_exist(procName):
    pids = psutil.pids()
    for pid in pids:
        if psutil.Process(pid).name() == procName:
            return pid


# 修改指标数据采集自动化的配置文件
"""
 @ 修改配置文件
  - @filepath: string 类型，传入文件的绝对路径
  - @ipaddr: string 类型，传入待采集数据的设备 Ip
  - @bak_pwd: string 类型，传入待采集数据的设备的后台密码
  - @web_pwd: string 类型，传入待采集数据的设备的网关登录密码

"""
def modifyConfig(filepath, ipaddr, bak_pwd, web_pwd):
    cf = configparser.ConfigParser()
    file = cf.read(filepath)
    cf.set('AC', 'ip_addr', ipaddr)
    cf.set('AC', 'bak_pwd', bak_pwd)
    cf.set('AC', 'web_pwd', web_pwd)

    with open(filepath, "w+") as f:
        cf.write(f)


# 拉起指标采集自动化脚本的方法，通过 os.system拉起
# start 关键字的声明， 可以使得 os.system 进行并行调用
# 如果不声明 start 关键字，则只能串行运行

def collData(scriptPath):
    os.system("start /B ruby {}".format(scriptPath))


# 并行数据采集，每次采集两台设备，使用 Pool 进行并发
def multiColl():
    pro = Pool(2)
    pro.apply_async(collData("D:/testdir/collect_code/run.rb"))
    pro.apply_async(collData("D:/testdir/collect_code_bak/run.rb"))

    pro.close()
    # 内部调用的 os.system() 会托管，这里判断下 os.system() 拉起的 ruby 进程是否
    # 在运行， 都退出后再执行 join() 操作
    if not isinstance(proc_exist("ruby.exe"), int):
        pro.join()


# 备份测试报告,备份后的测试报告名称为: name_device_ip_指标对比测试报告.xlsx
# 如 低端_1.1.1.1_指标对比测试报告.xlsx，统一保存在 "D:/testdir/reportbak/"

def backupReport(name, device_ip1, device_ip2):
    report1 = "D:/testdir/collect_code/report/指标测试报告.xlsx"
    report2 = "D:/testdir/collect_code_bak/report/指标测试报告.xlsx"

    bakdir = "D:/testdir/reportbak/"

    shutil.copy(report1, bakdir)
    os.rename(bakdir+"指标测试报告.xlsx", bakdir+"{}_{}_指标对比测试报告.xlsx".format(device_ip1, name))
    shutil.copy(report2, bakdir)
    os.rename(bakdir+"指标测试报告.xlsx", bakdir+"{}_{}_指标对比测试报告.xlsx".format(device_ip2, name))



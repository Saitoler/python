# -*- coding:utf-8 -*-

import AutoUtils
import time

# 指标采集自动化配置文件路径，全局声明
configFilePath1 = "D:/testdir/collect_code/config.ini"
configFilePath2 = "D:/testdir/collect_code_bak/config.ini"


AutoUtils.loginATP()


"""
低端平台

# caseID:  case60ab9cf539f99
"""

# 低端平台指标对比自动化
acIP1 = "10.130.17.201"
acIP2 = "10.130.17.202"
caseIDLow = "case60ab9cf539f99"

AutoUtils.startATP(caseIDLow)
time.sleep(900)


AutoUtils.modifyConfig(configFilePath1, acIP1, "1", "Perfor@test")
AutoUtils.modifyConfig(configFilePath2, acIP2, "1", "Perfor@test")

AutoUtils.multiColl()
AutoUtils.backupReport("低端", acIP1, acIP2)

AutoUtils.stopATP(caseIDLow)


"""
中端平台

caseID:  case60af3fd13f026
"""

# 中端平台指标对比自动化
acIP3 = "10.130.17.89"
acIP4 = "10.130.17.88" 
caseIDMedium = "case60af3fd13f026"

AutoUtils.startATP(caseIDMedium)
time.sleep(60)


AutoUtils.modifyConfig(configFilePath1, acIP3, "1", "Perfor@test")
AutoUtils.modifyConfig(configFilePath2, acIP4, "1", "Perfor@test")

AutoUtils.multiColl()
AutoUtils.backupReport("中端", acIP3, acIP4)

AutoUtils.stopATP(caseIDMedium)


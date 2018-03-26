# encoding:utf-8

import os,time
from autoitpy import WinMFCDriver
driver = WinMFCDriver()
# 打开应用， 如果不是管理员权限运行，那就手动运行一下吧 
# os.popen(r'C:\f_disk\BaiduNetdiskDownload\npp_7.5.6_Installer.exe')
# 激活应用
driver.invoke("WinActivate","Installer Language")

# 下拉框控件，选择语言
driver.invoke("ControlCommand","Installer","","[ID:1002;class:ComboBox]","SelectString","English")
time.sleep(0.5)
driver.invoke("ControlCommand","Installer","","[ID:1002;class:ComboBox]","SelectString",u"中文(简体)")

# Button控件,点击操作
driver.invoke("ControlClick","Installer Language","","OK")
time.sleep(0.5)
driver.invoke("ControlClick","Notepad++","",u"下一步(&N) >")
time.sleep(0.5)
driver.invoke("ControlClick","Notepad++","",u"我接受(&I)")
time.sleep(0.5)
driver.invoke("ControlClick","Notepad++","","[ID:1019;class:Button]")

# 文本控件，输入操作
driver.invoke("ControlSend","Notepad++","","[ID:1019;class:Button]","{END}+{HOME}")
time.sleep(1)
driver.invoke("ControlSend","Notepad++","","[ID:1019;class:Button]",ur"d:\hello input")
time.sleep(0.5)
driver.invoke("ControlClick","Notepad++","",u"下一步(&N) >")
driver.invoke("ControlClick","Notepad++","",u"取消(&C)")
time.sleep(0.5)
driver.invoke("ControlClick","Notepad++","","[ID:6]")
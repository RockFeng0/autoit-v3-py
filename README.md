# 痛点（创建这个工程的目的）

1. 在软件自动化的过程中，常常遇到一些windows弹出框，上传文件等，常用的解决方案如AutoItv3，该项目使用Python 简单封装了一下 autoitv3,用于Windows MFC UI的自动化操作和测试。
2. 但它**仅仅适用于 Microsoft MFC技术的window窗口，而对于Microsoft WPF技术开发的window窗口无能为力**
3. 如果您有需求完成WPF和MFC窗口自动化的操作和验证，请点击[MUIA项目](https://github.com/RockFeng0/muiapy)


* * *
# 安装， windows安装,仅Windows系统

```
# 安装和时候用， 注意：使用管理员权限，运行cmd
C:\autoit-v3-py> python setup.py install
C:\autoit-v3-py> python
>>> from autoitpy import WinMFCDriver
>>> driver = WinMFCDriver()
```
> 关于报错如： ImportError: No module named win32com.client
下载相应版本的[pywin32](https://github.com/mhammond/pywin32/releases)并安装

* * *
# Windows MFC控件识别
> tools目录下，有32位和64位，控件识别工具，下载下来，双击运行，拖动 Finder Tools到要识别的控件,
在显示的信息中，标准的用于操作控件的Control如下:
- Control ID 
- ClassNameNN 
- Text

> 高级的识别，格式:  [属性:值; 属性:值], 比如:
- [ID:1]
- [CLASS:Button; INSTANCE:1]


* * *
# 简单的使用实例
安装notepad++的示例,如:

```
import os,time
from autoitpy import WinMFCDriver
driver = WinMFCDriver()
# 打开应用， 如果不是管理员权限运行，那就手动用管理员权限运行一下吧 
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
```

- 注意： 如果您不是管理员用户，需要使用管理员权限运行应用，并且使用管理员权限运行命令行cmd等.
- 执行的效果，如下图

![](https://github.com/RockFeng0/autoit-v3-py/raw/master/example/mfc_auto_example.gif)
 

* * *
# API参考文档

- 详细的API，请参见 [autoit官网](https://www.autoitscript.com/site/autoit/)
- 另外，离线的API文档，可以参见，项目路径下的 **doc/AutoItX.chm**










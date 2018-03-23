# -*- encoding: utf-8 -*-
'''
Current module: setup

Rough version history:
v1.0    Original version to use

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      setup,v 1.0 2015年5月13日
    FROM:   2015年5月13日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib
import ctypes,platform,os,sys

is_installing = False
if len(sys.argv)>=2 and sys.argv[1] == "install":
    is_installing = True
    
# 需要管理员 身份运行
if is_installing and ctypes.windll.shell32.IsUserAnAdmin() == 0:
    raise Exception("Sorry.\n\tPermission denied.\n\tYou must run this with administrator power.")

setup(
        name = "autoitpy",
        version="1.0.0",
        packages = find_packages(),
        package_data = {"autoitpy" : ["AutoItX3.dll","AutoItX3_x64.dll"],},
		include_package_data = True,
        zip_safe = False,
        #install_requires = ['pywin32>=214',],

        description = "Windows MFC UI Automation",
        long_description = "Only for MFC UI automation.",
        author = "rock feng",
        author_email = "lkf20031988@163.com",

        license = "MIT",
        keywords = ("autoitpy_1.0.0", "egg"),
        platforms = ['windows'],        
        )

if is_installing:
    # C:\Python27\Lib\site-packages\autoitpy-1.0.0-py2.7.egg\autoitpy
    dll_32_dir = os.path.join(get_python_lib(),"autoitpy-1.0.0-py2.7.egg","autoitpy","AutoItX3.dll")
    dll_64_dir = os.path.join(get_python_lib(),"autoitpy-1.0.0-py2.7.egg","autoitpy","AutoItX3_x64.dll")
          
    (sys_bit, sys_name) = platform.architecture()
    if sys_bit == "32bit":
        os.popen("cmd /c regsvr32 /s %s" %dll_32_dir)
    elif sys_bit == "64bit":
        os.popen("cmd /c regsvr32 /s %s" %dll_64_dir)
    else:
        raise Exception("Can't register autoit dll.\nUnknow system %s %s") %(sys_name,sys_bit)
    print "Install %s autoitx3 dll success." %sys_bit

        
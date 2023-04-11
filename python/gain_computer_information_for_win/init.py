#!/user/bin/env python3
# -*- coding: utf-8 -*-
import wmi
import os
import socket
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from ui.untitled import Ui_MainWindow




class init(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(init, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.info)

    def info(self):
        try:
            name = self.lineEdit.text()
            w = wmi.WMI()

            # 获取电脑使用者信息
            for CS in w.Win32_ComputerSystem():
                # print(CS)
                print("电脑名称: %s" %CS.Caption)
                print("使用者: %s" %CS.UserName)
                print("制造商: %s" %CS.Manufacturer)
                print("系统信息: %s" %CS.SystemFamily)
                print("工作组: %s" %CS.Workgroup)
                print("机器型号: %s" %CS.model)

                self.log("电脑名称: %s" %CS.Caption, name)
                self.log("使用者: %s" %CS.UserName, name)
                self.log("制造商: %s" %CS.Manufacturer, name)
                self.log("系统信息: %s" %CS.SystemFamily, name)
                self.log("工作组: %s" %CS.Workgroup, name)
                self.log("机器型号: %s" %CS.model, name)
                # self.log("电脑名称: %s" %CS.Caption, name)

            # 获取操作系统信息
            for OS in w.Win32_OperatingSystem():
                # print(OS)
                print("操作系统: %s" %OS.Caption)
                print("系统位数: %s" %OS.OSArchitecture)
                print("注册人: %s" %OS.RegisteredUser)
                print("系统驱动: %s" %OS.SystemDevice)
                print("系统目录: %s" %OS.SystemDirectory)

                self.log("操作系统: %s" %OS.Caption, name)
                self.log("系统位数: %s" %OS.OSArchitecture, name)
                self.log("注册人: %s" %OS.RegisteredUser, name)
                self.log("系统驱动: %s" %OS.SystemDevice, name)
                self.log("系统目录: %s" %OS.SystemDirectory, name)

            # 获取电脑IP和MAC信息
            for address in w.Win32_NetworkAdapterConfiguration(ServiceName="e1dexpress"):
                # print(address)
                # print("IP地址: %s" % address.IPAddress[0])
                print("MAC地址: %s" % address.MACAddress)
                print("网络描述: %s" % address.Description)

                # self.log("IP地址: %s" % address.IPAddress[0], name)
                self.log("MAC地址: %s" % address.MACAddress, name)
                self.log("网络描述: %s" % address.Description, name)

            # 获取电脑CPU信息
            for processor in w.Win32_Processor():
                #print(processor)
                print("CPU型号: %s" % processor.Name.strip())
                print("CPU核数: %s" % processor.NumberOfCores)

                self.log("CPU型号: %s" % processor.Name.strip(), name)
                self.log("CPU核数: %s" % processor.NumberOfCores, name)

            # 获取BIOS信息
            for BIOS in w.Win32_BIOS():
                # print(BIOS)
                print("使用日期: %s" %BIOS.Description)
                print("主板型号: %s" %BIOS.SerialNumber)
                print("当前语言: %s" %BIOS.CurrentLanguage)

                self.log("使用日期: %s" %BIOS.Description, name)
                self.log("主板型号: %s" %BIOS.SerialNumber, name)
                self.log("当前语言: %s" %BIOS.CurrentLanguage, name)

            # 获取内存信息
            for memModule in w.Win32_PhysicalMemory():
                totalMemSize = int(memModule.Capacity)
                print("内存厂商: %s" %memModule.Manufacturer)
                print("内存型号: %s" %memModule.PartNumber)
                print("内存大小: %.2fGB" %(totalMemSize/1024**3))

                self.log("内存厂商: %s" %memModule.Manufacturer, name)
                self.log("内存型号: %s" %memModule.PartNumber, name)
                self.log("内存大小: %.2fGB" %(totalMemSize/1024**3), name)

            # 获取磁盘信息
            for disk in w.Win32_DiskDrive():
                diskSize = int(disk.size)
                print("磁盘名称: %s" %disk.Caption)
                print("硬盘型号: %s" %disk.Model)
                print("磁盘大小: %.2fGB" %(diskSize/1024**3))

                self.log("磁盘名称: %s" %disk.Caption, name)
                self.log("硬盘型号: %s" %disk.Model, name)
                self.log("磁盘大小: %.2fGB" %(diskSize/1024**3), name)

            # 获取显卡信息
            for xk in w.Win32_VideoController():
                print("显卡名称: %s" %xk.name)

                self.log("显卡名称: %s" %xk.name, name)

            # 获取计算机名称和IP
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            print("计算机名称: %s" %hostname)
            print("IP地址: %s" %ip)

            self.log("计算机名称: %s" %hostname, name)
            self.log("IP地址: %s" %ip, name)
            QMessageBox.about(self, "successful", "完成   ")
        except Exception as e:
            print(e)

    # 写文件
    def log(self, e, logname='log', mode='a'):
        txt = str(e) + "\n"
        path = os.path.split(os.path.realpath(sys.argv[0]))[0]
        log = str(path) + '\\' + logname + '.txt'
        with open(str(log), mode, encoding="utf-8") as f:
            f.write(txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    initMainWindow = init()
    initMainWindow.show()
    sys.exit(app.exec_())

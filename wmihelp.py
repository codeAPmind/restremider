# -*- coding: utf-8 -*-
import wmi


class Hardware:
    @staticmethod
    def get_cpu_sn():
        """
        获取CPU序列号
        :return: CPU序列号
        """
        c = wmi.WMI()
        for cpu in c.Win32_Processor():
            # print(cpu.ProcessorId.strip())
            return cpu.ProcessorId.strip()

    @staticmethod
    def get_baseboard_sn():
        """
        获取主板序列号
        :return: 主板序列号
        """
        c = wmi.WMI()
        for board_id in c.Win32_BaseBoard():
            # print(board_id.SerialNumber)
            return board_id.SerialNumber

    @staticmethod
    def get_bios_sn():
        """
        获取BIOS序列号
        :return: BIOS序列号
        """
        c = wmi.WMI()
        for bios_id in c.Win32_BIOS():
            # print(bios_id.SerialNumber.strip)
            return bios_id.SerialNumber.strip()

    @staticmethod
    def get_disk_sn():
        """
        获取硬盘序列号
        :return: 硬盘序列号列表
        """
        c = wmi.WMI()

        disk_sn_list = []
        for physical_disk in c.Win32_DiskDrive():
            # print(physical_disk.SerialNumber)
            # print(physical_disk.SerialNumber.replace(" ", ""))
            disk_sn_list.append(physical_disk.SerialNumber.replace(" ", ""))
        return disk_sn_list


def  get_bios():
    key = ""
    key += Hardware.get_cpu_sn()
    key += Hardware.get_baseboard_sn()
    key += Hardware.get_bios_sn()
    return key
        
if __name__ == "__main__":
    string_data = "Hello, World!"
    file_name = "binary_file.bin"

    print(get_bios())
    # # bios
    # key = ""
    # key += Hardware.get_cpu_sn()
    # key += Hardware.get_baseboard_sn()
    # key += Hardware.get_bios_sn()
        
    print("CPU序列号：{}".format(Hardware.get_cpu_sn()))
    print("主板序列号：{}".format(Hardware.get_baseboard_sn()))
    print("Bios序列号：{}".format(Hardware.get_bios_sn()))
    print("硬盘序列号：{}".format(Hardware.get_disk_sn()))
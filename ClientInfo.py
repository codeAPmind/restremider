
import json
import os
from key import view

def load_json(file_name):
	with open(file_name,'r',encoding='utf8')as fp:
		json_data = json.load(fp)
		return json_data


class Client:
    def __init__(self):
        super().__init__()
        # self.state('zoomed') 
        self.endTime = ""
        self.version = ""
        self.phoneNum = ""
        self.bios = ""
        self.init()


    def init(self):
        # if os.path.exists("EasyStock.dat"):
        #     # info = show("~keygen.dat") 
        #     # first_tuple = info[0]  # Get the first tuple
        #     infoValues = view('EasyStock.dat')[0][0]
        #     self.endTime = infoValues.time
        #     self.version = infoValues.version
        #     self.phoneNum = infoValues.mobile
        #     self.bios = infoValues.pc

        # else:
        #     # self.endTime = "info['endTime']"
        #     self.version = "1.0"
        #     self.phoneNum = "0123456789"
        #     self.bios = ""
            
        try:
            with open('WRBalance.json', 'r') as f:
                info = json.load(f)
                self.endTime = info['time']
                self.version = info['version']
                self.edition = info['edition']
                self.phoneNum = info["mobile"]
                self.bios = info["pc"]
                self.app = info["app"]
                self.MINUTESGAP = info["MINUTESGAP"]
                self.STOCKNUM = info["STOCKNUM"]
                self.STOCKNUM2 = info["STOCKNUM2"]
        except FileNotFoundError:
                self.endTime = 'time'
                self.version = 'version'
                self.edition ='edition'
                self.phoneNum ="mibile"
                self.bios = "pc"
                self.app = "app"
                self.MINUTESGAP = "MINUTESGAP"
                self.STOCKNUM = "STOCKNUM"
                self.STOCKNUM2 = "STOCKNUM2"
    
    # @staticmethod
    def get_endTime(self):

        return self.endTime

    # @staticmethod
    def get_version(self):

        return self.version
    
    # @staticmethod
    def get_bios(self):
        """
        获取CPU序列号
        :return: CPU序列号
        """
        return self.bios
    
    # @staticmethod
    def get_phoneNum(self):
        """
        获取CPU序列号
        :return: CPU序列号
        """
        return self.phoneNum
    
    
    
    
if __name__ == '__main__':
    a = Client()
    print(a.get_bios())
    print(a.get_endTime())
    import time
    print("time.time()",time.time())
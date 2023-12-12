from wmihelp import get_bios
from Encode import  sign,verify
from common import load_json
from tkinter import messagebox
from ConstValue import PHONENUM, ENDTIME,BIOSINFO

def check_tiemEX():
    datavalue = verify("license.json")
    if datavalue is not []:
        return True
    # else:
        # messagebox.showwarning("Time Passed", "Service has Passed")
    return False
    
def check_license():
    saveLicense = getLicenseEX()
    # global BIOSINFO
    print("save license",saveLicense)
    bios = PHONENUM + get_bios()
    license =  sign( ENDTIME ,BIOSINFO, "license.json",False)
    if  license  not in saveLicense:
        print ("license error===")
        # count_right = 
        messagebox.showwarning("License Error", "Invalid license")
        return False
    else:
        if check_tiemEX():
            return True
            # self.destroy()
        else:
            messagebox.showwarning("Time Passed", "Service has Passed")
            return False
        

def getLicenseEX():
    data =  load_json("License.json")
    i = 0
    for key, value in data.items():
            return value
    return ""




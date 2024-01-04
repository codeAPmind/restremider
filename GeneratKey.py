
from key import *

def generate_key(datfileName,jsonfileName):
    if ".dat" in datfileName and os.path.exists(jsonfileName):
        sign(datfileName,key(load(jsonfileName))) 
    else:
        None

if __name__ == '__main__':
    generate_key("keymodel.dat","keymodel.json")
    # print("===",name())
    # print("===7777",sign(sys.argv[2],key(load(sys.argv[1])))) if len(sys.argv)>2 and os.path.exists(sys.argv[1]) else None
    # print("===9999",show(sys.argv[2])) if len(sys.argv)>2 else None

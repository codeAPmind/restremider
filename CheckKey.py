from keygen import *

def verify_cpu(exeName,datfileName):
    if len(datfileName)>1 and os.path.exists(datfileName):
        # print(verify(datfileName,cpu()))
        sys.argv[0]="HideStkXD"
        # print(verify(bb,cpu()))
        return verify(datfileName,cpu())
    else:
        return None

def verify_mac(datfileName):
    if len(datfileName)>1 and os.path.exists(datfileName):
        return verify(datfileName,mac())
    else:
        return None

def verify_datfile_cpu(exeName,datfileName):
    clientinfo = verify_cpu(exeName,datfileName)
    if clientinfo is not None:
        print(clientinfo)
        return clientinfo
    
def verify_buy_trialversion(days):
    name()
    query(f'~{name()}.dat',mac()) if os.path.exists(f'~{name()}.dat') else trial(f'~{name()}.dat',key(sample(t=days)))
    # view(f'~{name()}.dat')
    
    print(name())
    print(query(f'~{name()}.dat',mac()) if os.path.exists(f'~{name()}.dat') else trial(f'~{name()}.dat',key(sample())))
    # print(view(f'~{name()}.dat'))
    
def verify_freedown_trialVer(days,ver):
    print(name())
    returnvalue =  query(permit()) if os.path.exists(permit()) else trial(permit(),key(sample(t = days)))

    if  len(returnvalue) == 1 and (returnvalue[0][3][0] is False or   returnvalue[0][3][1] is False or returnvalue[0][3][2] is False or returnvalue[0][3][3] is False ):
        # print("false")
        return False
    elif  len(returnvalue) >= 1:
        # print("true")
        return True


def get_freedown_trialtime():
    print(name())
    if os.path.exists(permit()):
        returnvalue = query(permit())
        print("ssd",returnvalue[0][1])
        return returnvalue[0][1]
    else:
        return []

    

    
if __name__ == '__main__':
    # verify_datfile_cpu("HideStkXD","keymodel.dat")
    # verify_buy_trialversion()
    # print(verify_freedown_trialVer(0,""))
    # returnvalue = verify_freedown_trialVer(10,"")
    # print("==========",returnvalue)

    get_freedown_trialtime()

    # print(time.time())
    # if returnvalue[0][3][0] is False or   returnvalue[0][3][1] is False or returnvalue[0][3][2] is False or returnvalue[0][3][3] is False :
        # print("fasle")
    # verify("~keygen.dat",cpu())
    # print(name())
    # if len(sys.argv)>1 and os.path.exists(sys.argv[1]):
    #     sys.argv[0]=show(sys.argv[1])[-1][-1]
    #     print(name())
    # print(verify(sys.argv[1],cpu() if len(sys.argv)>2 else mac())) if len(sys.argv)>1 and os.path.exists(sys.argv[1]) else None
    # print(show(sys.argv[1])) if len(sys.argv)>1 else None

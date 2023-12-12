import json,time,hashlib,datetime
# import uuid

def load(f):
        with open(f) as p:return json.load(p)
def dump(o,f,isSave):
        if isSave:
                with open(f,'w') as p:json.dump(o,p,separators=(',',':'))
                return o
        else:
                for key, value in o.items():
                        return str(value).replace(" ","")

    
# def mac():return hex(uuid.getnode())[2:]
def hexstr(s):return hex(int(datetime.datetime.strptime(s,'%Y%m%d').timestamp()))[2:]
def decint(s):return int(f'0x{s[:8]}',16)
def key(d):return hashlib.blake2b(d.encode()).hexdigest()
def hash(k):return {k:key(k)}
def verify(f):return [time.ctime(decint(i)) for i,j in load(f).items() if key(i)==j and decint(i)>time.time()]
def sign(d,m,f,isSave):return dump(hash(hexstr(d)+m),f,isSave)

if __name__ == '__main__':
        biosinfo = "17605928765BFEBFBFF000306C3To be filled by O.E.MTo be filled by o.E.w."
        endtime= "20240106"
        # [print(sign(i,j,k)) for i,j,k in [('20230101',"13510681710",'key1.json'),('20240101',mac(),'key2.json')]]
        # [print(verify(i)) for i in ('key1.json','key2.json')]
        sign( endtime ,biosinfo,'license1.json',True)
        aa = sign(endtime ,biosinfo ,'license1.json',False)
        print("=======",aa,len(aa))
        # print(verify("license.json"))
import os,sys,bz2,gzip,lzma,zlib,json
from name import *

def suffix(f):return list(filter(None,os.path.splitext(f)))[-1]
def dump1(o,f):
    with open(f,'w') as p:return [o][bool(json.dump(o,p,indent=1))]
def load(f):
    with open(f) as p:return json.load(p)
def dump(o,f):
    with open(f,'w') as p:return [o][bool(json.dump(o,p,separators=(',',':')))]
def loads(f):
    with open(f,'rb') as p:return json.loads({'.bin':bz2.decompress,'.dat':gzip.decompress,'.lib':lzma.decompress}.get(suffix(f).casefold(),zlib.decompress)(p.read()).decode())
def dumps(o,f):
    with open(f,'wb') as p:return (o,o)[bool(p.write({'.bin':bz2.compress,'.dat':gzip.compress,'.lib':lzma.compress}.get(suffix(f).casefold(),zlib.compress)(json.dumps(o,separators=(',',':')).encode())))]
def read(f):return (loads,load)['.json'==suffix(f).casefold()](f)
def write(o,f):return (dumps,dump)['.json'==suffix(f).casefold()](o,f)

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(write(read(sys.argv[1]),sys.argv[2])) if len(sys.argv)>2 and os.path.exists(sys.argv[1]) else None

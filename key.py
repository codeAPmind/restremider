import time,ctypes,hashlib,pathlib,collections,dataclasses
from convert import *
from template import *

def hide(f):return ctypes.windll.kernel32.SetFileAttributesW(f,0x02) if os.name=='nt' and os.path.exists(f) else None
def hash(k):return hashlib.blake2b(f'{tuple(k)}'.encode()).hexdigest()+hashlib.sha3_512(f'{list(k)}'.encode()).hexdigest()
def permit(l=[]):return l[0 if l else bool(l.append(os.path.join(pathlib.Path.home(),f'.{hex(mac())[2:]}{name().encode().hex()}')))]
def key(d):return collections.namedtuple(pathlib.Path(__file__).stem,d.keys())(*(lambda x:(int(next(x)*86400+time.time()),*x))(iter(d.values())))
def values(c):return [getattr(c,i.name) for i in dataclasses.fields(c)]
def dc(d):return dataclasses.make_dataclass(pathlib.Path(__file__).stem,d.keys())(*d.values())
def nt(d):return collections.namedtuple(pathlib.Path(__file__).stem,d.keys())(*d.values())
def view(f):return *((lambda x:(x,time.ctime(x.time),i))(nt(j)) for i,j in read(f).items()),
def sign(f,k):return [(lambda x:(x,time.ctime(x.time),i))(nt(j)) for i,j in write({hash(k):dict(zip(k._fields,k))},f).items()]
def verify(f,p):return [(lambda x:(x,time.ctime(x.time),i))(nt(j)) for i,j in read(f).items() if (lambda x:x.time>time.time() and x.pc==p and x.app==name() and hash(x)==i)(nt(j))]
def trial(f,k):return sign(f,k)+[hide(f)]

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(sign(license(),key(dump1(sample(app=sys.argv[1] if len(sys.argv)>1 else None),config()))))

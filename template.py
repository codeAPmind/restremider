from name import *
from convert import *
import templet

def sample(**d):
    if not d.get('pc'):d['pc']=mac()
    if not d.get('app'):d['app']=name()
    return {**templet.s(),**d}

def make(o,f):
    with open(f,'w') as p:return (o,o)[bool(p.write(f'def s():return {o}'))]

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(make(load(sys.argv[1]),'templet.py')) if len(sys.argv)>1 and '.json'==suffix(sys.argv[1]) and 's' not in dir(templet) else None

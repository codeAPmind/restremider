import os,sys,uuid

def mac(l=[]):return l[0 if l else bool(l.append(uuid.getnode()))]
def name():return os.path.splitext(os.path.basename(sys.argv[0]))[0]
def config(l=[]):return l[0 if l else bool(l.append(f'~{name()}.json'))]
def license(l=[]):return l[0 if l else bool(l.append(f'~{name()}.dat'))]
def file():return sys.argv[0],__file__
def stem(f=None,l=[]):return l[0 if l else bool(l.append(os.path.splitext(os.path.basename(f or sys.argv[0]))[0]))]
def path(f,r=True):return f if os.path.exists(f) else path(os.path.join(os.path.dirname(__file__),os.path.basename(f)),False) if r else ''
def datfile(f=None):return f'{stem(f)}.dat'
def jsonfile(f=None):return f'{stem(f)}.json'

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(mac())
    print(sys.argv[1],path(sys.argv[1])) if len(sys.argv)>1 else None

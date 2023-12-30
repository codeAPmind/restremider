from keygen import *

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(sign(sys.argv[2],key(load(sys.argv[1])))) if len(sys.argv)>2 and os.path.exists(sys.argv[1]) else None

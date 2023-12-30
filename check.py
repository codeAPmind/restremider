from keygen import *

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    if len(sys.argv)>1 and os.path.exists(sys.argv[1]):
        sys.argv[0]=view(sys.argv[1])[0][0].app
        print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
        print(query(sys.argv[1]))

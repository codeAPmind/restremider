from keygen import *

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(query(license()) if os.path.exists(license()) else query(permit()) if os.path.exists(permit()) else trial(permit(),key(sample())))

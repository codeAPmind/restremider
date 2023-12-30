from name import *
from convert import *
from template import make
import setting

if __name__ == '__main__':
    print(file(),datfile(sys.argv[1] if len(sys.argv)>1 else __file__),jsonfile())
    print(make(load('settings.json'),'setting.py')) if 's' not in dir(setting) else None

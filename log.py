
from loguru import logger

class Log:
    def __init__(self):
        super().__init__()
        
    def initLog(self,name):
        logger.add(name+ '.log')

    def logKey(self,key):
        logger.debug(f'{key} :pushed') 
        
    def log(self,content):
        logger.debug(content) 


if __name__ == '__main__':
    ll = Log()
    ll.initLog("test")
    ll.log("hello")
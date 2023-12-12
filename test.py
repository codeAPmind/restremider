
from pynput import keyboard,mouse
from loguru import logger
from threading import Thread
import time
import schedule
 
# 定义日志文件
logger.add('demo.log')
working = False
mouse_start_time = time.time()
key_start_time = time.time()

def on_press(key):
    #working = True
    key_start_time = time.time()
    logger.debug(f'{key} :pushed') 
    
def on_release(key):
    #print(f'{key} released')
    if key == keyboard.Key.esc:
        # Stop listener
        return False
# 定义f1用于线程1



def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        mouse_start_time = time.time()
        #working = True
        logger.debug('left was pressed!')
    elif button == mouse.Button.right:
        mouse_start_time = time.time()
        #working = True
        logger.debug('right was pressed!')
        #return False
    else:
        logger.debug('mid was pressed!') 
        
        
def f1():
    with keyboard.Listener(on_press=on_press,on_release=on_release) as lsn:
        lsn.join()
        

        
# 定义f2用于线程2
def f2():
    # Collect events until released
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
        
        
def noworking():
    working = False
    mouse_elapsed_time = time.time() - mouse_start_time
    key_elapsed_time = time.time() - key_start_time
    print(mouse_start_time)
    if mouse_elapsed_time >10 and key_elapsed_time > 10:
        print("not working====")

schedule.every(30).minutes.do(noworking)        

if __name__ == '__main__':

    schedule.run_pending()
    time.sleep(3)
        
    try:
        # 起两个线程分别监控键盘和鼠标
        t1 = Thread(target=f1)
        t2 = Thread(target=f2)

        
        t1.start()
        t2.start()

        

    except:
        print("error, unable to start ")

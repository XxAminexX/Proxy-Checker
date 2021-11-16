import os.path
import time
from tkinter import filedialog
from queue import Queue
from threading import Thread
import requests
proxies = []

msg = '''
            ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗          
            ██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝          
            ██████╔╝██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝           
            ██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝            
            ██║     ██║  ██║╚██████╔╝██╔╝ ██╗   ██║             
            ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝             
                                                                
███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
                                                                

'''


def check_file():
    print(msg)
    print('          | ======================================= |')
    time.sleep(0.5)
    print('          |         Open Your Proxy List:           |')
    time.sleep(0.5)
    print('          | ======================================= |\n')
    time.sleep(0.5)
    if os.path.isfile('Good_Proxies.txt'):
        os.remove('Good_Proxies.txt')
    else:
        pass


def CheckProxy(q):
    while True:
        value = q.get()
        try:
            requests.get(url='https://www.google.com', proxies={'https': f'http:{value}'}, timeout=2)
            with open('Good_Proxies.txt', 'a+') as good:
                good.writelines(value + '\n')
            print('Good Proxy: ' + value)
        except:
            print('Bad Proxy: ' + value)
        q.task_done()


def GetProxies():
    global proxies

    proxy_list = filedialog.askopenfile(title='Open Your Proxy List', filetypes={('Text', '*.txt')})
    for proxy in proxy_list:
        cb = proxy.replace('\n', '')
        proxies.append(cb)
    return proxies


if __name__ == '__main__':
    check_file()
    q= Queue()
    num_threads = 100
    for _ in range(num_threads):
        thread = Thread(target=CheckProxy, args=(q,))
        thread.daemon=True
        thread.start()

    for prx in GetProxies():
        q.put(prx)
    q.join()
    print('We Finish Scanning All Your Proxies List!')
    os.system('pause')
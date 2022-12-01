from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import threading
from multiprocessing import Process
import httpx

urls = list(map(lambda x:'https://jsonplaceholder.typicode.com/users/' + str(x),range(1,11)))

start_time = datetime.now()
for url in urls:
    r = httpx.get(url)
print("base", datetime.now() - start_time)

#import threading
def try_threading(url):
    r = httpx.get(url)

start_time = datetime.now()
for url in urls:
    my_thread = threading.Thread(target=try_threading, args=(url,))
    my_thread.run()
print("threading", datetime.now() - start_time)

#from concurrent.futures import ThreadPoolExecutor

start_time = datetime.now()
with ThreadPoolExecutor(10) as executor:
    executor.map(httpx.get, urls);
print("ThreadPoolExecutor", datetime.now() - start_time)

#from multiprocessing import Process
start_time = datetime.now()

def try_process(url):
    r = httpx.get(url)
for url in urls:
    process = Process(target=try_process, args=(url,))
    process.start()
    process.join()
print("multiprocessing", datetime.now() - start_time)



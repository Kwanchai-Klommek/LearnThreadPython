# Thread Multi-Thread 2

from threading import Thread

def thread_callback(name, end):
	for i in range(1, end+1):
		print(name + ": " + str(i))


thr1 = Thread(target=thread_callback, args=['Thread-1', 500000])
thr2 = Thread(target=thread_callback, args=['Thread-2', 500000])

thr1.start()
thr2.start()

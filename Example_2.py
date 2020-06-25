# Create Thread 2

import threading

def thread_callback(name, loop):
	for i in range(1, loop+1):
		print("%s: %i" %(name, i))

thr = threading.Thread(target=thread_callback, args=["Thread-1", 5])
thr.start()
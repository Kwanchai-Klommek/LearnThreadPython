# Create Thread 1

import threading

def thread_callback():
	print("Hello inside Thread")

thr = threading.Thread(target=thread_callback)
thr.start()


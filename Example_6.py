# Thread Joining 1

from threading import Thread

class Counter(Thread):

	def __init__(self, end):
		Thread.__init__(self)
		self.end = end

	def run(self):
		for i in range(1, self.end+1):
			print(self.name + ": " + str(i))


thr1 = Counter(500000)
thr1.start()

# Block until thread 1 is done
thr1.join()

thr2 = Counter(500000)
thr2.start()

# Create Multi-thread

from threading import Thread

class Counter(Thread):

	def __init__(self, end):
		Thread.__init__(self)
		self.end = end

	def run(self):
		for i in range(1, self.end+1):
			print(self.name + ": " + str(i))

thr1 = Counter(5)
thr2 = Counter(5)

thr1.start()
thr2.start()

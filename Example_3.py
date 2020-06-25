# Create Class Thread 

from threading import Thread

class MyThread(Thread):

	def __init__(self, firstName):
		Thread.__init__(self)
		self.firstName = firstName

	# run when called .start() method
	def run(self):
		print("Hello " + self.firstName + " from " + self.name)

thr1 = MyThread("Champ")
thr2 = MyThread("Boy")
thr3 = MyThread("Hi")

thr1.start()
thr2.start()
thr3.start()
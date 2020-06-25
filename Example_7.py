# Thread Joining 2

from threading import Thread
import numpy as np

class BubbleSorting(Thread):

	def __init__(self, numbers):
		Thread.__init__(self)
		self.numbers = numbers

	def run(self):
		n = len(self.numbers)
		for i in range(n):
			for j in range(0, n-i-1):
				if self.numbers[j] > self.numbers[j+1]:
					temp = self.numbers[j]
					self.numbers[j] = self.numbers[j+1]
					self.numbers[j+1] = temp

# List of number to sort
numbers = np.random.randint(1000000, size=20000)

middle_idx = int(numbers.size/2)

# Slice list into half and supply to each thread
thr1 = BubbleSorting(numbers[:middle_idx])
thr2 = BubbleSorting(numbers[middle_idx:])

thr1.start()
thr2.start()

# Wait for all threads to complete
thr1.join()
thr2.join()

# Obtain sorted lists from threads
arr_1 = thr1.numbers
arr_2 = thr2.numbers

len1 = arr_1.size
len2 = arr_2.size

# Merge sorted array to final list
sorted_numbers = []
i = j = 0
while i < len1 and j < len2:
	if arr_1[i] <= arr_2[j]:
		sorted_numbers.append(arr_1[i])
		i += 1
	else:
		sorted_numbers.append(arr_2[j])
		j += 1

while i < len1:
	sorted_numbers.append(arr_1[i])
	i += 1

while j < len2:
	sorted_numbers.append(arr_2[j])
	j += 1

print("Sorted from Thread-1:", arr_1)
print("Sorted from Thread-2:", arr_2)

print("Final sorted:", sorted_numbers)
import time 

class Hello:
	def __init__(self):
		self._author = 'Shiv Shakti'
	def print_message(self):
		print('Hello world from {} at {}'.format(self._author, time.time()))

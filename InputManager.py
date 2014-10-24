class InputManager:

	def __init__(self):
		super(InputManager, self).__init__()
		self.helloPhrase = "Enter some text: "

	def _getMessage(self):
		return self.message

	def _setMessage(self, newMessage):
		self.message = newMessage

		message = property(_getMessage, _setMessage)	

	def readInput(self):
		return input(self.helloPhrase + "\n")

	
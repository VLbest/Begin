from HexGenerator import HexGenerator

class MD5:

	def __init__(self):
		super(MD5, self).__init__()
		self.hexGenerator = HexGenerator()
		self.resutat = ""
		self.target = ""
		self.targetHex = ""

	def getMD5HashOf(self, value):
		self.target = value
		self.createHash()
		return self.resutat

	def createHash(self):
		self.targetHex = self.hexGenerator.getHexOf(self.target)

		
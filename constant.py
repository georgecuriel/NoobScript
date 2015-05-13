class Constant:

	memInt = [None] * 500
	memFloat = [None] * 500
	memString = [None] * 500
	constantes = []

	for eachLine in open('constantes.txt', "r"):
		constantes.append([int(k) for k in eachLine.split()])
	print constantes

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				self.memInt[dirReal] = val
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				self.memFloat[dirReal] = val

	def getValD(self, dire, tipo):
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemString(self,dire, val):
		dirReal = dire - 8500
		if dirReal < 500:
			self.memString[dirReal] = val

	def getMemString(self, dire):
		dirReal = dire - 8500
		if dirReal < 500:
			return self.memString[dirReal]
class Constant:

	memInt = [None] * 500
	memFloat = [None] * 500
	memString = [None] *500

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				memInt[dirReal] = int(val)
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD(self, dire, tipo):
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				return memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				return memFloat[dirReal]

	def setMemString(self,dire, val):
		dirReal = dire - 8500
		if dirReal < 500:
			memString[dirReal] = val

	def getMemString(self, dire):
		dirReal = dire - 8500
		if dirReal < 500:
			return memString[dirReal]
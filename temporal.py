class Temporal: 

	enteros = 7000
	flotantes = 7500
	esverdad = 8000
	frases = 8500

	memInt = []
	memFloat = []
	memBool = []
	memString = []
	memInt = [None]*500
	memFloat = [None]*500
	memBool = [None]*500
	memString = [None]*500

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				self.memInt[dirReal] = val
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD (self, dire, tipo):
		global enteros
		global flotantes
		if tipo == 1:
			dirReal = dire - 7000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 7500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemBool(self, dire, val):
		global esVerdad
		dirReal = dire - 8000
		if dirReal < 500:
			memBool[dirReal] = self.val
		
	def getMemBool(self, dire):
		global esVerdad
		dirReal = dire - 2000
		if dirReal < 8000:
			return self.memBool[dirReal]
		
	def setMemString(self, dire, val):
		global frases
		dirReal = dire - 8000
		if dirReal < 500:
			memString[dirReal] = self.val
		
	def getMemString(self ,dire):
		global frases
		dirReal = dire - 8500
		if dirReal < 500:
			return self.memString[dirReal]
	
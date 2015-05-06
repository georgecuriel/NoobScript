class Local: 

	enteros = 3000
	flotantes = 3500
	esverdad = 4000
	frases = 4500
	
	memInt = [0]*500
	memFloat = [0]*500
	memBool = [0]*500
	memString = [0]*500

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 3000
			if dirReal < 500:
				self.memInt[dirReal] = val
		elif tipo == 2:
			dirReal = dire - 3500
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD (self, dire, tipo):
		global enteros
		global flotantes
		if tipo == 1:
			dirReal = dire - 3000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 3500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemBool(self, dire, val):
		global esVerdad
		dirReal = dire - 4000
		if dirReal < 500:
			memBool[dirReal] = self.val
		
	def getMemBool(self, dire):
		global esVerdad
		dirReal = dire - 4000
		if dirReal < 500:
			return self.memBool[dirReal]
		
	def setMemString(self, dire, val):
		global frases
		dirReal = dire - 4500
		if dirReal < 500:
			memString[dirReal] = self.val
		
	def getMemString(self ,dire):
		global frases
		dirReal = dire - 4500
		if dirReal < 500:
			return self.memString[dirReal]
	
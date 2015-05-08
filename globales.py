class Global: 

	#enteros = 1000
	#flotantes = 1500
	#esverdad = 2000
	#frases = 2500

	memInt = globales[1][500]
	memFloat = [None]*500
	memBool = [None]*500
	memString = [None]*500
	
	

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 1000
			if dirReal < 500:
				self.memInt[dirReal] = val
		elif tipo == 2:
			dirReal = dire - 1500
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD (self, dire, tipo):
		if tipo == 1:
			dirReal = dire - 1000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 1500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemBool(self, dire, val):
		global esVerdad
		dirReal = dire - 2000
		if dirReal < 500:
			memBool[dirReal] = self.val
		
	def getMemBool(self, dire):
		global esVerdad
		dirReal = dire - 2000
		if dirReal < 500:
			return self.memBool[dirReal]
		
	def setMemString(self, dire, val):
		global frases
		dirReal = dire - 25000
		if dirReal < 500:
			memString[dirReal] = self.val
		
	def getMemString(self ,dire):
		global frases
		dirReal = dire - 2500
		if dirReal < 500:
			return self.memString[dirReal]
	
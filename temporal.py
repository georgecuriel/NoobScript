class Temporal:
	
	
	#TEMPENTERO =5000
	#TEMPDECIMAL =5500
	#TEMPesVerdad =6000
	#TEMPFRASE =6500
	
	memInt = [None]*500
	memFloat = [None]*500
	memBool = [None]*500
	memString = [None]*500

	def setValD(self, dire, val, tipo):
		if tipo == 1:
			dirReal = dire - 5000
			if dirReal < 500:
				self.memInt[dirReal] = val
		elif tipo == 2:
			dirReal = dire - 5500
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD (self, dire, tipo):
		if tipo == 1:
			dirReal = dire - 5000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 5500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemBool(self, dire, val):
		dirReal = dire - 6000
		if dirReal < 500:
			memBool[dirReal] = self.val
		
	def getMemBool(self, dire):
		global esVerdad
		dirReal = dire - 6000
		if dirReal < 500:
			return self.memBool[dirReal]
		
	def setMemString(self, dire, val):
		global frases
		dirReal = dire - 6500
		if dirReal < 500:
			memString[dirReal] = self.val
		
	def getMemString(self ,dire):
		global frases
		dirReal = dire - 6500
		if dirReal < 500:
			return self.memString[dirReal]
	
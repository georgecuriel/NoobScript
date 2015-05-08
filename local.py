class Local: 

	#LOCALENTERO =3000
	#LOCALDECIMAL =3500
	#LOCALesVerdad =4000
	#LOCALFRASE =4500	
	
	memInt = [None]*500
	memFloat = [None]*500
	memBool = [None]*500
	memString = [None]*500
	
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
		if tipo == 1:
			dirReal = dire - 3000
			if dirReal < 500:
				return self.memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - 3500
			if dirReal < 500:
				return self.memFloat[dirReal]

	def setMemBool(self, dire, val):
		dirReal = dire - 4000
		if dirReal < 500:
			memBool[dirReal] = self.val
		
	def getMemBool(self, dire):
		dirReal = dire - 4000
		if dirReal < 500:
			return self.memBool[dirReal]
		
	def setMemString(self, dire, val):
		dirReal = dire - 4500
		if dirReal < 500:
			memString[dirReal] = self.val
		
	def getMemString(self ,dire):
		dirReal = dire - 4500
		if dirReal < 500:
			return self.memString[dirReal]
		
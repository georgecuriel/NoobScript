class Global: 

	enteros = 1000
	flotantes = 1500
	esverdad = 2000
	frases = 2500

	memInt = []
	memFloat = []
	memBool = []
	memString = []

	def setValD(dire, val, tipo):
		if tipo == 1:
			dirReal = dire - enteros
			if dirReal < 500:
				memInt[dirReal] = int(val)
		elif tipo == 2:
			dirReal = dire - flotantes
			if dirReal < 500:
				memFloat[dirReal] = val

	def getValD (dire, tipo):
		if tipo == 1:
			dirReal = dire - enteros
			if dirReal < 500:
				return memInt[dirReal]
		elif tipo == 2:
			dirReal = dire - flotantes
			if dirReal < 500:
				return memFloat[dirReal]

	def setMemBool(dire, val):
		dirReal = dire - esverdad
		if dirReal < 500:
			memBool[dirReal] = val
		
	def getMemBool(dire):
		dirReal = dire - esverdad
		if dirReal < 500:
			return memBool[dirReal]
		
	def setMemString(dire, val):
		dirReal = dire - frases
		if dirReal < 500:
			memString[dirReal] = val
		
	def getMemString(dire):
		dirReal = dire - frases
		if dirReal < 500:
			return memString[dirReal]
	
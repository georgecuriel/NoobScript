from tokens import *
class Constant:

	memInt = [None] * 500
	memFloat = [None] * 500
	memString = [None] *500


for x in directorioconst:
    opcion = checaTipo(directorioconst[x])
    if opcion == 1 or opcion == 2:
        memconstant.setValD(directorioconst[x], x, opcion)
        print  memconstant.getValD(directorioconst[x], opcion)
    else:
        memconstant.setMemString(directorioconst[x], x, opcion)

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
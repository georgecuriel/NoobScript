    
x_table = []
for eachLine in open('cuadruplos.txt', "r"):
    x_table.append([int(k) for k in eachLine.split()])
    
print x_table[2][2]
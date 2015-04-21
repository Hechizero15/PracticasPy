'''
Programa para ordenar cedulas de menor a mayor y viceversa.
'''
opc = 's'
cedulas = []
i = 0
while (opc == 's' or opc == 'S'):
	cedula = raw_input('Por favor, Ingrese un numero de cedula: ')
	while (len(cedula) == 0):
		cedula = raw_input('Por favor, Ingrese un numero de cedula: ')
	cedulas.append(int(cedula))
	opc = raw_input('Desea ingresar otra cedula? (S/n): ')
print 'Su lista de cedulas fue :\n' + str(cedulas)
cedulas.sort()
print 'Sus cedulas ordenadas de Menor a Mayor: \n' + str(cedulas)
cedulas.reverse()
print 'Sus cedulas ordenadas de Mayor a Menor: \n' + str(cedulas)
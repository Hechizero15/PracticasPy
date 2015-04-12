# Un primer programa en python nada complicado
opc = 'S'

while (opc == 'S' or opc == 's'):

	usr = raw_input('Hola, Ingresa tu nombre: ')
	while (len(usr) == 0):
		usr = raw_input('Debes Ingresar tu nombre para usar el programa.\nIngresa tu nombre: ')
	num1 = raw_input('Ingrese un numero: ')
	while (len(num1) == 0):
		num1 = raw_input('Debes Ingresar un numero: ')
	num1 = float(num1)
	num2 = raw_input('Ingrese otro numero: ')
	while (len(num2) == 0):
		num2 = raw_input('Debes ingresar un segundo numero:')
	num2 = float(num2)

	# aqui empiezo con los calculos
	print usr + ' La suma de sus numeros es: ' + str(int(num1+num2))
	print 'Restando ' + str(num1) + ' - ' + str(num2) + ' el resultado es: ' + str(num1-num2)
	print 'Restando ' + str(num2) + ' - ' + str(num1) + ' el resultado es: ' + str(num2-num1)
	print 'La multiplicacion de sus numeros es: ' + str(num1*num2)
	print 'Dividiendo ' + str(num1) + ' / ' + str(num2) + ' el resultado es: ' + str(num1/num2)
	print 'Dividiendo ' + str(num2) + ' / ' + str(num1) + ' el resultado es: ' + str(num2/num1)
	print 'Si elevamos ' + str(num1) + ' al exponente ' + str(num2) + ' el resultado es: ' + str(pow(num1, num2))
	print 'Si elevamos ' + str(num2) + ' al exponente ' + str(num1) + ' el resultado es: ' + str(pow(num2, num1))
	print 'La raiz cuadrada de '+ str(num1) +' es: ' + str(pow(num1, 0.5))
	print 'La raiz cuadrada de '+ str(num2) +' es: ' + str(pow(num2, 0.5))
	print 'La raiz ' + str(num2) + ' de ' + str(num1) + ' es: ' + str(pow(num1, 1/num2))
	print 'La raiz ' + str(num1) + ' de ' + str(num2) + ' es: ' + str(pow(num2, 1/num1))

	opc = raw_input('Desea continuar? (S/n): ')
	while (len(opc) == 0):
		opc = raw_input('Desea continuar? (S/n): ')

print 'Hasta luego '+ usr 
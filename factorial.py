#Programemos un simple factorial

opc = 's'
while (opc == 'S' or opc == 's'):
	num = raw_input('Ingrese un numero entero: ')
	while (len(num) == 0):
		num = raw_input('Por favor, Ingrese un numero entero: ')
	num = int(num)
	neg = 0
	if (num < 0):
		num = num * -1
		neg = 1
	i = 1
	fac = 1
	while (i <= num):
		fac *= i
		i += 1
	if (neg == 1):
		num = num * -1
		fac = fac * -1
	print 'El factorial del numero: ' + str(num) + ', es: ' + str(fac)
	opc = raw_input('Desea continuar? (S/n): ')
	while (len(opc) == 0):
		opc = raw_input('Desea continuar? (S/n): ')
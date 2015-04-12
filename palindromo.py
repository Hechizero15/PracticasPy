#Primero pedimos una palabra
pal = raw_input('Ingrese una palabra: ')
while (len(pal) == 0):
	pal = raw_input('Debe Igresar una palabra: ')

#Guardamos el tama7o de la palabra
tam = len(pal)
i = 0
pali = 0
pal2 = []
while (i <= tam-1):
	pal2.insert(i, pal[i])
	i += 1
j = 0
while (j <= tam-1):
	if (pal[j] == pal2.pop()):
		pali = 1
	else:
		pali = 0
	j += 1
if (pali == 1):
	print 'Su palabra es un palindromo'
else:
	print 'Su palabra no es un palindromo'
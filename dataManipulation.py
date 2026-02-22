arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Python \n')
arquivo.write('Vasco da Gama')
arquivo.close()

#leitura do arquivo texto

leitura = open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
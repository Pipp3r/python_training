arquivo = open('arq_text.txt', 'w')

arquivo.write('\nescrevendo no arquivo de texto \n')
arquivo.write('deu tudo certo!!!\n')
arquivo.close()

# ler o arquivo de texto

leitura = open('arq_text.txt', 'r')
print(leitura.read())
leitura.close()

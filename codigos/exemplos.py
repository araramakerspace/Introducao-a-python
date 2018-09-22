import os, sys
'''
Códigos da aula 1 de python do arara makerspace
'''








if __name__ == '__main__':
	
	a = input()

	if(a == 'J'):
		print('Luan doente')
	elif(a =='M'):
		print('luan doente')
	else:
		print('luan doente')


	print("Comando while")
	b= 1
	while b< 10:
		print('luan doente')
		b+=1

	print("Comando for")
	for i in range(12,16): print(i)
	for i in range(0,10,2): print(i)
	for i in range(5,-1,-1): print(i) 


	print("Lista")

	maker = ['matheus','luan', 'gabis', 'augusto', 'guina' , 'risadinha']
	
	for i in maker: print(i)
	for i in range(0,len(maker)):print(maker[i])

	print(maker[-1])
	print(maker[1])
	print(maker)


	Pessoa = {'name':'MANAO', 'especie':'doentao','idade':'54'}
	for v in Pessoa.values():
		print(v)

	for k in Pessoa.keys():
		print(k)

	for i in spam.items():
		print(i)

	for k, v in spam.items():
		print('Key'+k+  'Value'+str(v))

	'Manao' in Pessoa.values()
	
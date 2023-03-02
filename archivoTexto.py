'''
f = open('alumnos.txt','r')
nombres = f.read()
print(nombres)
#controlar la posicion
f.seek(9)
nombres2 = f.read()
print(nombres2)
f.close()
'''
'''
f = open('alumnos.txt','r')
nombres = f.readline()
print(nombres)
f.close()
'''

f = open('alumnos.txt','r')
nombres2 = f.readlines()
print(nombres2)
f.close()
# ['Hola mundo\n', 'Hola mundo 2']

'''
for item in nombres:
    print(item,end='')
'''
'''
# remplaza el comtenido anterior con el nuevo
f = open('alumnos.txt','w')
f.write("Hola mundo")
f.close()
'''
'''
# agrega solamente el nuevi contenido, manteniendo el anterior
f = open('alumnos.txt','a')
f.write('\n' + "Hola mundo 2")
f.close()
'''
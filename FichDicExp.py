#!usr/bin/python3
fich = open("/etc/passwd","r")
usuarios = fich.readlines()
fich.close()
dicc = {}
root = 'root'
imaginario = 'imaginario'
for usuario in usuarios:
    dicc[usuario.split(':')[0]] = (usuario.split(':')[-1][:-1])

try:
    print("Key:", root, "---> Value:", dicc[root])
    print("Key:", imaginario,"---> Value:", dicc[imaginario])
except KeyError:
    print("No existe esa key en este diccionario")

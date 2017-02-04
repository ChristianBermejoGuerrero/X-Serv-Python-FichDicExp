#!usr/bin/python3
try:
    fich=open("/etc/passwd","r")
    usuarios=fich.readlines()
    fich.close()
    dicc = {}
    root = 'root'
    imaginario = 'imaginario'
    for usuario in usuarios:
        dicc[usuario.split(':')[0]] = (usuario.split(':')[-1])

    print("Key:", root, "---> Value:", dicc[root])
    print(dicc[imaginario])
except KeyError: 
    print("No existe esa key en este diccionario")

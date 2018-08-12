def leer_pukamones(archiv):
    datos = open(archiv)
    lista = []
    for linea in datos:
        nombre,cordx,cordy = linea.strip().split(";")
        a = (nombre,float(cordx),float(cordy))
        lista.append(a)
    datos.close()
    return lista

def cercania(pos,radio,archivo):
    datos = open(archivo)
    dicc={}
    for linea in datos:
        nombre,cordx,cordy = linea.strip().split(";")
        distancia = ((pos[0]-float(cordx))**2+(pos[1]-float(cordy))**2)**0.5
        if distancia < radio:
            if 1 in dicc:
                dicc[1].append(nombre)
            else:
                dicc[1] = [nombre]
        elif distancia <2*radio:
            if 2 in dicc:
                dicc[2].append(nombre)
            else:
                dicc[2] = [nombre]
        else:
            if 3 in dicc:
                dicc[3].append(nombre)
            else:
                dicc[3] = [nombre]
    datos.close()
    return dicc

def itinerario_pokemon(pos,radio,archivo,archivofinal):
    datos = cercania(pos,radio,archivo)
    escribir = open(archivofinal,"w")
    escribir.write("Itinerario a seguir \n")
    if 1 in datos:
        escribir.write("Pukamones encontrados a 1 grado de cercania \n")
        escribir.write((" - ").join(datos[1])+"\n")
    if 2 in datos:
        escribir.write("Pukamones encontrados a 2 grados de cercania \n")
        escribir.write((" - ").join(datos[2]) +"\n")
    if 3 in datos:
        escribir.write("Pukamones encontrados a 3 grados de cercania \n")
        escribir.write((" - ").join(datos[3]) +"\n")
    
            
    escribir.close()
    return "Archivo de texto generado"
#print leer_pukamones("pukamones.txt")
#print cercania((39,-74),2,"pukamones.txt")
print itinerario_pokemon((39,-74),2,"pukamones.txt","itinerario.txt")


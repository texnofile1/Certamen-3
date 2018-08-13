def patentes_por_dueno(archivo):
    arch = open(archivo)
    dicc = {}
    for linea in arch:
        nombre,autos = linea.strip().split(";")
        autos = autos.split(",")
        dicc[nombre] = len(autos)
    arch.close()
    return dicc

def patentes_multadas(arch1,arch2):
    lista = []
    archivo = open(arch1)
    for linea in archivo:
        patente = linea.strip()
        archivo2 = open(arch2)
        for datos in archivo2:
            rut,tag = datos.strip().split(",")
            if rut == patente and tag == "0":
                lista.append(rut)
         archivo2.close()
    archivo.close()
    return lista

def personas_multadas(arch1,arch2,arch3):
    lista = patentes_multadas(arch1,arch2)
    multados= []
    datos = open(arch3)
    for linea in datos:
        linea,autos = linea.strip().split(";")
        autos = autos.split(",")
        for auto in autos:
            if auto in lista:
                if auto not in multados:
                    multados.append(linea)
    datos.close()
    return multados
        
        

#print personas_multadas("registro_diario.txt","patentes.txt","info_duenos.txt")
#print patentes_multadas("registro_diario.txt","patentes.txt")
#print patentes_por_dueno("info_duenos.txt")

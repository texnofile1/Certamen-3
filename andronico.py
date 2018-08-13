#ESTA FUNCION sirve  :) 
def buscar_clientes(archivo,dicom):
    datos = open(archivo)
    dicc = {}
    for linea in datos:
        rut,nombre,estado = linea.strip().split(";")
        if estado == dicom:
            dicc[rut] = nombre
        else:
            continue
    datos.close()
    return dicc

def dar_credito(archivo,run):
    datos = open(archivo)
    for linea in datos:
        rut,nombre,estado = linea.strip().split(";")
        if run == rut:
            if estado == "VIP":
                return True
            else:
                return False
    datos.close()
def contar_clientes(archivo):
    datos = open(archivo)
    dicc = {}
    cont1 = 0
    cont2 = 0
    cont3 = 0
    for linea in datos:
        rut,nombre,estado = linea.strip().split(";")
        if estado == "VIP":
            cont1+=1
            dicc["VIP"] = cont1
        elif estado == "RIP":
            cont2 += 1
            dicc["RIP"] = cont2
        elif estado == "Pendiente":
            cont3 += 1
            dicc["Pendiente"] = cont3
    datos.close()
    return dicc
            
            

#print busca_clientes("clientes.txt","Pendiente")
#print dar_credito("clientes.txt","9999999-k")
#print contar_clientes("clientes.txt")

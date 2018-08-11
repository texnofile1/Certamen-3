def status(tomo, arch):
    archivo = open(arch)
    dicc = {}
    for linea in archivo:
        texto = linea.strip().split(";")
        if texto[0] == tomo:
            if texto[1] == 0 or texto[2] == 0:
                return False
            else:
                
                dicc["Feliz"] = int(texto[1])
                dicc["Satisfecho"] = int(texto[2])
                return dicc
        
    archivo.close()
def alimento(ali, arch):
    archivo = open(arch)
    dicc={}
    for linea in archivo:
        texto = linea.strip().split(";")
        if texto[0] == ali:
            dicc["feliz"] = int(texto[1])
            dicc["satisfecho"] = int(texto[2])
            return dicc
        else:
            return False
    archivo.close()

def alimentar(tomo,ali,arch1,arch2):
    a = status(tomo,arch1)
    b = alimento(ali,arch2)
    dicc1 = {}
    if b == False:
        return "no existe alimento"
    elif a == False:
        return "X.X"
    else:
        feliz = a["Feliz"] + b["feliz"]
        satisfecho = a["Satisfecho"] + b["satisfecho"]
        dicc1["feliz"] = feliz
        dicc1["satisfecho"] = satisfecho
        return dicc1
        
    


print status("pedrotchi","tomodachi.txt")
print alimento("sopaipa","comidas.txt")
print alimentar("pedrotchi","sopaipa","tomodachi.txt","comidas.txt")

import os
import easygui as eg

tab_cancion = '       ----> '
tab_entre_bandas = '\n---*------*------*------*------*------*------*---\n'
indice_de_generos = ''


def generarLista(DIR_IN, sort_por_genero, tab_cancion, tab_entre_bandas, indice_de_generos):
    listaDeTemas = '' #String
    
    #Genero un dicc con banda, genero y lista de temas
    mydict = []      
    for carpeta in os.listdir(DIR_IN):
        print(carpeta)
        try:
            genero = carpeta.split("(")[1].replace(")","").strip() #strip to eliminate trailing blank spaces
            banda = carpeta.split("(")[0].strip()
            temas = []
            
            for cancion in os.listdir(os.path.join(DIR_IN,carpeta)):
                if '.jpg' not in cancion:
                    temas.append(cancion)
        
            mydict.append({'genero': genero, 'banda':banda, 'lista de temas': temas})    
    
        except:  #Si hay elementos sueltos dentro de DIR_IN, saltearlos
            pass    
    #Sort by genre if required
    if sort_por_genero == True:
        miDicc = sorted(mydict, key=lambda mydict: mydict['genero']) 
        #Si pedi ordenar por genero, agrego un indice al inicio del txt.
        #ESTO NO FC--!!
        indice_de_generos = [miDicc[i]['genero'] for i in miDicc]
        listaDeTemas += indice_de_generos
    
    else: 
        miDicc = mydict
    #Paso del dicc a string para escribirlo en un txt.
    listaDeTemas =  ''
    for i in range(len(miDicc)):
        listaDeTemas +=   tab_entre_bandas + f'''Band: {miDicc[i]['banda']} <-> Genre: {miDicc[i]['genero']}''' + tab_entre_bandas
        for k in range(len(miDicc[i]['lista de temas'])):
            listaDeTemas += tab_cancion + miDicc[i]['lista de temas'][k]  + '\n'
        
    return listaDeTemas    
        
def guardarTXT(DIR_OUT, listaDeTemas):
    #open text file
    text_file = open(os.path.join(DIR_OUT, "Song list.txt"), "w", encoding="utf-8")
    #write string to file
    text_file.write(listaDeTemas)
    #close file
    text_file.close()
    
    
#%% PROGRAMA
# listaDeTemas = generarLista(DIR_IN, sort_por_genero)
# guardarTXT(DIR_OUT, listaDeTemas)
    
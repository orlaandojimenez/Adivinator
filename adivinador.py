# -*- coding: cp1252 -*-
fin = "LO ADIVINE!"

def si(preg):
    from string import lower
    resp = lower(raw_input(preg))
    return (resp[0] == 's')

def grabar():
    with open('datos.txt','a') as archi:
        nuevo=raw_input("Lo siento no lo pude adivinar, ¿Que animal era?")
        archi.write(nuevo + "?\n")
    

def leer():
    with open('datos.txt','r') as a:
        linea=a.readline()
        nl = len(open('datos.txt','r').readlines())
        if linea == "":
            grabar()
        else:
                if si("Es un " + linea):
                        print fin
                        
                else:
                    for i,linea in enumerate(a):
                        if si("Es un " + linea):
                             print fin
                        elif i == nl-2:
                             grabar()
                             return 0
                            
        
        
                            
    
            

def main():
    bucle = True
    print "BIENVENIDO AL ADIVINADOR DE ANIMALES"
    while bucle:
        
        print "Tecla tu respuesta segun el caso s/n"
        if not si("Estas pensando en un animal? "): break
        
        
        if si("Tu animal es terrestre?"):
            if si("Tu animal es un reptil?"):
                if si("Tu animal es un depredador?"):
                    if si("Tu animal tiene el hocico y la cola larga?"):
                        if si("Es un cocodrilo?"):
                            print fin
                        else:
                            leer()
                    elif si("Tu animal es venenoso?"):
                        if si("Tu animal se mueve en zic zac?"):
                            if si("Es una serpiente?"):
                                print fin
                            else:
                                leer()
                        else:
                            leer()
                    else:
                        leer()
                elif si("Tu animal cambia de color?"):
                    if si("Es un camaleon?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal es un anfibio?"):
                if si("Tu animal salta?"):
                    if si("Es una rana?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal es un felino?"):
                if si("Tu animal es comun tenerlo como mascota?"):
                    if si("Es un gato?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es llamado 'Rey de la Selva'?"):
                    if si("Es un leon?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es naranja con rayas negras?"):
                    if si("Es un tigre?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal tiene pequeñas manchas negras?"):
                    if si("Es un jaguar?"):
                        print fin
                    else:
                        leer()
                elif si("Es un puma?"):
                        print fin
                else:
                    leer()
            elif si("Tu animal es un canino?"):
                if si("Tu animal es comun tenerlo como mascota?"):
                    if si("Es un perro?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es un depredador?"):
                    if si("Es un lobo?"):
                        print fin
                    else:
                        leer()
            elif si("Tu animal es la mascota de FIME?"):
                if si("Tu animal vive en zonas frias?"):
                    if si("Es un oso polar?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es blanco con manchas negras?"):
                    if si("Es un oso panda?"):
                        print fin
                    else:
                        leer()
                elif si("Es un oso negro?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal es un primate?"):
                if si("Tu animal es grande y fuerte?"):
                    if si("Es un gorila?"):
                        print fin
                    else:
                        leer()
                elif si("Es un mono?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal es comun verlo en un zoologico?"):
                if si("Tu animal tiene trompa?"):
                    if si("Es un elefante?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal tiene el cuello largo?"):
                    if si("Es una jirafa?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es blanco con rayas negras?"):
                    if si("Es una cebra?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal tiene un solo cuerno?"):
                    if si("Tu animal es grande y fuerte?"):
                        if si("Es un rinoceronte?"):
                            print fin
                        else:
                            leer()
                else:
                    leer()
            elif si("Tu animal es comun verlo en granjas o establos?"):
                if si("Tu animal produce leche?"):
                    if si("Tu animal es grande?"):
                        if si("Es una vaca?"):
                            print fin
                        else:
                            leer()
                    elif si("Es una cabra?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal sirve como animal de carga?"):
                    if si("Tu animal tiene orejas grandes?"):
                        if si("Es un burro?"):
                            print fin
                        else:
                            leer()
                    elif si("Es un caballo?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal hace 'oink'?"):
                    if si("Tu animal es un cerdo?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal impregna mal olor al orinar?"):
                if si("Es un zorrillo?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal se caracteriza por comer zanahorias?"):
                if si("Es un conejo?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal se caracteriza por tener queso?"):
                if si("Es un raton?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal tiene joroba?"):
                if si("Tu animal vive en desiertos?"):
                    if si("Es un camello?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal tiene espinas?"):
                if si("Es un puerco espin?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal tala arboles?"):
                if si("Es un castor?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal esta relacionado con la navidad?"):
                if si("Es un reno?"):
                    print fin
                else:
                    leer()
            else:
                leer()
        elif si("Tu animal es marino?"):
            if si("Tu animal es comun tenerlo como mascota?"):
                if si("Es un pez?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal es un depredador?"):
                if si("Es un tiburon?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal se dice ser inteligente?"):
                if si("Tu animal tiene bigote?"):
                    if si("Es una foca?"):
                        print fin
                    else:
                        leer()
                elif si("Es un delfin?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal vive en zonas frias?"):
                if si("Es un pinguino?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal avienta agua por un orificio?"):
                if si("Tu animal es grande?"):
                    if si("Es una ballena?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal tiene caparazon?"):
                if si("Es una tortuga?"):
                    print fin
                else:
                    leer()
            else:
                leer()
        elif si("Tu animal es un ave?"):
            if si("Tu animal es nocturno?"):
                if si("Tu animal tiene ojos grandes?"):
                    if si("Es un buho?"):
                        print fin
                    else:
                        leer()
                elif si("Es un murcielago?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal es un cazador?"):
                if si("Tu animal se dice tener buena vista?"):
                    if si("Es un aguila?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es comun verlo en las playas?"):
                    if si("Es un pelicano?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal no vuela?"):
                if si("Tu animal es comun verlo en un establo?"):
                    if si("Es una gallina?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es rapido?"):
                    if si("Es un avestruz?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal es comun ver en la vida diaria?"):
                if si("Es un pajaro?"):
                    print fin
                elif si("Es una paloma?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal es un ave acuatica?"):
                if si("Tu animal hace 'cuac'?"):
                    if si("Es un pato?"):
                        print fin
                    else:
                        leer()
                elif si("Tu animal es rosado?"):
                    if si("Es un flamenco?"):
                        print fin
                    else:
                        leer()
                else:
                    leer()
            elif si("Tu animal tiene un pico colorido?"):
                if si("Es un tucan?"):
                    print fin
                else:
                    leer()
            elif si("Tu animal tiene muchas plumas coloridas?"):
                if si("Es un pavo real?"):
                    print fin
                else:
                    leer()
            else:
                leer()
        else:
            print "Escoge un tipo de animal"
            
        

 
    return 0
 
if __name__ == '__main__':
    main()

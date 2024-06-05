import random
import Constantes
import pygame,sys
import time
from pygame import *

pygame.init()



PANTALLA = pygame.display.set_mode((Constantes.ANCHO,Constantes.ALTO))
pygame.display.set_caption("LA TIENDITA")

letra = font.SysFont("Calibri",35,True)
letra2 = font.SysFont("Arial",35,True)
letrach = font.SysFont("Calibri",28,True)
letrag = font.SysFont("Calibri",60,True)

####IMAGENES####
#ICONO DE VENTANA
icono = pygame.image.load("Juego/imagenes/icono.jpg")
pygame.display.set_icon(icono)
#FONDO DE PANTALLA
fondo = pygame.image.load("Juego/imagenes/fondo.jpg")
sound_img = pygame.image.load("Juego/imagenes/sound.png")
mute_img = pygame.image.load("Juego/imagenes/mute.png")
#FONDO DE VENTANA MODOS
modos = pygame.image.load("Juego/imagenes/modos.jpg")
#IMAGENES DE MODOS
normal_img = pygame.image.load("Juego/imagenes/normal.jpg")
contrarreloj_img = pygame.image.load("Juego/imagenes/contrarreloj.jpg")
#IMAGENES DE INSTRUCCIONES
lista_img = pygame.image.load("Juego/imagenes/lista_img.jpg")
inst_img = pygame.image.load("Juego/imagenes/inst_img.jpg")
en_juego = pygame.image.load("Juego/imagenes/en_juego.png")
#imagenes ARTICULOS
articulos = pygame.image.load("Juego/imagenes/articulos.jpg")
agua_img = pygame.image.load("Juego/imagenes/agua_img.jpg")
agua_img2 = pygame.image.load("Juego/imagenes/agua_img2.jpg")
leche_img = pygame.image.load("Juego/imagenes/leche_img.jpg")
leche_img2 = pygame.image.load("Juego/imagenes/leche_img2.jpg")
platanos_img = pygame.image.load("Juego/imagenes/platanos_img.jpg")
platanos_img2 = pygame.image.load("Juego/imagenes/platanos_img2.jpg")
zanahoria_img = pygame.image.load("Juego/imagenes/zanahoria_img.jpg")
zanahoria_img2 = pygame.image.load("Juego/imagenes/zanahoria_img2.jpg")
cereal_img = pygame.image.load("Juego/imagenes/cereal_img.jpg")
cereal_img2 = pygame.image.load("Juego/imagenes/cereal_img2.jpg")
huevos_img = pygame.image.load("Juego/imagenes/huevos_img.jpg")
huevos_img2 = pygame.image.load("Juego/imagenes/huevos_img2.jpg")

#IMAGENES EN JUEGO
enjuego = pygame.image.load("Juego/imagenes/enjuego.jpg")

#Musica de fondo
pygame.mixer.music.load("Juego/Musica/Zelda.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
####MODO####
contrarreloj = 0
#funcion para pintar botones
def pintar_boton(PANTALLA,boton,palabra,color,sombra):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(PANTALLA,sombra,boton,0)
    else:
        draw.rect(PANTALLA,color,boton,0)
    texto = letra.render(palabra, True,(Constantes.BLANCO))
    PANTALLA.blit(texto,(boton.x+(boton.width-texto.get_width())/2,boton.y+(boton.height-texto.get_height())/2))

####FUNCION DE MENU PRINCIPAL####
def Menu_principal():
    while True:
        PANTALLA.blit(fondo,(0,0))

        #BOTONES DE MENU PRINCIPAL
        jugar = Rect(405,480,180,60)
        salir = Rect(415,550,160,40)
        sound = Rect(10,10,50,50)
        mute = Rect(10,70,50,50)
        
        #BOTON JUGAR MENU PRINCIPAL
        pintar_boton(PANTALLA,jugar,"JUGAR",(70,189,34),(38,99,19))
        draw.rect(PANTALLA,Constantes.NEGRO,mute,1)
        PANTALLA.blit(mute_img,(10,70))

        draw.rect(PANTALLA,Constantes.NEGRO,sound,1)
        PANTALLA.blit(sound_img,(10,10))
        #BOTON SALIR MENU PRINCIPAL
        if salir.collidepoint(mouse.get_pos()):
            draw.rect(PANTALLA,(162,3,3),salir,0)
        else:
            draw.rect(PANTALLA,(Constantes.ROJO),salir,0)
        texto = letra.render("SALIR", True,(Constantes.BLANCO))
        PANTALLA.blit(texto,(salir.x+(salir.width-texto.get_width())/2,salir.y+(salir.height-texto.get_height())/2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if jugar.collidepoint(mouse.get_pos()):
                    Menu_modos()
                if salir.collidepoint(mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
                if mute.collidepoint(mouse.get_pos()):
                    pygame.mixer.music.set_volume(0.0)
                if sound.collidepoint(mouse.get_pos()):
                    pygame.mixer.music.set_volume(0.2)

        pygame.display.update()

####FUNCION DE MENU DE MODOS####
def Menu_modos():
    while True:
        PANTALLA.blit(modos,(-200,0))
        texto = letra.render("SELECCIONE LA OPCION QUE DESEE", True,(Constantes.BLANCO))
        PANTALLA.blit(texto,(220,70))
        
        normal = Rect(250,370,200,70)
        contrarreloj = Rect(522,370,260,70)
        instrucciones = Rect(350,600,300,70)
        back = Rect(30,700,160,70)

        pintar_boton(PANTALLA,normal,"NORMAL",(70,189,34),(38,99,19))
        PANTALLA.blit(normal_img,(250,150))
        pintar_boton(PANTALLA,contrarreloj,"CONTRARRELOJ",(242,121,6),(165,88,16))
        PANTALLA.blit(contrarreloj_img,(550,150))
        pintar_boton(PANTALLA,instrucciones,"INSTRUCCIONES",(41,148,205),(39,133,183))
        pintar_boton(PANTALLA,back,"REGRESAR",(70,189,34),(38,99,19))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if normal.collidepoint(mouse.get_pos()):
                    Lista_de_articulos_norm()
                if contrarreloj.collidepoint(mouse.get_pos()):
                    Lista_de_articulos_cont()
                if instrucciones.collidepoint(mouse.get_pos()):
                    Instrucciones()
                if back.collidepoint(mouse.get_pos()):
                    Menu_principal()

        pygame.display.update()

####FUNCION DE MODO NORMAL DE JUEGO####
def Modo_normal():
    agua = 15
    huevos = 30
    zanahorias = 25
    platanos = 20
    cereal = 50
    leche = 40
    
    art = [agua,huevos,zanahorias,cereal,leche,platanos]
    PANTALLA.blit(enjuego,(-30,0))
    score = 0
    i=0
    while i<10:
        variacion = random.randint(1,10)
        obj1 = random.choice(art)
        obj2 = random.choice(art)
        obj3 = random.choice(art)
        res = obj1+obj2
        res2 = obj1+obj2+obj3
        nores1 = res + variacion
        nores2 = res - variacion
        correcto = random.randint(1,2)
        band = True
        while band:
            if i<5:
                PANTALLA.blit(enjuego,(-30,0))
                texto = letrag.render(f"NIVEL {i+1}", True,(Constantes.NEGRO))
                PANTALLA.blit(texto,(380,30))
                opc1 = Rect(150,600,300,100) 
                opc2 = Rect(550,600,300,100)

                puntua = letrach.render("PUNTUACION =", True,(Constantes.NEGRO))
                PANTALLA.blit(puntua,(10,10))
                puntua_num = letra.render(str(score), True,(Constantes.NEGRO))
                PANTALLA.blit(puntua_num,(190,8))
                suma = letrag.render("SUMALOS", True,(Constantes.NEGRO))
                PANTALLA.blit(suma,(380,500))

                if obj1 == 15:
                    PANTALLA.blit(agua_img2,(225,200))
                elif obj1 == 30:
                    PANTALLA.blit(huevos_img2,(150,250))
                elif obj1 == 25:
                    PANTALLA.blit(zanahoria_img2,(150,250))
                elif obj1 == 20:
                    PANTALLA.blit(platanos_img2,(200,200))
                elif obj1 == 50:
                    PANTALLA.blit(cereal_img2,(200,200))
                elif obj1 == 40:
                    PANTALLA.blit(leche_img2,(225,200))


                if obj2 == 15:
                    PANTALLA.blit(agua_img2,(725,200))
                elif obj2 == 30:
                    PANTALLA.blit(huevos_img2,(550,250))
                elif obj2 == 25:
                    PANTALLA.blit(zanahoria_img2,(550,250))
                elif obj2 == 20:
                    PANTALLA.blit(platanos_img2,(550,200))
                elif obj2 == 50:
                    PANTALLA.blit(cereal_img2,(600,200))
                elif obj2 == 40:
                    PANTALLA.blit(leche_img2,(650,200))

                
                
                if correcto == 1:
                    pintar_boton(PANTALLA,opc1,str(res),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores1),(70,189,34),(38,99,19))
                    
                elif correcto == 2:
                    pintar_boton(PANTALLA,opc2,str(res),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if opc1.collidepoint(mouse.get_pos()):
                            if correcto == 1:
                                texto = letrag.render("CORRECTO!!!", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(380,500))
                                score += 50
                                band = False
                            elif correcto == 2:
                                texto = letrag.render("INCORRECTO", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(375,500))
                                band = False
                        if opc2.collidepoint(mouse.get_pos()):
                            if correcto == 2:
                                texto = letrag.render("CORRECTO!!!", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(380,500))
                                score += 50
                                band = False
                            elif correcto == 1:
                                texto = letrag.render("INCORRECTO", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(375,500))
                                band = False
            else:
                PANTALLA.blit(enjuego,(-30,0))
                texto = letrag.render(f"NIVEL {i+1}", True,(Constantes.NEGRO))
                PANTALLA.blit(texto,(380,30))
                opc1 = Rect(150,600,200,100) 
                opc2 = Rect(400,600,200,100)
                opc3 = Rect(650,600,200,100)

                puntua = letrach.render("PUNTUACION =", True,(Constantes.NEGRO))
                PANTALLA.blit(puntua,(10,10))
                puntua_num = letra.render(str(score), True,(Constantes.NEGRO))
                PANTALLA.blit(puntua_num,(190,8))
                suma = letrag.render("SUMALOS", True,(Constantes.NEGRO))
                PANTALLA.blit(suma,(380,500))

                if obj1 == 15:
                    PANTALLA.blit(agua_img2,(100,200))
                elif obj1 == 30:
                    PANTALLA.blit(huevos_img2,(50,250))
                elif obj1 == 25:
                    PANTALLA.blit(zanahoria_img2,(50,250))
                elif obj1 == 20:
                    PANTALLA.blit(platanos_img2,(50,200))
                elif obj1 == 50:
                    PANTALLA.blit(cereal_img2,(70,200))
                elif obj1 == 40:
                    PANTALLA.blit(leche_img2,(100,200))

                if obj2 == 15:
                    PANTALLA.blit(agua_img2,(450,200))
                elif obj2 == 30:
                    PANTALLA.blit(huevos_img2,(360,250))
                elif obj2 == 25:
                    PANTALLA.blit(zanahoria_img2,(380,250))
                elif obj2 == 20:
                    PANTALLA.blit(platanos_img2,(410,200))
                elif obj2 == 50:
                    PANTALLA.blit(cereal_img2,(400,200))
                elif obj2 == 40:
                    PANTALLA.blit(leche_img2,(450,200))

                if obj3 == 15:
                    PANTALLA.blit(agua_img2,(800,200))
                elif obj3 == 30:
                    PANTALLA.blit(huevos_img2,(680,250))
                elif obj3 == 25:
                    PANTALLA.blit(zanahoria_img2,(700,250))
                elif obj3 == 20:
                    PANTALLA.blit(platanos_img2,(700,200))
                elif obj3 == 50:
                    PANTALLA.blit(cereal_img2,(700,200))
                elif obj3 == 40:
                    PANTALLA.blit(leche_img2,(700,200))

                
                
                if correcto == 1:
                    pintar_boton(PANTALLA,opc1,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc3,str(nores2),(70,189,34),(38,99,19))
                    
                elif correcto == 2:
                    pintar_boton(PANTALLA,opc2,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc3,str(nores2),(70,189,34),(38,99,19))

                elif correcto == 3:
                    pintar_boton(PANTALLA,opc3,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores2),(70,189,34),(38,99,19))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if opc1.collidepoint(mouse.get_pos()):
                            if correcto == 1:
                                score += 50
                                band = False
                            elif correcto == 2:
                                band = False
                            elif correcto == 3:
                                band = False
                        if opc2.collidepoint(mouse.get_pos()):
                            if correcto == 2:
                                score += 50
                                band = False
                            elif correcto == 1:
                                band = False
                            elif correcto == 3:
                                band = False
                        if opc3.collidepoint(mouse.get_pos()):
                            if correcto == 3:
                                score += 50
                                band = False
                            elif correcto == 1:
                                band = False
                            elif correcto == 2:
                                band = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
        i+=1
        if i == 10:
            puntuacion(score)
####FUNCION DE MODO CONTRARRELOJ DEL JUEGO####
def Modo_contrarreloj():
    agua = 15
    huevos = 30
    zanahorias = 25
    platanos = 20
    cereal = 50
    leche = 40
    art = [agua,huevos,zanahorias,cereal,leche,platanos]
    PANTALLA.blit(enjuego,(-30,0))
    score = 0
    i=0
    clock = pygame.time.Clock()
    while i<10:
        variacion = random.randint(1,10)
        obj1 = random.choice(art)
        obj2 = random.choice(art)
        obj3 = random.choice(art)
        res = obj1+obj2
        res2 = obj1+obj2+obj3
        nores1 = res + variacion
        nores2 = res - variacion
        correcto = random.randint(1,2)
        limite = 2000
        segundos = 20
        band = True
        while band:
            if i<5:
                PANTALLA.blit(enjuego,(-30,0))
                texto = letrag.render(f"NIVEL {i+1}", True,(Constantes.NEGRO))
                PANTALLA.blit(texto,(380,30))
                opc1 = Rect(150,600,300,100) 
                opc2 = Rect(550,600,300,100)

                puntua = letrach.render("PUNTUACION =", True,(Constantes.NEGRO))
                PANTALLA.blit(puntua,(10,10))
                puntua_num = letra.render(str(score), True,(Constantes.NEGRO))
                PANTALLA.blit(puntua_num,(190,8))
                suma = letrag.render("SUMALOS", True,(Constantes.NEGRO))
                PANTALLA.blit(suma,(380,500))

                if obj1 == 15:
                    PANTALLA.blit(agua_img2,(225,200))
                elif obj1 == 30:
                    PANTALLA.blit(huevos_img2,(150,250))
                elif obj1 == 25:
                    PANTALLA.blit(zanahoria_img2,(150,250))
                elif obj1 == 20:
                    PANTALLA.blit(platanos_img2,(200,200))
                elif obj1 == 50:
                    PANTALLA.blit(cereal_img2,(200,200))
                elif obj1 == 40:
                    PANTALLA.blit(leche_img2,(225,200))


                if obj2 == 15:
                    PANTALLA.blit(agua_img2,(725,200))
                elif obj2 == 30:
                    PANTALLA.blit(huevos_img2,(550,250))
                elif obj2 == 25:
                    PANTALLA.blit(zanahoria_img2,(550,250))
                elif obj2 == 20:
                    PANTALLA.blit(platanos_img2,(550,200))
                elif obj2 == 50:
                    PANTALLA.blit(cereal_img2,(600,200))
                elif obj2 == 40:
                    PANTALLA.blit(leche_img2,(650,200))

                
                
                if correcto == 1:
                    pintar_boton(PANTALLA,opc1,str(res),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores1),(70,189,34),(38,99,19))
                    
                elif correcto == 2:
                    pintar_boton(PANTALLA,opc2,str(res),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                   
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if opc1.collidepoint(mouse.get_pos()):
                            if correcto == 1:
                                texto = letrag.render("CORRECTO!!!", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(380,500))
                                score += 50
                                band = False
                            elif correcto == 2:
                                texto = letrag.render("INCORRECTO", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(375,500))
                                band = False
                        if opc2.collidepoint(mouse.get_pos()):
                            if correcto == 2:
                                texto = letrag.render("CORRECTO!!!", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(380,500))
                                score += 50
                                band = False
                            elif correcto == 1:
                                texto = letrag.render("INCORRECTO", True,(Constantes.NEGRO))
                                PANTALLA.blit(texto,(375,500))
                                band = False
            else:
                PANTALLA.blit(enjuego,(-30,0))
                texto = letrag.render(f"NIVEL {i+1}", True,(Constantes.NEGRO))
                PANTALLA.blit(texto,(380,30))
                opc1 = Rect(150,600,200,100) 
                opc2 = Rect(400,600,200,100)
                opc3 = Rect(650,600,200,100)

                puntua = letrach.render("PUNTUACION =", True,(Constantes.NEGRO))
                PANTALLA.blit(puntua,(10,10))
                puntua_num = letra.render(str(score), True,(Constantes.NEGRO))
                PANTALLA.blit(puntua_num,(190,8))
                suma = letrag.render("SUMALOS", True,(Constantes.NEGRO))
                PANTALLA.blit(suma,(380,500))

                if obj1 == 15:
                    PANTALLA.blit(agua_img2,(100,200))
                elif obj1 == 30:
                    PANTALLA.blit(huevos_img2,(50,250))
                elif obj1 == 25:
                    PANTALLA.blit(zanahoria_img2,(50,250))
                elif obj1 == 20:
                    PANTALLA.blit(platanos_img2,(50,200))
                elif obj1 == 50:
                    PANTALLA.blit(cereal_img2,(70,200))
                elif obj1 == 40:
                    PANTALLA.blit(leche_img2,(100,200))

                if obj2 == 15:
                    PANTALLA.blit(agua_img2,(450,200))
                elif obj2 == 30:
                    PANTALLA.blit(huevos_img2,(360,250))
                elif obj2 == 25:
                    PANTALLA.blit(zanahoria_img2,(380,250))
                elif obj2 == 20:
                    PANTALLA.blit(platanos_img2,(410,200))
                elif obj2 == 50:
                    PANTALLA.blit(cereal_img2,(400,200))
                elif obj2 == 40:
                    PANTALLA.blit(leche_img2,(450,200))

                if obj3 == 15:
                    PANTALLA.blit(agua_img2,(800,200))
                elif obj3 == 30:
                    PANTALLA.blit(huevos_img2,(680,250))
                elif obj3 == 25:
                    PANTALLA.blit(zanahoria_img2,(700,250))
                elif obj3 == 20:
                    PANTALLA.blit(platanos_img2,(700,200))
                elif obj3 == 50:
                    PANTALLA.blit(cereal_img2,(700,200))
                elif obj3 == 40:
                    PANTALLA.blit(leche_img2,(700,200))

                
                
                if correcto == 1:
                    pintar_boton(PANTALLA,opc1,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc3,str(nores2),(70,189,34),(38,99,19))
                    
                elif correcto == 2:
                    pintar_boton(PANTALLA,opc2,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc3,str(nores2),(70,189,34),(38,99,19))

                elif correcto == 3:
                    pintar_boton(PANTALLA,opc3,str(res2),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc1,str(nores1),(70,189,34),(38,99,19))
                    pintar_boton(PANTALLA,opc2,str(nores2),(70,189,34),(38,99,19))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        if opc1.collidepoint(mouse.get_pos()):
                            if correcto == 1:
                                score += 50
                                band = False
                            elif correcto == 2:
                                band = False
                            elif correcto == 3:
                                band = False
                        if opc2.collidepoint(mouse.get_pos()):
                            if correcto == 2:
                                score += 50
                                band = False
                            elif correcto == 1:
                                band = False
                            elif correcto == 3:
                                band = False
                        if opc3.collidepoint(mouse.get_pos()):
                            if correcto == 3:
                                score += 50
                                band = False
                            elif correcto == 1:
                                band = False
                            elif correcto == 2:
                                band = False
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            limite -=1
            texto = letrag.render(str(segundos), True,(Constantes.ROJO))
            PANTALLA.blit(texto,(850,50))
            if limite<1900:
                segundos = 19
            if limite<1800:
                segundos = 18
            if limite<1700:
                segundos = 17
            if limite<1600:
                segundos = 16
            if limite<1500:
                segundos = 15
            if limite<1400:
                segundos = 14
            if limite<1300:
                segundos = 13
            if limite<1200:
                segundos = 12
            if limite<1100:
                segundos = 11
            if limite<1000:
                segundos = 10
            if limite<900:
                segundos = 9
            if limite<800:
                segundos = 8
            if limite<700:
                segundos = 7
            if limite<600:
                segundos = 6
            if limite<500:
                segundos = 5
            if limite<400:
                segundos = 4
            if limite<300:
                segundos = 3
            if limite<200:
                segundos = 2
            if limite<100:
                segundos = 1
            if limite <=0:
                Perdiste()
            clock.tick(100)
            pygame.display.update()
        i+=1
        if i == 10:
            puntuacion(score)
####FUNCION DE INSTRUCCIONES####
def Instrucciones():
    inst = "OBSERVE DETENIDAMENTE LA LISTA DE ARTICULOS CON SU RESPECTIVO PRECIO"
    inst2 = "INTENTE MEMORIZAR LOS PRECIOS DE LOS ARTICULOS"
    inst3 = "REALICE LAS SUMATORIAS O MULTIPLICACIONES QUE SE MUESTAN EN PANTALLA" 
    inst4 = "Y SELECCIONE LA RESPUESTA CORRECTA"
    while True:
        PANTALLA.blit(inst_img,(-100,0))
        texto = letrach.render(inst,True,(Constantes.BLANCO))
        PANTALLA.blit(texto,(40,5))
        texto2 = letrach.render(inst2,True,(Constantes.BLANCO))
        PANTALLA.blit(texto2,(150,30))
        texto3 = letrach.render(inst3,True,(Constantes.BLANCO))
        PANTALLA.blit(texto3,(30,400))
        texto4 = letrach.render(inst4,True,(Constantes.BLANCO))
        PANTALLA.blit(texto4,(250,430))
        PANTALLA.blit(lista_img,(300,60))
        PANTALLA.blit(en_juego,(300,460))
        back = Rect(30,700,160,70)

        pintar_boton(PANTALLA,back,"REGRESAR",(70,189,34),(38,99,19))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if back.collidepoint(mouse.get_pos()):
                    Menu_modos()
        pygame.display.update()  

def Lista_de_articulos_norm():
    while True:
        PANTALLA.blit(articulos,(-200,0))
        texto = letra2.render("ARTICULOS A LA VENTA", True,(Constantes.BLANCO))
        articulos_cuadro = Rect(280,50,450,50)
        draw.rect(PANTALLA,(191,235,132),articulos_cuadro,0)
        PANTALLA.blit(texto,(300,50))
        
        comenzar = Rect(400,700,200,60)
        pintar_boton(PANTALLA,comenzar,"COMENZAR",(70,189,34),(38,99,19))

        PANTALLA.blit(agua_img,(200,150))
        aguatxt = letra2.render("= 15", True,(Constantes.NEGRO))
        PANTALLA.blit(aguatxt,(255,200))

        PANTALLA.blit(leche_img,(200,350))
        lechetxt = letra2.render("= 40", True,(Constantes.NEGRO))
        PANTALLA.blit(lechetxt,(255,380))

        PANTALLA.blit(huevos_img,(140,550))
        huevostxt = letra2.render("= 30", True,(Constantes.NEGRO))
        PANTALLA.blit(huevostxt,(300,555))

        PANTALLA.blit(cereal_img,(600,150))
        cerealtxt = letra2.render("= 50", True,(Constantes.NEGRO))
        PANTALLA.blit(cerealtxt,(700,200))

        PANTALLA.blit(platanos_img,(600,380))
        platanostxt = letra2.render("= 20", True,(Constantes.NEGRO))
        PANTALLA.blit(platanostxt,(690,400))

        PANTALLA.blit(zanahoria_img,(550,550))
        zanahoriatxt = letra2.render("= 25", True,(Constantes.NEGRO))
        PANTALLA.blit(zanahoriatxt,(750,555))

        back = Rect(30,700,160,70)

        pintar_boton(PANTALLA,back,"REGRESAR",(70,189,34),(38,99,19))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if comenzar.collidepoint(mouse.get_pos()):
                    Modo_normal()
                if back.collidepoint(mouse.get_pos()):
                    Menu_modos()
            pygame.display.update()

def Lista_de_articulos_cont():
    while True:
        PANTALLA.blit(articulos,(-200,0))
        texto = letra2.render("ARTICULOS A LA VENTA", True,(Constantes.BLANCO))
        articulos_cuadro = Rect(280,50,450,50)
        draw.rect(PANTALLA,(191,235,132),articulos_cuadro,0)
        PANTALLA.blit(texto,(300,50))
        
        comenzar = Rect(400,700,200,60)
        pintar_boton(PANTALLA,comenzar,"COMENZAR",(70,189,34),(38,99,19))

        PANTALLA.blit(agua_img,(200,150))
        aguatxt = letra2.render("= 15", True,(Constantes.NEGRO))
        PANTALLA.blit(aguatxt,(255,200))

        PANTALLA.blit(leche_img,(200,350))
        lechetxt = letra2.render("= 40", True,(Constantes.NEGRO))
        PANTALLA.blit(lechetxt,(255,380))

        PANTALLA.blit(huevos_img,(140,550))
        huevostxt = letra2.render("= 30", True,(Constantes.NEGRO))
        PANTALLA.blit(huevostxt,(300,555))

        PANTALLA.blit(cereal_img,(600,150))
        cerealtxt = letra2.render("= 50", True,(Constantes.NEGRO))
        PANTALLA.blit(cerealtxt,(700,200))

        PANTALLA.blit(platanos_img,(600,380))
        platanostxt = letra2.render("= 20", True,(Constantes.NEGRO))
        PANTALLA.blit(platanostxt,(690,400))

        PANTALLA.blit(zanahoria_img,(550,550))
        zanahoriatxt = letra2.render("= 25", True,(Constantes.NEGRO))
        PANTALLA.blit(zanahoriatxt,(750,555))

        back = Rect(30,700,160,70)

        pintar_boton(PANTALLA,back,"REGRESAR",(70,189,34),(38,99,19))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if comenzar.collidepoint(mouse.get_pos()):
                    Modo_contrarreloj()
                if back.collidepoint(mouse.get_pos()):
                    Menu_modos()
        pygame.display.update()
def puntuacion(puntuacion):
    while True:
        PANTALLA.blit(enjuego,(-30,0))

        opc1 = Rect(150,600,300,100) 
        opc2 = Rect(550,600,300,100)

        resultadotxt = letra.render("FELICIDADES TERMINO LOS 10 NIVELES DEL JUEGO", True,(Constantes.NEGRO))
        PANTALLA.blit(resultadotxt,(150,50))

        resultado2txt = letra.render("SU PUNTUACION FUE:", True,(Constantes.NEGRO))
        PANTALLA.blit(resultado2txt,(300,100))

        puntua = letrag.render("PUNTUACION =", True,(Constantes.NEGRO))
        PANTALLA.blit(puntua,(250,400))

        puntua_num = letrag.render(str(puntuacion), True,(Constantes.NEGRO))
        PANTALLA.blit(puntua_num,(650,400))

        pintar_boton(PANTALLA,opc1,"MENU PRINCIPAL",(70,189,34),(38,99,19))
        pintar_boton(PANTALLA,opc2,"MENU MODOS",(70,189,34),(38,99,19))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if opc1.collidepoint(mouse.get_pos()):
                    Menu_principal()
                if opc2.collidepoint(mouse.get_pos()):
                    Menu_modos()
        pygame.display.update()
def Perdiste():
    while True:
        PANTALLA.blit(enjuego,(-30,0))

        opc1 = Rect(150,600,300,100) 
        opc2 = Rect(550,600,300,100)

        resultadotxt = letrag.render("GAME OVER", True,(Constantes.NEGRO))
        PANTALLA.blit(resultadotxt,(350,350))

        resultado2txt = letrach.render("SE TE TERMINO EL TIEMPO COMIENZA DE NUEVO", True,(Constantes.NEGRO))
        PANTALLA.blit(resultado2txt,(200,400))


        pintar_boton(PANTALLA,opc1,"MENU PRINCIPAL",(70,189,34),(38,99,19))
        pintar_boton(PANTALLA,opc2,"MENU MODOS",(70,189,34),(38,99,19))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if opc1.collidepoint(mouse.get_pos()):
                    Menu_principal()
                if opc2.collidepoint(mouse.get_pos()):
                    Menu_modos()
        pygame.display.update()
Menu_principal()
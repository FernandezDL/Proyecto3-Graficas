import pygame
import glm
import math
from pygame.locals import *
from gl import Renderer
from model import Model
from shaders import *

width = 960
height = 540

senMovY = 0.03
senMovX = 0.6
senZoom= 0.5

minHeigth = -2
maxHeigth = 2
minZoom = -5
maxZoom = -16

sewActivate = False

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height), pygame.OPENGL | pygame.DOUBLEBUF)
clock= pygame.time.Clock()

sound = pygame.mixer.Sound("music/ninas_de_instagram.mp3")
sound.play()

rend= Renderer(screen)
rend.setShader(vertex_shader, fragment_shader)

#Modelos 
sewMachineModel = "models/SewingMachine.obj"
sewMachineTexture = "textures/wood.jpg"

cocoModel = "models/coco.obj"
cocoTexture = "textures/cocodrilo.jpg"

turtleModel = "models/turtle.obj"
turtleTexture = "textures/turtle.jpg"

carModel = "models/porsche.obj"
carTexture = "textures/metal.jpg"

model= Model(filename= turtleModel,
             translate= (0,0,-6),
             rotation = (-90, 0, 75),
             scale = (0.3,0.3,0.3)) 
model.loadTexture(turtleTexture) 

rend.ObjActual = model

isRunning= True

while isRunning:
    deltaTime = clock.tick(60)/ 1000
    keys= pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        elif event.type == pygame.MOUSEMOTION:
            movX, movY = event.rel
            
            rend.camPosition.y = max(min(rend.camPosition.y + movY * senMovY, maxHeigth), minHeigth)
            rend.camAngle += movX * senMovX

            if rend.camAngle > 360:
                rend.camAngle -= 360

            elif rend.camAngle < 360:
                rend.camAngle += 360

            rend.camPosition.x = rend.target.x + rend.camRadio * math.sin(rend.camAngle * math.pi / 180)
            rend.camPosition.z = rend.target.z + rend.camRadio * math.cos(rend.camAngle * math.pi / 180)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4: #Rueda arriba
                rend.camPosition.z = max(rend.camPosition.z - senZoom, maxZoom)

            elif event.button == 5: #Rueda abajo
                rend.camPosition.z = min(rend.camPosition.z + senZoom, minZoom)
    
    rend.update()

    #Movimiento del objeto con las teclas
    if not sewActivate:
        if keys[K_d]:
            model.rotation.z += 15 * deltaTime

        elif keys[K_a]:
            model.rotation.z -= 15 * deltaTime
    
    else:
        if keys[K_d]:
            model.rotation.y += 15 * deltaTime

        elif keys[K_a]:
            model.rotation.y -= 15 * deltaTime

    #Cambio de shaders
    if keys[K_1]:
        rend.setShader(vertex_shader, fragment_shader)

    elif keys[K_2]:
        rend.setShader(vertex_shader, pie_shader)
    
    elif keys[K_3]:
        rend.setShader(vertex_shader, siren_shader)

    elif keys[K_4]:
        rend.setShader(vertex_shader, glitch_shader)

    elif keys[K_5]:
        rend.setShader(vertex_shader, mixColors_shader)

    #Cambio de música
    if keys[K_x]:
        sound.stop()
        sound = pygame.mixer.Sound("music/ni_me_debes_ni_te_debo.mp3")
        sound.play()

    elif keys[K_z]:
        sound.stop()
        sound = pygame.mixer.Sound("music/ninas_de_instagram.mp3")
        sound.play()

    elif keys[K_c]:
        sound.stop()
        sound = pygame.mixer.Sound("music/conteo_regresivo.mp3")
        sound.play()

    elif keys[K_v]:
        sound.stop()
        sound = pygame.mixer.Sound("music/adios_adios.mp3")
        sound.play()

    #Cambio de modelos
    if keys[K_i]:
        model= Model(filename= cocoModel,
                     translate= (0, 0, -6),
                     rotation= (-90, 0, 75),
                     scale= (0.03, 0.03, 0.03))
        model.loadTexture(cocoTexture)
        rend.changeModel(model)

    elif keys[K_u]:
        model= Model(filename= sewMachineModel,
                     translate= (0, 0, -6),
                     rotation= (0, 90, 0),
                     scale= (4.5, 4.5, 4.5))
        model.loadTexture(sewMachineTexture)
        rend.changeModel(model)
        sewActivate= True

    elif keys[K_y]:
        model= Model(filename= carModel,
                     translate= (0, 0, -6),
                     rotation= (0, 90, 0),
                     scale= (0.5, 0.5, 0.5))
        model.loadTexture(carTexture)
        rend.changeModel(model)

    elif keys[K_t]:
        model= Model(filename= turtleModel,
                     translate= (0, 0, -6),
                     rotation= (0, 90, 0),
                     scale= (0.8, 0.8, 0.8))
        model.loadTexture(turtleModel)
        rend.changeModel(model)

    rend.render()
    pygame.display.flip()

pygame.quit()
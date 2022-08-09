import turtle
import time
import random

score = 0
highScore = 0

# Definicion de ventana
ventana = turtle.Screen() 
ventana.title("Snake game")
ventana.setup(width= 600, height= 600)
ventana.bgcolor("black")
ventana.tracer()

# Cabeza serpiente
cabeza = turtle.Turtle() 
cabeza.color("green")
cabeza.speed(0) 
cabeza.shape("square") 
cabeza.penup() 
cabeza.goto(0,0) 
cabeza.direction = "stop" 

# Cuerpo
cuerpo = []

# Comida
comida = turtle.Turtle() 
comida.color("red")
comida.speed(0) 
comida.shape("circle") 
comida.penup() 
comida.goto(random.randint(-280,280),random.randint(-280,280)) 
comida.direction = "stop" 

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0,260)
marcador.write("Score: 0    High Score: 0", align = "center", font= ('Courier', 24, 'italic'))

# Movimiento de la cabeza
def movimientoCabeza():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    elif cabeza.direction == "down":
        y = cabeza.ycor() 
        cabeza.sety(y - 20)
    elif cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    elif cabeza.direction == "right": # Si la direccion es hacia der mueve el cuadrado en el eje y hacia der   
        x = cabeza.xcor()
        cabeza.setx(x + 20)
    else:
        cabeza.direccion = "stop"

def arriba():
    cabeza.direction = "up"

def abajo():
    cabeza.direction = "down"

def izquierda():
    cabeza.direction = "left"

def derecha():
    cabeza.direction = "right"

def pausa():
    cabeza.direction = "stop"

# Movimiento del cuerpo
def movimientoCuerpo():
    global cuerpo
    global cabeza
    for i in range(len(cuerpo)-1,0,-1):
      cuerpo[i].goto(cuerpo[i-1].xcor(),cuerpo[i-1].ycor())
    if len(cuerpo) > 0: 
      cuerpo[0].goto(cabeza.xcor(),cabeza.ycor())
    
# Detectar teclado 
ventana.listen()
ventana.onkeypress(arriba,"w")
ventana.onkeypress(abajo,"s")
ventana.onkeypress(derecha,"d")
ventana.onkeypress(izquierda,"a")
ventana.onkeypress(pausa,"space")

# Detectar colision
def colision(objeto):
    if cabeza.distance(objeto) < 20:
        return True
    else:
        return False

def colisionBorde():
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        return True
    return False

# Comer
def comer():
    comida.goto(random.randint(-280,280),random.randint(-280,280)) 

# Actualizo marcador
def anotar():
    global score
    global highScore
    score = score + 1
    if score > highScore:
        highScore = score
    marcador.clear()
    marcador.write("Score: {}    High Score: {}".format(score,highScore), align = "center", font= ('Courier', 24, 'italic'))

# Crecer
def crecer():
    # Genero la nueva parte
    parte = turtle.Turtle() 
    parte.color("green")
    parte.speed(30) 
    parte.shape("square") 
    parte.penup()
    # Agrego al cuerpo 
    cuerpo.append(parte)

#Reiniciar juego
def morir():
    time.sleep(1)
    cabeza.goto(0,0)
    cabeza.direction = "stop"
    global cuerpo
    for i in cuerpo:
        i.hideturtle() 
    cuerpo.clear() 
    global score 
    score = 0
    marcador.clear()
    marcador.write("Score: {}    High Score: {}".format(score,highScore), align = "center", font= ('Courier', 24, 'italic'))

# Jugar
while True:

    # Actualizar ventana 
    ventana.update()
    
    # Comer serpiente
    if colision(comida):
        comer()
        anotar()
        crecer()

    # Movimiento serpiente  
    movimientoCabeza()
    time.sleep(0.1)
    if len(cuerpo) > 0:
        movimientoCuerpo()

    # Check Perder
    if colisionBorde():
        morir()
    for i in range(1,len(cuerpo)-1):
        if colision(cuerpo[i]):
            morir()
            break

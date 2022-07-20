import turtle
import time
import random

score = 0
highScore = 0

# Definimos ventana
ventana = turtle.Screen() # Crea una ventana 
ventana.title("Snake game") # Cambia el titulo de la ventana
ventana.setup(width= 600, height= 600) # Cambia el tamaño de la ventana
ventana.bgcolor("black") # Cambia el color de la ventana
ventana.tracer()

# Cabeza serpiente
cabeza = turtle.Turtle() # Creamos un objeto turtle
cabeza.color("green")
cabeza.speed(0) # Para que no tome velocidad el objeto y ya este pintado en la pantalla cuando se inicie
cabeza.shape("square") # Para que tenga forma de cuadrado
cabeza.penup() # Para que no deje una linea mientras se mueve
cabeza.goto(0,0) # Para que inicie desde el centro
cabeza.direction = "stop" # Para que inicie frenado

# Cuerpo
cuerpo = []

# Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle() # Para ocultar la pluma
marcador.goto(0,260)
marcador.write("Score: 0    High Score: 0", align = "center")

# Comida 
comida = turtle.Turtle() # Creamos un objeto turtle
comida.speed(0) # Para que no tome velocidad el objeto
comida.color("red")
comida.shape("circle") # Para que tenga forma de cuadrado
comida.penup() # Para que no deje una linea 
comida.goto(random.randint(-280,280),random.randint(-280,280)) # Para que inicie en un lugar random

# Movimiento de la serpiente
def movimiento():
    if cabeza.direction == "up": # Si la direccion es hacia arriba mueve el cuadrado en el eje y hacia arriba
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down": # Si la direccion es hacia abajo mueve el cuadrado en el eje y hacia abajo
        y = cabeza.ycor() 
        cabeza.sety(y - 20)

    if cabeza.direction == "left": # Si la direccion es hacia izq mueve el cuadrado en el eje x hacia izq
        x = cabeza.xcor()
        cabeza.setx(x - 20)
        
    if cabeza.direction == "right": # Si la direccion es hacia der mueve el cuadrado en el eje y hacia der   
        x = cabeza.xcor()
        cabeza.setx(x + 20)

def arriba(): # se encarga de actualizar el valor de direction cuando se pulsta una tecla
    cabeza.direction = "up"

def abajo(): # se encarga de actualizar el valor de direction cuando se pulsta una tecla
    cabeza.direction = "down"

def izquierda(): # se encarga de actualizar el valor de direction cuando se pulsta una tecla
    cabeza.direction = "left"

def derecha(): # se encarga de actualizar el valor de direction cuando se pulsta una tecla
    cabeza.direction = "right"

def parar(): # se encarga de actualizar el valor de direction cuando se pulsta una tecla
    cabeza.direction = "stop"

# Lectura de teclado
ventana.listen() # Pone a la ventana en modo lectura por teclado
ventana.onkeypress(arriba,"w") # Cuando pulsa la tecla, llama a la funcion que actualiza la direccion
ventana.onkeypress(abajo,"s") # Cuando pulsa la tecla, llama a la funcion que actualiza la direccion
ventana.onkeypress(derecha,"d") # Cuando pulsa la tecla, llama a la funcion que actualiza la direccion
ventana.onkeypress(izquierda,"a") # Cuando pulsa la tecla, llama a la funcion que actualiza la direccion
ventana.onkeypress(parar,"space") # Cuando pulsa la tecla, llama a la funcion que actualiza la direccion

# Jugar
while True: # Que se ejecute siempre hasta que yo decida frenarlo

    ventana.update() # Actualiza la ventana constanmente

    # Si sucede una colision con el borde se detiene el juego y vuelve a iniciar
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
      time.sleep(1)
      # Reincio la cabeza de la serpiente y la detengo
      cabeza.goto(0,0)
      cabeza.direction = "stop"
      # Borro el cuerpo
      for i in cuerpo:
        i.hideturtle() 
      cuerpo.clear() 
      # Reinicio el marcador
      score = 0
      marcador.clear()
      marcador.write("Score: {}    High Score: {}".format(score,highScore), align = "center")

    for i in cuerpo:
        if cabeza.distance(i) < 20:
          time.sleep(1)
          # Reincio la cabeza de la serpiente y la detengo
          cabeza.goto(0,0)
          cabeza.direction = "stop"
          # Borro el cuerpo
          for i in cuerpo:
            i.hideturtle() 
          cuerpo.clear() 
          # Reinicio el marcador
          score = 0
          marcador.clear()
          marcador.write("Score: {}    High Score: {}".format(score,highScore), align = "center")

    if cabeza.distance(comida) < 20: # Si la distancia entre la comida y la serpiente es menor que 20 pixeles
      # Genero una comida en la pantalla
      comida.goto(random.randint(-280,280),random.randint(-280,280)) 
      # Hago crecer a mi serpiente
      parte = turtle.Turtle() 
      parte.color("green")
      parte.speed(30) 
      parte.shape("square") 
      parte.penup() 
      cuerpo.append(parte)
      #aumento mi marcador
      score = score + 1
      #Actualizo mi highscore 
      if score > highScore:
        highScore = score
      #Actualizo mi marcador
      marcador.clear()
      marcador.write("Score: {}    High Score: {}".format(score,highScore), align = "center")

    #mover el cuerpo
    for i in range(len(cuerpo)-1,0,-1):
      cuerpo[i].goto(cuerpo[i-1].xcor(),cuerpo[i-1].ycor())
    if len(cuerpo) > 0: 
      cuerpo[0].goto(cabeza.xcor(),cabeza.ycor())
    #Llama a la funcion mover para mover la cabeza que al presionar una tecla mueva
    movimiento() 
    time.sleep(0.1)
import pygame,random

# Definicion de constantes
RED = (255,0,0)
MEDIO_VERDE = (60,179,113)
MAR_VERDE = (46,139,87)
WHITE = (255,255,255)
BLACK = (0,0,0)
SIZE_SCREEN = (720, 720)
SPEED = 3

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("apple.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image,(APPLE_WIDTH,APPLE_HEIGHT))
        self.rect = self.image.get_rect()
        self.setCoord()

    def setCoord(self):
        self.rect.x = random.randrange(10,SIZE_SCREEN[0]-10)
        self.rect.y = random.randrange(10,SIZE_SCREEN[1]-10)

class Head(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.name = "head"
        self.image = pygame.image.load("snake_head.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image,(SNAKE_HEAD_WIDTH,SNAKE_HEAD_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = 310
        self.rect.y = 310
        self.direction = 4 # 4 = no move; 0 = izq; 1 = abj; 2 = der; 3 = arr;
        self.correct_move = [1,2,1,0] # [izq,abj,der,arr] Indica cuales son los posibles movimioentos para la cabeza
        self.move = "abajo"  
        self.angle_image = "abajo" # Indica el angulo de la imagen
        self.choco = False # Indica que la cabeza choco con el borde False= no choco; True= choco

    def checkMove(self, num):
        # Retorna si es posible moverse en esa direccion
        if self.correct_move[num] == 1 or self.correct_move[num] == 2:
            return True
        return False

    def updateMove(self):
        # Actualiza a donde es posible que se mueva 
        if self.direction == 0: #Se movio a la izquierda
            self.correct_move[0] = 2
            self.correct_move[1] = 1
            self.correct_move[2] = 0
            self.correct_move[3] = 1
            self.move = "izquierda"
        if self.direction == 1: #Se movio a la abajo
            self.correct_move[0] = 1
            self.correct_move[1] = 2
            self.correct_move[2] = 1
            self.correct_move[3] = 0
            self.move = "abajo"
        if self.direction == 2: #Se movio a la derecha
            self.correct_move[0] = 0
            self.correct_move[1] = 1
            self.correct_move[2] = 2
            self.correct_move[3] = 1
            self.move = "derecha"
        if self.direction == 3: #Se movio a la arriba
            self.correct_move[0] = 1
            self.correct_move[1] = 0
            self.correct_move[2] = 1
            self.correct_move[3] = 2
            self.move = "arriba"

    def getAngle(self):
        # Devuelve el angulo al que deberia moverse la imagen
        if self.angle_image == self.move:
            return 0
        if self.angle_image == "abajo":
            if self.move == "izquierda":
                return -90
            elif self.move == "derecha":
                return 90
        if self.angle_image == "arriba":
            if self.move == "izquierda":
                return 90
            elif self.move == "derecha":
                return -90
        if self.angle_image == "izquierda":
            if self.move == "abajo":
                return 90
            elif self.move == "arriba":
                return -90
        if self.angle_image == "derecha":
            if self.move == "abajo":
                return -90
            elif self.move == "arriba":
                return 90

    def checkBorder(self):
        #Checkea si la cabeza no se choco con el borde de la pantalla
        if (self.rect.x >= 0) and (self.rect.x <= 675):
            if (self.rect.y >= 0) and (self.rect.y <= 675):     
                return False
        return True

    def rotateImage(self,direccion):
        # Se encarga de set el angulo de la imagen y rotarla en caso de ser necesario
        if self.angle_image != direccion:
                self.image = pygame.transform.rotate(self.image,self.getAngle())
                self.angle_image = direccion
    
    def update(self):
        #Actualiza el movimiento de la serpiente
        self.updateMove()
        if self.direction == 0: 
            self.rotateImage("izquierda")
            self.rect.x -= SPEED
            self.rect.y = self.rect.y
        if self.direction == 1: 
            self.rotateImage("abajo")
            self.rect.x = self.rect.x
            self.rect.y += SPEED
        if self.direction == 2: 
            self.rotateImage("derecha")
            self.rect.x += SPEED
            self.rect.y = self.rect.y
        if self.direction == 3: 
            self.rotateImage("arriba")
            self.rect.x = self.rect.x
            self.rect.y -= SPEED
        self.choco = self.checkBorder()

class Body(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("snake_body_v2.png").convert_alpha()
        self.rect = self.image.get_rect()   

    def setRectX(self,coord):
        self.rect.x = coord

    def setRectY(self,coord):
        self.rect.y = coord

    def update(self):
        pass

class Game(object): 
    def __init__(self):
        # Inicializo el juego
        self.all_sprite = pygame.sprite.Group()
        self.body = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.head = Head()
        self.body.add(self.head)
        self.all_sprite.add(self.head)
        f = Food()
        self.food.add(f)
        self.all_sprite.add(f)

    def processEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if (self.head.checkMove(0)):
                        self.head.direction = 0
                if event.key == pygame.K_s:
                    if (self.head.checkMove(1)):
                        self.head.direction = 1
                if event.key == pygame.K_d:
                    if (self.head.checkMove(2)):
                        self.head.direction = 2
                if event.key == pygame.K_w:
                    if (self.head.checkMove(3)):
                        self.head.direction = 3
        if self.head.choco:
           return True
        return False

    def updateSpriteList(self):
        # Se encarga de eliminar la comida que se comio de las listas
        for elemnt in self.food:
            self.all_sprite.remove(elemnt)
            self.food.remove(elemnt)

    def addBodyPart(self):
        i = 0
        j = len(self.body) - 1
        new_part = Body()
        for element in self.body:
            if i == j:
                new_part.setRectX(element.rect.x)
                new_part.setRectY(element.rect.y)
            else: 
                i += 1
        self.body.add(new_part)   
        self.all_sprite.add(new_part) 

    def runLogic(self): 
        self.all_sprite.update()
        hit_food = pygame.sprite.spritecollide(self.head, self.food, True)
        if len(hit_food) > 0:
            self.updateSpriteList()
            f = Food()
            self.food.add(f)
            self.all_sprite.add(f)
            self.addBodyPart()
            hit_food.clear()

    def displayFrame(self,screen):
        screen.fill(BLACK)
        self.all_sprite.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE_SCREEN)
    clock = pygame.time.Clock()
    done = False
    game = Game()

    while not done:
        done = game.processEvent()
        game.runLogic()
        game.displayFrame(screen)
        clock.tick(60)

if __name__ == "__main__":
    main()
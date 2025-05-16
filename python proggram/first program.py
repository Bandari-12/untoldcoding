import pygame 
import sys 
import random 

# initilize the game 
pygame. init()

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 20
BALL_SPEED = 4
SHOOT_DELAY = 500

# COLORS 
BLACK =(0,0,0)
WHITE =(255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,255)
ORANGE = (65,255,255)

# LIST OF BUBBLE COLOURS 
BUBBLE_COLOUR = [RED,GREEN,BLUE]

# CREATE THE GAME SCREEN 
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.dispay.set_caption("PUZZLE BUBBLE")

CLOCK  = pygame.time.clock()


class Bubble
    def __init__(self):
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT = BALL_RADIUS
        self.colour = YELLOW
        self.shooting = False 
        self.shooting = False
        self.current_bubble = Bubble(RED, self.X, self.y)
        self.next_bubble_color = random.choice(BUBBLE_COLOUR)


        def shoot(self): 
          self.current_bubble = Bubble(self.next_bubble_colour, self.x, self.y)
          self.next_bbubble_colour =random.choice(BUBBLE_COLOUR)

        def stop_shooting(self)
             self.shooting = False 

        def draw(self):
           self.current_bubble.draw()
           pygame.draw.circle(SCREEN, self.colour,(self.x,self.y+BALL_RADIUS))
           pygame.draw.circle(SCREEN,self.next_bubble_colour,(self.x, self.y +BALL_RADIUS + 2), BALL_RADIUS)

bubbles = []
shooter = shooter()
shoot_time = 0 

def check_collision(bubble, bubble2):
    distance = ((bubble.x - bubble2)  ** 2 + (bubble.y - bubble2.y) ** 2) **0.5
    return distance <= bubble1.radius * 2 

# main game loop 
while True 
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame .K_SPACE:
                if not shooter.shooting and pygame.time.get_tickes() - shoot_time >= SHOOT_DELAY:
                    shooter.shoot()
                    shoot_time = pygame.get_uticks()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.k_LEFT]:
        shooter.x -= BALL_SPEED 
    elif keys[pygame.k_RIGHT]:
        shooter.x += BALL_SPEED

    if shooter.shooting:
        shooter.current_bubble.y_- BALL_SPEED
        if shooter.current_bubble.y <= BALL_RADIUS:
            shooter.stop_shooting()
            bubbles.append(shooter.current_bubble)

    # clear the screen 
    SCREEN.fill(BLACK)

    shooter.draw()

    for bubble in bubbles:
        bubble.draw()
        if shooter.shooting and check_collision(shooter.current_bubble, bubble):
            if shooter.current_bubble.colour == bubble.colour:
                bubbles.remove(bubble)
                shooter.stop_shooting()

pygame.display.flip()
CLOCK.tick(30)


pygame.quit()



  


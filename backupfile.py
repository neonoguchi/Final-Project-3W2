import pygame
import random
import time

#window dimensions
screen_width = 800
screen_height = 600
screen_dimensions = (screen_width,screen_height)

door = pygame.Rect(200, 0, 60, 10)
door_color = 'Red'

class Player():
    def __init__(self, x, y, size, health=100):
        self.size = size
        self.x = x
        self.y = y
        self.color = pygame.Color(0, 210, 0)
        self.health = health
        self.dead = False

    def update(self):
        #checks health for death
        if self.health < 0:
            self.dead = True

    def borders(self):
        if self.y <= 0:
            self.y = 0
        elif self.y >= screen_height:
            self.y = screen_height
        
        if self.x <= 0:
            self.x = 0
        elif self.x >= screen_width:
            self.x = screen_width
    
    def draw(self):
        if self.dead:
            return
        screen_dimensions.blit()

def main():
    pygame.init()
    pygame.display.set_caption("Simple RPG")
    screen = pygame.display.set_mode(screen_dimensions)
    clock = pygame.time.Clock()

    #player constants
    x = 600
    y = 550
    width = 25
    height = 25
    velo = 5
    
    #game loop
    running = True
    while running:

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and y > 0:
            y -= velo
        if keys[pygame.K_a] and x > 0:
            x -= velo
        if keys[pygame.K_s] and y < screen_height - height:
            y += velo
        if keys[pygame.K_d] and x < screen_width - width:
            x += velo
        
        #background fill
        screen.fill((15,30,15))
        
        #player rectangle
        pygame.draw.rect(screen, (0,200,0), (x, y, width, height))
        pygame.draw.rect(screen, door_color, door)
        
        pygame.display.update()
        clock.tick(60) #fps


if __name__ == "__main__":
    main()
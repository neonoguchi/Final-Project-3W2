import pygame
import random

#window dimensions
window_width = 800
window_height = 670
window_dimensions = (window_width, window_height)

#game screen dimensions
screen_width = 800
screen_height = 600
screen_dimensions = (screen_width,screen_height)
screen = pygame.display.set_mode(window_dimensions)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 600
        self.y = 550
        self.size = 32
        self.image = pygame.image.load('images//robot.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.velo = 5
        self.health = 100
        self.max_health = self.health
        self.dead = False

    def update(self):
        #checks for movement
        self._movement()
        #checks if player is alive
        if self.health <= 0:
            self.dead = True
    
    def take_dmg(self, damage):
        self.health -= damage
        self.update()
    
    def _movement(self):
        #wasd movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.velo
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.velo
        if keys[pygame.K_s] and self.rect.y < screen_height - self.size:
            self.rect.y += self.velo
        if keys[pygame.K_d] and self.rect.x < screen_width - self.size:
            self.rect.x += self.velo

        #boundary
        self.rect.x = max(0, min(self.rect.x, screen_width - self.size))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.size))
    
    def draw(self):
        if not self.dead:
            screen.blit(self.image, self.rect)
    
    def draw_health(self):
        #hp bar on player
        current_hp = (self.health / self.max_health) * 100
        pygame.draw.rect(screen, (255,0,0), (self.rect.x - 39, self.rect.y - 15, 100, 5))
        pygame.draw.rect(screen, (0,255,0), (self.rect.x - 39, self.rect.y - 15, current_hp, 5))
        #hp bar on hud
        hud_healthbar_x = 470
        hud_healthbar_y = 620
        hud_healthbar_height = 30
        pygame.draw.rect(screen, (255,0,0), (hud_healthbar_x, hud_healthbar_y, 300, hud_healthbar_height))
        pygame.draw.rect(screen, (0,255,0), (hud_healthbar_x, hud_healthbar_y, current_hp*3, hud_healthbar_height))

class Door():
    def __init__(self, x=200, y=0, width=60, height=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = 'Yellow'
        self.is_open = False
        self.is_unlocked = False
    
    def update(self, player):
        #sound constants
        door_open_sfx = pygame.mixer.Sound("sounds//door_open.mp3")
        door_locked_sfx = pygame.mixer.Sound("sounds//door_locked.mp3")

        #[E] interact with door
        if self.rect.colliderect(player.rect):
            if not self.is_unlocked:
                self.color = ((180,10,10))
                if pygame.key.get_pressed()[pygame.K_e]:
                    door_locked_sfx.play()
                    print("Door locked.")
            elif self.is_unlocked:
                self.color = 'Yellow'
                if pygame.key.get_pressed()[pygame.K_e]:
                    door_open_sfx.play()
                    self.is_open = True
        else:
            self.color = 'Red'

    
    def generate_new_door(self):
        #door locations simplified
        topside = Door(random.randrange(0, screen_width - 60, 60), 0, 60, 10)
        bottomside = Door(random.randrange(0, screen_width - 60, 60), (screen_height - 10), 60, 10)
        leftside = Door(0, random.randrange(0, screen_height, 60), 10, 60)
        rightside = Door((screen_width - 10), random.randrange(0, screen_height, 60), 10, 60)
        return random.choice([topside, bottomside, leftside, rightside])

    def draw(self):
        pygame.draw.rect(screen, pygame.Color(self.color), self.rect)

class Score():
    def __init__(self, level, pos=(20,620)):
        self.level = level
        self.pos = pos
        self.font = pygame.font.Font(None,40)

    def draw(self):
        text = self.font.render(f"Lvl: {self.level}", True, 'White')
        screen.blit(text, self.pos)

class Hostile():
    def __init__(self):
        self.x = 700
        self.y = 300
        self.size = 80
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.color = 'Red'
        self.base_velocity = 1
        self.velocity = self.base_velocity
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self, player, level):
        self._movement(player)
        self._speed(level)
        
        #damage to player
        if self.rect.colliderect(player.rect):
            self.color = 'Blue'
            player.take_dmg(5)
            print(player.health)
        else:
            self.color = 'Red'

    def _speed(self, level):
        if level >= 20:
            self.velocity = self.base_velocity * 3
        elif level >= 15:
            self.velocity = self.base_velocity * 2.75
        elif level >= 10:
            self.velocity = self.base_velocity * 2.5
        elif level >= 5:
            self.velocity = self.base_velocity * 2
            
    def _movement(self, player):
        #boundary
        self.rect.x = max(0, min(self.rect.x, screen_width - self.size))
        self.rect.y = max(0, min(self.rect.y, screen_height - self.size))
        
        #movement of hostile (relativity of center of the hostile and the player)
        if self.rect.centerx < player.rect.centerx:
            self.rect.centerx += self.velocity
        elif self.rect.centerx > player.rect.centerx:
            self.rect.centerx -= self.velocity

        if self.rect.centery < player.rect.centery:
            self.rect.centery += self.velocity
        elif self.rect.centery > player.rect.centery:
            self.rect.centery -= self.velocity

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 32
        self.image = pygame.image.load('images//heart.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.size)
        self.rect.y = random.randrange(screen_height - self.size)
        self.collected = False

    def update(self, player):
        heart_sfx = pygame.mixer.Sound("sounds//heal_sound.mp3")
        
        if self.rect.colliderect(player.rect) and not self.collected:
            player.health = min(100, player.health +  20)
            heart_sfx.play()
            print("+20 HP")
            self.collected = True
            self.kill()

    def draw(self):
        if not self.collected:
            screen.blit(self.image, self.rect)
    
class Key(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = 16
        self.image = pygame.image.load('images//key.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.collected = False

    def update(self, player, door):
        coin_sfx = pygame.mixer.Sound("sounds//key_sound.mp3")
        
        if self.rect.colliderect(player.rect) and not self.collected:
            door.is_unlocked = True
            self.collected = True
            coin_sfx.play()
            print("Key collected!")

    def draw(self):
        if not self.collected:
            screen.blit(self.image, self.rect)  

def generate_level(player, door, hostile, hearts, key):
    #player spawn based off of previous door
    if door.rect.x == 0:
        player.rect.topleft = (screen_width - player.rect.width, door.rect.centery - player.rect.height // 2)
    elif door.rect.x == screen_width - door.rect.width:
        player.rect.topleft = (0, door.rect.centery - player.rect.height // 2)
    elif door.rect.y == 0:
        player.rect.topleft = (door.rect.centerx - player.rect.width // 2, screen_height - player.rect.height)
    elif door.rect.y == screen_height - door.rect.height:
        player.rect.topleft = (door.rect.centerx - player.rect.width // 2, 0)
    
    #door constant (for new levels)
    door.color = 'Yellow'
    door.is_open = False

    #hostile spawns at previous lvl's door
    if player.rect.x == 0:
        hostile.rect.topleft = (screen_width - hostile.rect.width, player.rect.centery - hostile.rect.height // 2)
    elif player.rect.x == screen_width - player.rect.width:
        hostile.rect.topleft = (0, player.rect.centery - hostile.rect.height // 2)
    elif player.rect.y == 0:
        hostile.rect.topleft = (player.rect.centerx - hostile.rect.width // 2, screen_height - hostile.rect.height)
    elif player.rect.y == screen_height - player.rect.height:
        hostile.rect.topleft = (player.rect.centerx - hostile.rect.width // 2, 0)

    #heart spawn location (per lvl)
    heart = Heart()
    heart.rect.x = random.randrange(screen_width - heart.size)
    heart.rect.y = random.randrange(screen_height - heart.size)
    hearts.add(heart)

    #key spawn location (per lvl)
    key.rect.x = random.randrange(screen_width - key.size)
    key.rect.y = random.randrange(screen_height - key.size)

def main():
    pygame.init()
    pygame.display.set_caption("Simple RPG")
    clock = pygame.time.Clock()
    
    level = 1
    score= Score(level)
    high_score = 0

    player = Player()
    door = Door()
    hostile = Hostile()
    # heart = Heart()
    sprites = pygame.sprite.Group()
    key = Key()
    generate_level(player, door, hostile, sprites, key)

    #game loop
    running = True
    while running:
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #GAME OVER
        if player.dead:
            running = False
            if score.level > high_score:
                print(f"New High Score of {score.level}!")
                high_score = score.level
        

        #updates
        player.update()
        door.update(player)
        hostile.update(player, level)
        sprites.update(player)
        key.update(player, door)

        #background fill
        display_bg_color = ((15,30,15))
        console_color = ((60, 60, 60))
        screen.fill(console_color)
        pygame.draw.rect(screen, display_bg_color, (0, 0, screen_width, screen_height))

        #draw
        player.draw()
        player.draw_health()
        door.draw()
        score.draw()
        key.draw()
        # heart.draw()
        sprites.draw(screen)
        hostile.draw()

        if door.is_open:
            
            level += 1
            print(f"Door opened! Transitioning to level {level}")
            score.level = level
            sprites.empty()
            key = Key()
            generate_level(player, door, hostile, sprites, key)
            door = Door.generate_new_door(door)
        
        pygame.display.update()
        clock.tick(60) #fps


if __name__ == "__main__":
    main()
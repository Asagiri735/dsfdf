from pygame import *
from random import randint
window = display.set_mode((700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Racket(GameSprite):
    def update(self):
        if self.rect.x <= 450:
            self.rect_x = 'right'
        if self.rect.y >= - 85:
            self.rect_y = 'left'

class Racket2(GameSprite):
    def update(self):
        self.image = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.rect = pygame.Rect(x,y, w-320, h-375)
        self.rect.x = x
        self.rect.y = y

class Ball(GameSprite):
        def __init__(self, img, x, y, speed_x,speed_y):
            super().__init__(player_image, player_x, player_y, player_width, player_height, player_speed)
            self.speed_x = speed
            self.speed_y = speed
        def update(self):
            if self.rect.y <0 or self.rect_y > 450:
                self.speed_y *= -1
            if self.rect.x < 0 or self.rect_x > 450:
                self.speed_x *= -1
        

background = transform.scale(image.load('Фон пинг понга.webp'),(700,500))


game = True
finish = False
clock = time.Clock()
FPS = 60
x = 3
y = 3

racket = Racket('Ракетка.webp', 260, 400, 60, 100, 10 )
racket2 = Racket2('ракетка 2.jpg', 260, 400, 60, 100, 10 )
ball = Ball('мяч.webp', randint(0,600), -100, 100, 60, 3)

lose = font1.render('Проигрыш', True,(255,0,0))


font.init()
font1 = font.SysFont('Arial', 36)
glasses1 = 0 
glasses2 = 0

while game:
    for ev in pygame.event.get():
        if e.type == QUIT:
            game = False
            
    keys = pygame.key.get_pressed()

    if ball.rect.colliderect(platform.rect):
        y *= -1

    
    if finish != True:
        racket.draw(window)
        racket2.draw(window)
        ball.draw(window)
        window.blit(background,(0 , 0))
        text_losee2 = font1.render('Счет:' +str(glasses2), 1, (255,255,255))
        window.blit(text_losee2,(0, 30))
        text_lose = font1.render('Счет:' + str(glasses1), 1, (255,255,255))
        window.blit(text_lose, (0, 30))

        if sprite.spritecollide(ball, racket, racket2, False) or (lost > 3):
            finish = True
            window.blit(lose,(200,200))
        if sprite.spritecollide(ball, racket, racket2, False):
            finish = True
            window.blit(lose,(200,200))
        if glasses1 > 5:
            finish = False
            window.blit(life,(200,200))
        if glasses2 > 5:
            finish = False
            window.blit(life,(200,200))



    display.update()
    clock.tick(60)

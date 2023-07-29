import pygame
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface
from runner import Runner

FPS = 28
VELOCITY = 7
MASS = 2

class Bullet(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = Surface((20, 20))
        pygame.draw.rect(self.image,
                         Color(255, 0, 0),
                         (0, 0, 20, 20))
        self.rect = self.image.get_rect()

    def update(self):
        if self.rect.x < 0:
            self.rect.x = screen.get_width() # 벽에 닿았을때 처음 위치로 이동
        self.rect.x -= 1 # 속도

    def __init__(self):
        self.image = ""
        self.dx = 0
        self.dy = 0
        self.rect = ""
        self.isjump = 0
        self.v = VELOCITY # 속도
        self.m = MASS # 질량

    def jump(self, j):
        self.isjump = j

    def update(self):
        if self.isjump > 0:
            if self.isjump == 2:
                self.v = VELOCITY
            if self.v > 0:
                F = (0.5 * self.m *(self.v * self.v))
            else:
                F = -(0.5 * self.m * (self.v * self.v))
            self.rect.y -= round(F)
            self.v -= 1
            if self.rect.bottom > WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT
                self.isjump = 0
                self.v = VELOCITY

if __name__ == "__main__":
    pygame.init()

    size = (400, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Runner Animation")

    run = True
    clock = pygame.time.Clock()

    background_img = pygame.image.load("background.png")

    runner1 = Runner()
    runner1.rect.x = 0
    runner1.rect.y =170

    runner2 = Runner()
    runner2.rect.x =130
    runner2.rect.y = 170

    runner3 = Runner()
    runner3.rect.x = 250
    runner3.rect.y = 170

    runner_group = pygame.sprite.Group()
    runner_group.add(runner1)
    runner_group.add(runner2)
    runner_group.add(runner3)

    bullet = Bullet()
    bullet.rect_x = screen.get_width()
    bullet.rect_y = 200

    bullet_group = pygame.sprite.Group()
    bullet_group.add(bullet)

    #게임 루프
    while run:
        # 1) 사용자 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            runner1.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            runner1.rect.x += 5
        elif (keys[pygame.K_SPACE]):
            if runner1.isjump == 2:
                runner1.jump(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        if event.key == pygame.K_SPACE:
            if runner1.isjump == 0:
                runner1.jump(1)
            elif runner1.isjump == 1:
                runner.jump(2)
                
            

        # 2) 게임 상태 업데이트
        runner_group.update()
        bullet_group.update()
        collided = pygame.sprite.groupcollide(
            bullet_group, runner_group, False, True)
        if len(collided.items()) > 0:
            print("남은 Runner 수 : {0}".format(len(runner_group.sprites())))
        
        # 3) 게임 상태 그리기
        screen.blit(background_img, screen.get_rect())
        runner_group.draw(screen)
        bullet_group.draw(screen)
        pygame.display.flip()
        

        clock.tick(FPS)

pygame.quit()

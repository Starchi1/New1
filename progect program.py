import pygame
from random import sample
import time


# Задача лучше проработать классы, исправит баги в коде для стрельбы, приделать пуле картинку и добавить взрывы.
lastMove = 'up'
bonus_variaty = ['red', 'blue', 'yellow']
cords_bonus = [(100, 370), (400, 370), (700, 370)]
a, b, c = sample(bonus_variaty, 3)
a1, b1, c1 = sample(cords_bonus, 3)

bullet_img = pygame.image.load('snaryd.png')

creen_tank_img = [pygame.image.load('tank1.png'), pygame.image.load('tank2.png'), pygame.image.load('tank3.png'),
                  pygame.image.load('tank4.png'), pygame.image.load('tank5.png'), pygame.image.load('tank6.png'),
                  pygame.image.load('tank7.png'), pygame.image.load('tank8.png')]

creen_tank_right_img = [pygame.image.load('tank_right1.png'), pygame.image.load('tank_right2.png'), pygame.image.load('tank_right3.png'),
                  pygame.image.load('tank_right4.png'), pygame.image.load('tank_right5.png'), pygame.image.load('tank_right6.png'),
                  pygame.image.load('tank_right7.png'), pygame.image.load('tank_right8.png')]

creen_tank_laft_img = [pygame.image.load('tank_laft1.png'), pygame.image.load('tank_laft2.png'), pygame.image.load('tank_laft3.png'),
                  pygame.image.load('tank_laft4.png'), pygame.image.load('tank_laft5.png'), pygame.image.load('tank_laft6.png'),
                  pygame.image.load('tank_laft7.png'), pygame.image.load('tank_laft8.png')]

creen_tank_back_img = [pygame.image.load('tank8.png'), pygame.image.load('tank7.png'), pygame.image.load('tank6.png'),
                  pygame.image.load('tank5.png'), pygame.image.load('tank4.png'), pygame.image.load('tank3.png'),
                  pygame.image.load('tank2.png'), pygame.image.load('tank1.png')]

blue_tank_img = [pygame.image.load('tank_blue1.png'), pygame.image.load('tank_blue2.png'), pygame.image.load('tank_blue3.png'),
                 pygame.image.load('tank_blue4.png'), pygame.image.load('tank_blue5.png'), pygame.image.load('tank_blue6.png'),
                 pygame.image.load('tank_blue7.png'), pygame.image.load('tank_blue8.png')]

blue_tank_back_img = [pygame.image.load('tank_blue8.png'), pygame.image.load('tank_blue7.png'), pygame.image.load('tank_blue6.png'),
                 pygame.image.load('tank_blue5.png'), pygame.image.load('tank_blue4.png'), pygame.image.load('tank_blue3.png'),
                 pygame.image.load('tank_blue8.png'), pygame.image.load('tank_blue1.png')]

blue_tank_laft_img = [pygame.image.load('tank_blue_laft1.png'), pygame.image.load('tank_blue_laft2.png'),
                      pygame.image.load('tank_blue_laft3.png'), pygame.image.load('tank_blue_laft4.png'),
                      pygame.image.load('tank_blue_laft5.png'), pygame.image.load('tank_blue_laft6.png'),
                      pygame.image.load('tank_blue_laft7.png'), pygame.image.load('tank_blue_laft8.png')]

blue_tank_right_img = [pygame.image.load('tank_blue_right1.png'), pygame.image.load('tank_blue_right2.png'),
                      pygame.image.load('tank_blue_right3.png'), pygame.image.load('tank_blue_right4.png'),
                      pygame.image.load('tank_blue_right5.png'), pygame.image.load('tank_blue_right6.png'),
                      pygame.image.load('tank_blue_right7.png'), pygame.image.load('tank_blue_right8.png')]

creen_tank_stop_img = [pygame.image.load('tank1.png')]
blue_tank_stop_img = [pygame.image.load('tank_blue1.png')]
img_count = 0


class Bullet:
    def __init__(self, x, y):
        self.x_bul = x
        self.y_bul = y
        self.speed_bul = 8

    def move(self):
        global lastMove
        if lastMove == 'up':
            if self.x_bul > 20 and self.y_bul < 740:
                self.y_bul += self.speed_bul
                screen.blit(bullet_img, (self.x_bul, self.y_bul))
                return True

        elif lastMove == 'down':
            if self.y_bul > 20 and self.y_bul < 740:
                self.y_bul -= self.speed_bul
                screen.blit(bullet_img, (self.x_bul, self.y_bul))
                return True

        elif lastMove == 'left':
            if self.x_bul > 20 and self.y_bul < 740:
                self.x_bul -= self.speed_bul
                screen.blit(bullet_img, (self.x_bul, self.y_bul))
                return True

        elif lastMove == 'right':
            if self.x_bul > 20 and self.y_bul < 731:
                self.x_bul += self.speed_bul
                screen.blit(bullet_img, (self.x_bul, self.y_bul))
                return True

        else:
            return False


class Level(Bullet):
    def __init__(self, screen):
        super(Bullet, self).__init__()
        self.sten = pygame.image.load('стенки.png')
        self.sten2 = pygame.image.load('стенки2.png')
        self.running = True
        self.graniz = True
        self.ed_vper = False
        self.laft = False
        self.right = False
        self.ed_naz = False
        self.stop = False
        self.ed_vper1 = False
        self.laft1 = False
        self.right1 = False
        self.ed_naz1 = False
        self.stop1 = False
        self.clock = pygame.time.Clock()
        self.x = 375
        self.y = 700
        self.x1 = 375
        self.y1 = 100
        self.speed = 0.1
        self.screen = screen
        self.f = False

    def zadershka(self):
        time.sleep(1)
        self.f = True

    def sickl(self):
        global lastMove
        self.sten_verh = self.sten.get_rect(center=(332, -15))
        self.sten_niz = self.sten.get_rect(center=(332, 815))
        self.sten_left = self.sten2.get_rect(center=(-15, 355))
        self.sten_right = self.sten2.get_rect(center=(815, 355))
        self.sten_verh_dal = self.sten.get_rect(center=(532, -15))
        self.sten_niz_dal = self.sten.get_rect(center=(532, 815))
        self.sten_left_dal = self.sten2.get_rect(center=(-15, 555))
        self.sten_right_dal = self.sten2.get_rect(center=(815, 555))
        bullets = []
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_x]:
                bullets.append(Bullet(self.x, self.y))

            for bullet in bullets:
                if not bullet.move():
                    bullets.remove(bullet)

            if keys[pygame.K_LEFT] and self.x > 20:
                if keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
                    if keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
                        self.x -= self.speed
                        lastMove = 'left'
                        self.laft = True
                        self.stop = False
                        self.right = False
                        self.ed_vper = False
                        self.ed_naz = False

            if keys[pygame.K_RIGHT] and self.x < 731:
                if keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
                    if keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
                        self.x += self.speed
                        lastMove = 'right'
                        self.right = True
                        self.stop = False
                        self.ed_vper = False
                        self.ed_naz = False
                        self.laft = False

            if keys[pygame.K_UP] and self.y > 20:
                self.y -= self.speed
                lastMove = 'up'
                self.ed_vper = False
                self.ed_naz = True
                self.stop = False
                self.laft = False
                self.right = False

            if keys[pygame.K_DOWN] and self.y < 740:
                if keys[pygame.K_DOWN] and not keys[pygame.K_LEFT]:
                    if keys[pygame.K_DOWN] and not keys[pygame.K_RIGHT]:
                        self.y += self.speed
                        lastMove = 'down'
                        self.ed_vper = False
                        self.ed_naz = True
                        self.stop = False
                        self.laft = False
                        self.right = False

            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    self.stop = True
                    self.ed_vper = False
                    self.laft = False
                    self.right = False
                    self.ed_naz = False


            if keys[pygame.K_a] and self.x1 > 20:
                if keys[pygame.K_a] and not keys[pygame.K_w]:
                    if keys[pygame.K_a] and not keys[pygame.K_w]:
                        self.x1 -= self.speed
                        lastMove = 'left'
                        self.laft1 = True
                        self.stop1 = False
                        self.right1 = False
                        self.ed_vper1 = False
                        self.ed_naz1 = False

            if keys[pygame.K_d] and self.x1 < 731:
                if keys[pygame.K_d] and not keys[pygame.K_w]:
                    if keys[pygame.K_d] and not keys[pygame.K_s]:
                        self.x1 += self.speed
                        lastMove = 'right'
                        self.right1 = True
                        self.stop1 = False
                        self.ed_vper1 = False
                        self.ed_naz1 = False
                        self.laft1 = False

            if keys[pygame.K_s] and self.y1 > 20:
                self.y1 -= self.speed
                lastMove = 'up'
                self.ed_vper1 = False
                self.ed_naz1 = True
                self.stop1 = False
                self.laft1 = False
                self.right1 = False

            if keys[pygame.K_w] and self.y1 < 740:
                if keys[pygame.K_w] and not keys[pygame.K_a]:
                    if keys[pygame.K_w] and not keys[pygame.K_d]:
                        self.y1 += self.speed
                        lastMove = 'down'
                        self.ed_naz1 = True
                        self.stop1 = False
                        self.ed_vper1 = False
                        self.laft1 = False
                        self.right1 = False

            if not keys[pygame.K_a] and not keys[pygame.K_d]:
                if not keys[pygame.K_w] and not keys[pygame.K_s]:
                    self.stop1 = True
                    self.ed_vper1 = False
                    self.laft1 = False
                    self.right1 = False
                    self.ed_naz1 = False

            self.screen.fill('white')
            random_bonus(self.screen)
            animashin_tank_green(self.screen, self.x, self.y, self.stop,
                                self.ed_vper, self.laft, self.right, self.ed_naz)
            animashin_tank_blue(self.screen, self.x1, self.y1, self.stop1,
                                self.ed_vper1, self.laft1, self.right1, self.ed_naz1)
            self.screen.blit(self.sten, self.sten_verh)
            self.screen.blit(self.sten, self.sten_niz)
            self.screen.blit(self.sten2, self.sten_left)
            self.screen.blit(self.sten2, self.sten_right)
            self.screen.blit(self.sten, self.sten_verh_dal)
            self.screen.blit(self.sten, self.sten_niz_dal)
            self.screen.blit(self.sten2, self.sten_left_dal)
            self.screen.blit(self.sten2, self.sten_right_dal)

            pygame.display.update()
        pygame.quit()


def random_bonus(screen):
    global cooldown
    pygame.draw.circle(screen, a, a1, 20)
    pygame.draw.circle(screen, b, b1, 20)
    pygame.draw.circle(screen, c, c1, 20)


def animashin_tank_green(screen, x, y, stop, ed_vper, laft, right, ed_naz):
    global img_count
    if img_count == 512:
        img_count = 0

    if ed_vper and not stop:
        if not laft and not right and not ed_naz:
            screen.blit(creen_tank_img[img_count // 64], (x, y))
            img_count += 1

    if stop and not ed_vper:
        if not laft and not right and not ed_naz:
            screen.blit(creen_tank_stop_img[0], (x, y))
            img_count += 1

    if laft and not right and not ed_naz:
        if not ed_vper and not stop:
            screen.blit(creen_tank_laft_img[img_count // 64], (x, y))
            img_count += 1

    if right and not laft and not ed_naz:
        if not ed_vper and not stop:
            screen.blit(creen_tank_right_img[img_count // 64], (x, y))
            img_count += 1

    if ed_naz and not right and not laft:
        if not ed_vper and not stop:
            screen.blit(creen_tank_back_img[img_count // 64], (x, y))
            img_count += 1

    if ed_vper and not stop:
        if not laft and not right and not ed_naz:
            screen.blit(creen_tank_img[0], (x, y))
            img_count += 1


def animashin_tank_blue(screen, x, y, stop, ed_vper1, laft1, right1, ed_naz1):
    global img_count
    if img_count == 512:
        img_count = 0

    if ed_vper1 and not stop:
        if not laft1 and not right1 and not ed_naz1:
            screen.blit(blue_tank_img[img_count // 64], (x, y))
            img_count += 1

    if stop and not ed_vper1:
        if not laft1 and not right1 and not ed_naz1:
            screen.blit(blue_tank_stop_img[0], (x, y))
            img_count += 1

    if laft1 and not right1 and not ed_naz1:
        if not ed_vper1 and not stop:
            screen.blit(blue_tank_laft_img[img_count // 64], (x, y))
            img_count += 1

    if right1 and not laft1 and not ed_naz1:
        if not ed_vper1 and not stop:
            screen.blit(blue_tank_right_img[img_count // 64], (x, y))
            img_count += 1

    if ed_naz1 and not right1 and not laft1:
        if not ed_vper1 and not stop:
            screen.blit(blue_tank_back_img[img_count // 64], (x, y))
            img_count += 1

    if ed_vper1 and not stop:
        if not laft1 and not right1 and not ed_naz1:
            screen.blit(blue_tank_img[0], (x, y))
            img_count += 1



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Танки')
    size = width, height = 800, 800
    screen = pygame.display.set_mode(size)
    lv = Level(screen)
    lv.sickl()
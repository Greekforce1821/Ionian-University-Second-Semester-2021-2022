import pygame as pg
import random

pg.font.init()

FPS = 60

WIDTH, HEIGHT = 1000, 750

WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Invaders Ripoff")

# load images
SPACESHIP_IMG = pg.image.load("assets/spaceship_32.png")
ALIEN_IMG = pg.image.load("assets/alien_green_32x23.png")
LASER_BULLET = pg.image.load("assets/lazer_bullet.png")

BIG_ALIEN_IMG = pg.image.load("assets/big_alien.png")
POWER_UP_IMG = pg.image.load("assets/power_up.png")


class Player:
    VELOCITY = 5

    def __init__(self):  # First instantiation of the player
        self.image = SPACESHIP_IMG  # Player Sprite
        self.mask = pg.mask.from_surface(self.image)  # Player mask for collisions
        self.x = int(WIDTH / 2)  # Starting x position
        self.y = HEIGHT - 64  # Starting y position
        self.laser_power = 1
        self.lasers = []  # List of bullets in the screen shot by the player
        self.cooldown_timer = 0
        self.cooldown = 18
        

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        self.cooldown_timer -= 1

    def shoot(self):
        if self.cooldown_timer <= 0:
            new_laser = Laser(self.x + self.image.get_width() / 2, self.y, self.laser_power)
            self.lasers.append(new_laser)
            self.cooldown_timer = self.cooldown

    def move(self, direction):
        if direction == "left":
            self.x -= self.VELOCITY
        elif direction == "right":
            self.x += self.VELOCITY
        elif direction == "up":
            self.y -= self.VELOCITY
        elif direction == "down":
            self.y += self.VELOCITY



    def move_lasers(self, vel, objs_Alien, objs_powrsUp):
        for laser in self.lasers:
            laser.move(vel)
            if outOfScreen(laser):
                self.lasers.remove(laser)
            else:
                for alien in objs_Alien:
                    if checkCollision(laser, alien):
                        alien.hp -= laser.power
                        if alien.hp <= 0:
                            objs_Alien.remove(alien)
                            if random.randint(1, 10) == 1:
                                new_powerup = PowerUp(alien.x, alien.y)
                                objs_powrsUp.append(new_powerup)
                        try:
                            self.lasers.remove(laser)
                        except:
                            continue


    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()


class Alien:
    def __init__(self, x, y, hp):
        self.vel = 0.4  # Velocity of the aliens
        self.hp = hp
        self.x = x
        self.y = y  # To be completed by students
        self.image = ALIEN_IMG  # To be completed by students
        self.mask = pg.mask.from_surface(self.image)  # To be completed by students

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.vel
        self.vel += 0.0001


class BigAlien(Alien):
    def __init__(self, x, y, hp):
        super().__init__(x, y, hp)
        self.image = BIG_ALIEN_IMG  # To be completed by students
        self.mask = pg.mask.from_surface(self.image)  # To be completed by students


class Laser:
    def __init__(self, x, y, power):
        self.image = LASER_BULLET  # To be completed by students
        self.mask = pg.mask.from_surface(self.image)  # To be completed by students
        self.x = x - self.image.get_width() / 2  # To be completed by students / Explain why it's not x
        self.y = y  # To be completed by students
        self.power = power

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))  # To be completed by students

    def move(self, vel):
        self.y += vel  # To be completed by students

    def get_width(self):
        return self.image.get_width()  # To be completed by students

    def get_height(self):
        return self.image.get_height()  # To be completed by students


class PowerUp:
    def __init__(self, x, y):
        self.image = POWER_UP_IMG  # To be completed by students
        self.mask = pg.mask.from_surface(self.image)  # To be completed by students
        self.vel = 5
        self.x = x
        self.y = y

    def move(self):
        self.y += self.vel  # To be completed by students
        self.vel -= 0.01

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))  # To be completed by students


def checkCollision(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None


def outOfScreen(obj):
    return obj.y < 0 or obj.y > HEIGHT


def main():
    font = pg.font.SysFont("comicsans", 60)
    run = True
    clock = pg.time.Clock()
    wave = 0 
    lives = 3

    ALIEN_ROW = 4
    ALIEN_COL = 6

    MAP_STATE = {1: "You Win!!", -1: "You lost!!"}
    state = 0  # default state
    print(MAP_STATE[-1])

    player = Player()

    aliens = []
    powerups = []

    def spawn_aliens(wave):
        for i in range(ALIEN_ROW):
            cur_row = 20 + i * 50
            for j in range(1, ALIEN_COL + 1):
                new_alien = Alien(int(j * WIDTH / (ALIEN_COL + 1)), cur_row, 1)
                aliens.append(new_alien)

        for k in range(wave):
            print(k)
            cur_row = 20 + (i+k+1) * 50
            for j in range(1, ALIEN_COL + 1):
                new_alien = BigAlien(int(j * WIDTH / (ALIEN_COL + 1)), cur_row, 2)
                aliens.append(new_alien)

    def redraw_window():
        WINDOW.fill((0, 20, 40))

        player.draw(WINDOW)
        for alien in aliens:
            alien.draw(WINDOW)
            alien.move()

        for powerup in powerups:
            powerup.draw(WINDOW)
            powerup.move()

        if state != 0:
            lost_label = font.render(MAP_STATE[state], 1, (255, 255, 255))
            WINDOW.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))
        
        lost_label = font.render("Wave " + str(wave), 1, (255, 255, 255))
        WINDOW.blit(lost_label, (WIDTH - lost_label.get_width() -10, 10))
        
        lost_label = font.render("Lives " + str(lives), 1, (255, 255, 255))
        WINDOW.blit(lost_label, (10, 10))


        pg.display.update()

    spawn_aliens(wave)
    while run:  # Main game loop
        clock.tick(FPS)
        redraw_window()

        

        # check for any event
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

        keys = pg.key.get_pressed()
        if keys[pg.K_a] and player.x - player.VELOCITY > 0:  # left
            player.move("left")
        if keys[pg.K_d] and player.x + player.VELOCITY + player.get_width() < WIDTH:  # right
            player.move("right")  # To be completed by students
        if keys[pg.K_w] and player.y - player.VELOCITY > 0:
            player.move("up") 
        if keys[pg.K_s] and player.y + player.VELOCITY + player.get_height() < HEIGHT:
            player.move("down")  
        if keys[pg.K_SPACE]:  # shoot
            player.shoot()

        player.move_lasers(-5, aliens, powerups)

        for alien in aliens:  # Check if any alien collides with player
            if checkCollision(alien, player):
                state = -1
            elif outOfScreen(alien):
                aliens.remove(alien)
                if lives == 0:
                    state = -1
                else:
                    lives -= 1

        for powerup in powerups:  # Check if any alien collides with player
            if checkCollision(powerup, player):
                player.cooldown /= 1.2
                powerups.remove(powerup)

            if outOfScreen(powerup):
                powerups.remove(powerup)

        if len(aliens) == 0:  # Check if there are any aliens left
            if wave == 2:
                state = 1
            else:
                wave += 1
                spawn_aliens(wave)

main()

import pygame as pg

FPS = 60

WIDTH, HEIGHT = 1000, 750
WINDOW = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Space Invaders")

# load images
SPACESHIP_IMG = pg.image.load("assets/spaceship_32.png")
ALIEN_IMG = pg.image.load("assets/alien_green_32x23.png")
LASER_BULET = pg.image.load("assets/lazer_bullet.png")

pg.font.init()

class Laser:
    def __init__(self, x, y):
        self.image = LASER_BULET
        self.x = x - self.image.get_width() / 2
        self.y = y
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()


class Player:
    COOLDOWN = 15
    LASER_VELOCITY = 5
    VELOCITY = 5

    def __init__(self):
        self.image = SPACESHIP_IMG
        self.x = int(WIDTH / 2)
        self.y = HEIGHT - self.image.get_width() * 2
        self.mask = pg.mask.from_surface(self.image)
        self.lasers = []
        self.cooldown = 0

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
        self.cooldown -= 1

    def shoot(self):
        if self.cooldown <= 0:
            new_laser = Laser(self.x + self.image.get_width() / 2, self.y)
            self.lasers.append(new_laser)
            self.cooldown = self.COOLDOWN

    def move(self, direction):
        if direction == "left":
            self.x -= self.VELOCITY
        if direction == "right":
            self.x += self.VELOCITY

    def move_lasers(self, vel, objs):
        for laser in self.lasers:
            laser.move(vel)
            if outOfScreen(laser):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if checkCollision(laser, obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()


class Alien:
    def __init__(self, x, y):
        self.vel = 0.4

        self.x = x
        self.y = y
        self.image = ALIEN_IMG
        self.mask = pg.mask.from_surface(self.image)

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += self.vel
        self.vel += 0.0001


def checkCollision(obj1, obj2):
    offset_x = int(obj2.x - obj1.x)
    offset_y = int(obj2.y - obj1.y)
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def outOfScreen(obj):
    return obj.y < 0 or obj.y > HEIGHT


def main():
    font = pg.font.SysFont("comicsans", 60)
    run = True
    clock = pg.time.Clock()

    ALIEN_ROW = 4
    ALIEN_COL = 10

    MAP_STATE = {1: "You Win!", -1: "You lost!"}
    state = 0  # default state

    player = Player()

    aliens = []
    for i in range(ALIEN_ROW):
        cur_row = 20 + i * 50
        for j in range(1, ALIEN_COL + 1):
            new_alien = Alien(int(j * WIDTH / (ALIEN_COL + 1)), cur_row)
            aliens.append(new_alien)

    def redraw_window():
        WINDOW.fill((0, 20, 40))

        player.draw(WINDOW)
        for alien in aliens:
            alien.draw(WINDOW)
            alien.move()

        if state != 0:
            lost_label = font.render(MAP_STATE[state], 1, (255, 255, 255))
            WINDOW.blit(lost_label, (WIDTH / 2 - lost_label.get_width() / 2, 350))

        pg.display.update()

    while run:
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
            player.move("right")
        if keys[pg.K_w]:  # right
            player.shoot()

        player.move_lasers(-5, aliens)

        for alien in aliens:
            if checkCollision(alien, player) or outOfScreen(alien):
                state = -1

        if len(aliens) == 0:
            state = 1


main()

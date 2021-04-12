from pygame import *
import random

windowX = 720
windowY = 360

init()
clock = time.Clock()
window = display.set_mode((windowX, windowY))

display.set_caption('Jumpy Thing!')

ground = windowY - 70

gravity = 1


class PlayerClass:
    def __init__(self, scale, imageChangeSpeed, terminalVelocity):
        self.run1 = transform.scale(image.load('run2.png'), (7 * scale, 14 * scale))
        self.run2 = transform.scale(image.load('run3.png'), (7 * scale, 14 * scale))
        self.run3 = transform.scale(image.load('run4.png'), (7 * scale, 14 * scale))
        self.run4 = transform.scale(image.load('run5.png'), (7 * scale, 14 * scale))
        self.run5 = transform.scale(image.load('run6.png'), (7 * scale, 14 * scale))

        self.scale = scale
        self.imageChangeSpeed = imageChangeSpeed
        self.terminalVelocity = terminalVelocity

        self.height = 14 * scale
        self.width = 7 * scale

    dead = False

    def update(self):
        self.physics()

        if self.touchingHurdle():
            self.dead = True

        if not self.dead:
            self.playerInput()

        self.y += self.velocityY

        self.show()

    def touchingHurdle(self):
        for hurdle in hurdleManager.hurdleList:
            if self.x + self.width > hurdle.x:
                if self.x < hurdle.x + hurdle.width:
                    if self.y + self.height > hurdle.y:
                        return True

    x = 100
    y = 100

    velocityY = 0

    def playerInput(self):
        pressedKeys = key.get_pressed()

        if pressedKeys[K_SPACE]:
            if self.y + self.height == ground:
                self.velocityY -= 10
            else:
                self.velocityY -= gravity / 2

    def physics(self):
        if self.dead:
            if self.y < windowY:
                self.velocityY += 1


        elif self.y + self.height < ground:
            if self.velocityY < self.terminalVelocity:
                self.velocityY += gravity


        elif self.velocityY > 0:
            self.velocityY = 0
            self.y = ground - self.height

    runTick = 0

    def show(self):
        if self.runTick <= self.imageChangeSpeed:
            img = self.run1
        elif self.runTick <= self.imageChangeSpeed * 2:
            img = self.run2
        elif self.runTick <= self.imageChangeSpeed * 3:
            img = self.run3
        elif self.runTick <= self.imageChangeSpeed * 4:
            img = self.run4
        else:
            img = self.run5

        self.runTick += 1

        if self.runTick >= self.imageChangeSpeed * 5:
            self.runTick = 0

        window.blit(img, (self.x, self.y))


player = PlayerClass(5, 6, 10)


class HurdleManager:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('hurdle.png'), (7 * scale, 15 * scale))

        self.spawnRange = spawnRange
        self.hurdleList = []
        self.scale = scale

    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)

    def manage(self, moveSpeed):
        hurdles2 = []

        for hurdle in self.hurdleList:
            hurdle.update(moveSpeed)

            if hurdle.onScreen():
                hurdles2.append(hurdle)

        self.hurdleList = hurdles2

    spawnTick = 0

    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newHurdle = HurdleClass(windowX, self.img, 7 * self.scale, 15 * self.scale)
            self.hurdleList.append(newHurdle)
            self.spawnTick = 0

        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0, self.spawnRange[1] - self.spawnRange[0]) == 0:
                newHurdle = HurdleClass(windowX, self.img, 7 * self.scale, 15 * self.scale)
                self.hurdleList.append(newHurdle)
                self.spawnTick = 0

        self.spawnTick += 1


hurdleManager = HurdleManager(3, (45, 90))


class HurdleClass:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = img
        self.width = width
        self.height = height
        self.y = ground - height

    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()

    def move(self, moveSpeed):
        self.x -= moveSpeed

    def show(self):
        window.blit(self.img, (self.x, self.y))

    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False


def mainEventLoop():
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                quit()


groundImg = transform.scale(image.load('ground.png'), (windowX, int(windowY - ground)))

font1 = font.Font('SFPixelate.ttf', 50)
font2 = font.Font('SFPixelate.ttf', 40)
deathMessage1 = font1.render('You Fell Over!', True, (255, 255, 255))
deathMessage1Shadow = font1.render('You Fell Over!', True, (0, 0, 0))
deathMessage2 = font2.render('Press Space', True, (255, 255, 255))
deathMessage2Shadow = font2.render('Press Space', True, (0, 0, 0))

message1Rect = deathMessage1.get_rect()
message1x = windowX / 2 - message1Rect.width / 2

message2Rect = deathMessage2.get_rect()
message2x = windowX / 2 - message2Rect.width / 2


def showMessage(y):
    window.blit(deathMessage1, (message1x, y))
    window.blit(deathMessage1Shadow, (message1x + 5, y + 5))

    window.blit(deathMessage2, (message2x, y + message1Rect.height))
    window.blit(deathMessage2Shadow, (message2x, message1Rect.height + 5 + y))


score = {'gameScore': 0}


def game():
    player.update()
    while True:
        if player.dead:
            fall(scoreStr)

        mainEventLoop()
        window.fill((200, 240, 250))

        player.update()

        hurdleManager.update(True, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        scoreStr = font2.render(str(round(score['gameScore'])), True, (0, 0, 0))
        window.blit(scoreStr, (50, 50))

        display.update()

        score['gameScore'] += 0.1


def fall(scoreStr):
    space = 0
    while True:
        pressedKeys = key.get_pressed()

        oldSpace = space
        space = pressedKeys[K_SPACE]

        mainEventLoop()
        window.fill((200, 240, 250))

        player.update()

        hurdleManager.update(False, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        showMessage(50)

        window.blit(scoreStr, (50, 50))
        display.update()

        spaceEvent = space - oldSpace

        if spaceEvent == 1:
            # Reset Everything

            hurdleManager.hurdleList = []
            player.velocityY = 0
            player.dead = False
            player.y = ground - player.height
            score['gameScore'] = 0

            break


game()
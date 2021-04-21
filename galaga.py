import pgzrun
import random
# screen dimensions

WIDTH = 1200
HEIGHT = 1000

# defining colours of our game
BLUE = (0, 0, 255)


# create our galaga ship

ship = Actor('galaga')

# specify initial position of ship

ship.x = WIDTH//2
ship.y = HEIGHT-60
ship.dead = False
ship.countdown = 90

# define a list for bullets
bullets = []

# define a list for enemies
enemies = []
NUMBER_OF_ENEMIES = 10
NUMBER_OF_ROWS = 5

for x in range(NUMBER_OF_ENEMIES):
    for y in range(NUMBER_OF_ROWS):
        enemies.append(Actor('bug'))
        enemies[-1].x = 100 + 90*x
        enemies[-1].y = 80 + 80*y

score = 0
direction = 1


def drawScore():
    screen.draw.text(str(score), (50, 30), fontname="arcade", fontsize=40)


def drawWin():
    screen.draw.text("YOU WIN!", (WIDTH/4, HEIGHT/2),
                     fontname="pacfont", fontsize=80)


def on_key_down(key):
    if ship.dead == False:
        if keyboard.space:
            bullets.append(Actor('bullet'))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y


def update():
    global score, direction
    # ship movement using arrow keys left and right
    if ship.dead == False:
        if keyboard.left:
            ship.x -= 5
        elif keyboard.right:
            ship.x += 5

    moveDown = False

    for bullet in bullets:
        if bullet.y < - 20:
            bullets.remove(bullet)
        else:
            bullet.y -= 10

    if len(enemies) > 0 and (enemies[-1].x > WIDTH - 80 or enemies[0].x < 50):
        moveDown = True
        direction *= -1
    for enemy in enemies:
        enemy.x += 5 * direction
        if moveDown == True:
            enemy.y += 30
        for bullet in bullets:
            if enemy.colliderect(bullet):
                score += 150
                bullets.remove(bullet)
                enemies.remove(enemy)
        if enemy.colliderect(ship):
            ship.dead = True

    if ship.dead:
        ship.countdown -= 1
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90


def draw():
    screen.clear()
    screen.fill(BLUE)
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if ship.dead == False:
        ship.draw()
    drawScore()
    if len(enemies) == 0:
        ship.dead = True
        drawWin()


pgzrun.go()

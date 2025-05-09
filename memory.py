from random import *
from turtle import *
from freegames import path


while True:
    tileNumber = int(input("Enter desired number of tiles: "))
    if tileNumber % 2 == 0:
        break
    print("Invalid value: must be divisible by two.")

car = path('car.gif')
tiles = list(range(int((tileNumber**2) / 2))) * 2
state = {'mark': None}
hide = [True] * (tileNumber**2)
tileSize = 400 // tileNumber
revealedTiles = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(tileSize)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // tileSize + ((y + 200) // tileSize) * tileNumber)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % tileNumber) * tileSize - 200, (count // tileNumber) * tileSize - 200


def tap(x, y):
    global revealedTiles
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        revealedTiles += 1
        if revealedTiles == tileNumber * 2:
            print("All tiles have been revealed.")


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(tileNumber**2):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(440, 440)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

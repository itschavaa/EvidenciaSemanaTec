import random
import turtle
from freegames import path

# Ask user for a valid tile number, must be even for pairs to be made.
while True:
    tileNumber = int(input("Enter desired number of tiles: "))
    if tileNumber % 2 == 0:
        break
    print("Invalid value: must be divisible by two.")

# Initialize game assets and state.
car = path('car.gif')
tiles = list(range(int((tileNumber**2) / 2))) * 2  # Create pairs of tiles
state = {'mark': None}  # Track currently selected tile
hide = [True] * (tileNumber**2)  # Track which tiles are hidden
tileSize = 400 // tileNumber  # Calculate size of each tile based on grid
revealedPairs = 0


def square(x_pos, y_pos):
    """Draw white square with black outline at (x, y)."""
    turtle.up()
    turtle.goto(x_pos, y_pos)
    turtle.down()
    turtle.color('black', 'white')
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(tileSize)
        turtle.left(90)
    turtle.end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index.
    Arguments:
        x: x coordinate of click
        y: y coordinate of click
    Returns:
        int: index of the clicked tile
    """
    return int((x + 200) // tileSize + ((y + 200) // tileSize) * tileNumber)


def xy(count):
    """Convert tiles count to (x, y) coordinates.
    Arguments:
        count: tile index
    Returns:
        tuple: (x, y) coordinates for the tile
    """
    return ((count % tileNumber) * tileSize - 200,
            (count // tileNumber) * tileSize - 200)


def tap(x, y):
    """Handle tile clicks.
    Arguments:
        x: x coordinate of click
        y: y coordinate of click
    """
    global revealedPairs

    # Update mark and hidden tiles based on tap.
    spot = index(x, y)
    mark = state['mark']

    # Ignore already revealed tiles.
    if not hide[spot]:
        return

    # First selection / invalid pair.
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Matching pair found.
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        revealedPairs += 1

        # Print number of revealed pairs.
        print(f"{revealedPairs} pair(s) have been revealed")

        # Check if all tiles have been revealed.
        if revealedPairs == tileNumber * 2:
            print("All tiles have been revealed.")


def draw():
    # Draw image and tiles.
    turtle.clear()
    turtle.goto(0, 0)
    turtle.shape(car)
    turtle.stamp()

    for count in range(tileNumber**2):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        turtle.up()
        turtle.goto(x + 2, y)
        turtle.color('black')
        turtle.write(tiles[mark], font=('Arial', 30, 'normal'))

    turtle.update()
    turtle.ontimer(draw, 100)


# Game initialization.
random.shuffle(tiles)
turtle.setup(440, 440)  # Set up game window size to 440 x 440 pixels
turtle.addshape(car)
turtle.hideturtle()
turtle.tracer(False)
turtle.onscreenclick(tap)
draw()
turtle.done()

import random
import curses

# Initialize  Screen
s = curses.initscr()
curses.curs_set(0)
# Get Width & Height
sh, sw = s.getmaxyx()
# Create New Window
w = curses.newwin(sh, sw, 0, 0)
# Accept Keypad Input
w.keypad(1)
# Refresh Screen Every 100 MS
w.timeout(100)
# Snakes Initial Position
# Note : In Python 3 '/' results in floating point results. To get integer results, use integer division '//'.
snk_x = sw//4
snk_y = sh//2
# Snake Body Part
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
# Food
food = [sh//2, sw//2]
# Add Food To The Screen
w.addch(food[0], food[1], curses.ACS_PI)
# Where Its Going Initially
key = curses.KEY_RIGHT

# Infinite Loop For Moving Snake
while True:
    # See What The Next Key Pressed
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check If The Person Lost The Game
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    # New Head Of Snake
    new_head = [snake[0][0], snake[0][1]]

    # Check What The Actual Key Is Pressed To Determine New Head
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Add New Head
    snake.insert(0, new_head)

    # Check If Snake Ran Into Food
    if snake[0] == food:
        food = None
        while food is None:
            # Create New Food
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        # Add Food New Food To Screen
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # If Not Remove The Tail From Snake
        tail = snake.pop()
        # Add Space Where Tail Was
        w.addch(tail[0], tail[1], ' ')

    # Add Head To The Screen
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

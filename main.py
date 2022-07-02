import random
import curses

#x/y can be any ratio
x = 32
y = 64

worldmap = []

x_iter = 0
y_iter = 0



# random map generator
while x_iter <= x:
    y_iter = 0
    newline = ''
    while y_iter <= y:
        newlinechar = str(random.randint(0, 4))
        newline = newline + newlinechar
        y_iter += 1
    worldmap.append(newline)
    x_iter += 1


# define chars and colors for ncurses
blockchar = '█'

stdscr = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
window = curses.newwin(len(worldmap), len(worldmap[0]) + 1, 3, 3) # curses.newwin(height, width, begin_y, begin_x)


###vvv    unpack map    vvv###
outer_loop_itx = 0
for range in worldmap:
    #print(worldmap[outer_loop_itx])
    inner_loop_itx = 0
    for range in worldmap[0]:
        #decision making here
        if worldmap[outer_loop_itx][inner_loop_itx] == '0':
            window.addstr(outer_loop_itx, inner_loop_itx, blockchar, curses.color_pair(3))  # startx, starty, len, color
        if worldmap[outer_loop_itx][inner_loop_itx] == '1':
            window.addstr(outer_loop_itx, inner_loop_itx, blockchar, curses.color_pair(2))
        if worldmap[outer_loop_itx][inner_loop_itx] == '2':
            window.addstr(outer_loop_itx, inner_loop_itx, blockchar, curses.color_pair(1))
        if worldmap[outer_loop_itx][inner_loop_itx] == '3':
            window.addstr(outer_loop_itx, inner_loop_itx, blockchar, curses.color_pair(4))
        if worldmap[outer_loop_itx][inner_loop_itx] == '4':
            window.addstr(outer_loop_itx, inner_loop_itx, blockchar, curses.color_pair(5))

        inner_loop_itx += 1
    window.refresh() # run in outer loop , this is time costly   
    outer_loop_itx += 1
import time
import random
from machine import Pin
from neopixel import NeoPixel

# ── Hardware Setup ─────────────────────────────────────────────
btn_up    = Pin(4,  Pin.IN, Pin.PULL_UP)
btn_down  = Pin(5,  Pin.IN, Pin.PULL_UP)
btn_left  = Pin(18, Pin.IN, Pin.PULL_UP)
btn_right = Pin(19, Pin.IN, Pin.PULL_UP)
btn_place = Pin(33, Pin.IN, Pin.PULL_UP)

np_board = NeoPixel(Pin(13, Pin.OUT), 64)   # 8x8 game board
np_prev = NeoPixel(Pin(32, Pin.OUT), 64)    # 8x8 matrix (using 5x5 area)

led_green = Pin(2,  Pin.OUT)
led_red   = Pin(23, Pin.OUT)

last_press = {'up':0,'down':0,'left':0,'right':0,'place':0}
DEBOUNCE   = 200

buttons = {'up': btn_up, 'down': btn_down, 'left': btn_left, 'right': btn_right, 'place': btn_place}

def pressed(name):
    now = time.ticks_ms()
    if buttons[name].value() == 0: 
        if time.ticks_diff(now, last_press[name]) > DEBOUNCE:
            last_press[name] = now
            return True
    return False

# ── Index functions ────────────────────────────────────────────
def board_idx(x, y):
    return y * 8 + x

# ── Index function ─────────────────────────────────────
def prev_idx(x, y):
    # To skip the first 3 rows and 3 columns on an 8x8 matrix:
    px, py = x + 3, y + 2
    return py * 8 + px

# ── Blocks ─────────────────────────────────────────────────────
BLOCK_DEFS = [
    [(2,1),(2,2),(1,2),(1,3)],
    [(1,1),(1,2),(2,2),(2,3)],
    [(1,2),(2,1),(2,2),(3,1)],
    [(1,2),(2,2),(2,3),(3,3)],
    [(1,1),(1,2),(2,1),(2,2),(3,1),(3,2)],
    [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)],
    [(2,1),(2,2),(2,3)],
    [(1,2),(2,2),(3,2)],
    [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)],
    [(1,1),(1,2),(2,1),(2,2)],
    [(1,1),(1,2),(1,3),(2,3),(3,3)],
    [(1,1),(1,2),(1,3),(2,1),(3,1)],
    [(1,1),(2,1),(3,1),(3,2),(3,3)],
    [(1,3),(2,3),(3,3),(3,2),(3,1)],
    [(2,3),(3,3),(3,2),(1,3)],
    [(1,2),(1,3),(2,3),(3,3)],
    [(1,1),(2,1),(3,1),(1,2)],
    [(1,1),(2,1),(3,1),(3,2)],
    [(2,1),(2,2),(2,3),(1,3)],
    [(2,1),(2,2),(2,3),(1,1)],
    [(2,1),(2,2),(2,3),(3,1)],
    [(2,1),(2,2),(2,3),(3,3)],
    [(2,1),(2,2)],
    [(2,2),(1,2)],
    [(2,2)],
    [(2,0),(2,1),(2,2),(2,3),(2,4)],
    [(0,2),(1,2),(2,2),(3,2),(4,2)],
    [(2,0),(2,1),(2,2),(2,3)],
    [(0,2),(1,2),(2,2),(3,2)],
    [(2,1),(2,2),(2,3),(1,2)],
    [(2,1),(2,2),(2,3),(3,2)],
    [(2,1),(2,2),(1,2),(3,2)],
    [(2,2),(2,3),(1,2),(3,2)],
    [(1,2),(2,2),(1,3)],
    [(1,1),(1,2),(2,2)],
    [(1,1),(2,1),(2,2)],
    [(2,2),(2,3),(1,3)]
]


COLORS = [(30,0,0), (0,30,0), (0,0,30), (30,15,0), (20,0,30), (0,25,25), (30,30,0)]
color_index = 0

def next_color():
    global color_index
    c = COLORS[color_index % len(COLORS)]
    color_index += 1
    return c

def flash_green(times=2):
    for _ in range(times):
        led_green.value(1)
        time.sleep_ms(150)
        led_green.value(0)
        time.sleep_ms(100)

def flash_red(times=3):
    for _ in range(times):
        led_red.value(1)
        time.sleep_ms(150)
        led_red.value(0)
        time.sleep_ms(100)

def clear_all():
    for i in range(64):
        np_board[i] = (0, 0, 0)
        np_prev[i]  = (0, 0, 0)
    np_board.write()
    np_prev.write()

def render_board_with_cursor(block, ox, oy):
    for i in range(64):
        x, y = i % 8, i // 8
        np_board[i] = board[y][x] if board[y][x] else (0,0,0)
    
    for (dx, dy) in block:
        gx, gy = ox + dx, oy + dy
        if 0 <= gx < 8 and 0 <= gy < 8:
            np_board[board_idx(gx, gy)] = (150, 150, 150) # Bright White
    np_board.write()

def render_preview(block):
    for i in range(64): np_prev[i] = (0,0,0)
    for (dx, dy) in block:
        np_prev[prev_idx(dx, dy)] = (50, 50, 50)
    np_prev.write()

# ── Logic ──────────────────────────────────────────────────────
def block_fits(block, ox, oy):
    for (dx, dy) in block:
        x, y = ox + dx, oy + dy
        if not (0 <= x < 8 and 0 <= y < 8) or board[y][x] is not None:
            return False
    return True

def any_valid_position(block):
    for y in range(8):
        for x in range(8):
            if block_fits(block, x, y): return True
    return False

def check_and_clear_lines():
    global score
    cleared = 0
    # Check rows and columns
    rows = [y for y in range(8) if all(board[y][x] is not None for x in range(8))]
    cols = [x for x in range(8) if all(board[y][x] is not None for y in range(8))]
    
    if rows or cols:
        for y in rows:
            for x in range(8): board[y][x] = None
            cleared += 1
        for x in cols:
            for y in range(8): board[y][x] = None
            cleared += 1

        render_board_only() 
        flash_green(2)
        
    return cleared

def render_board_only():
    """Wipes the matrix and draws only settled blocks (no cursor)."""
    for i in range(64):
        x, y = i % 8, i // 8
        np_board[i] = board[y][x] if board[y][x] else (0,0,0)
    np_board.write()

# ── Main Loop ──────────────────────────────────────────────────    
def run_game():
    global board
    board = [[None]*8 for _ in range(8)]
    clear_all()
    
    cur_block = random.choice(BLOCK_DEFS)
    cur_color = next_color()
    next_blk  = random.choice(BLOCK_DEFS)
    cursor_x, cursor_y = 0, 0 

    while True:
        # Side matrix shows what's coming next (offset to bottom-right)
        render_preview(next_blk)
        # Main matrix shows board + your moving white block
        render_board_with_cursor(cur_block, cursor_x, cursor_y)

        if pressed('up'):
            min_y = min(dy for dx, dy in cur_block)
            if cursor_y + min_y > 0: 
                cursor_y -= 1
                
        if pressed('down'):
            max_y = max(dy for dx, dy in cur_block)
            if cursor_y + max_y < 7: 
                cursor_y += 1
                
        if pressed('left'):
            min_x = min(dx for dx, dy in cur_block)
            if cursor_x + min_x > 0: 
                cursor_x -= 1
                
        if pressed('right'): 
            max_x = max(dx for dx, dy in cur_block)
            if cursor_x + max_x < 7: 
                cursor_x += 1
                
        # 2. Placement Logic
        if pressed('place'):
            if block_fits(cur_block, cursor_x, cursor_y):
                for (dx, dy) in cur_block:
                    board[cursor_y + dy][cursor_x + dx] = cur_color
                
                if check_and_clear_lines() > 0:
                    time.sleep_ms(200)
                    
                cur_block, cur_color = next_blk, next_color()
                next_blk = random.choice(BLOCK_DEFS)
                cursor_x, cursor_y = 0, 0 
                
                if not any_valid_position(cur_block):
                    flash_red(5)
                    board = [[None]*8 for _ in range(8)]
                    clear_all()
                    print ("Game Over")
                    time.sleep(10)
            else:
                led_red.value(1)
                time.sleep_ms(150)
                led_red.value(0)

        time.sleep_ms(25)

run_game()
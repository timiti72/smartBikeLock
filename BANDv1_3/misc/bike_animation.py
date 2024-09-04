from timer import *

def screen_reset(oled):
    oled.fill_rect(2, 23, 124, 10, 0)

def draw_bike(oled, offset, color):
    lines = [
        (54 + offset, 24, 7), (55 + offset, 25, 5), (73 + offset, 25, 8),
        (56 + offset, 25, 2), (73 + offset, 25, 2), (80 + offset, 25, 1),
        (56 + offset, 26, 2), (73 + offset, 26, 2), (80 + offset, 26, 1),
        (56 + offset, 27, 2), (73 + offset, 27, 2), (78 + offset, 27, 3),
        (56 + offset, 28, 18), (56 + offset, 29, 18), (48 + offset, 30, 5),
        (56 + offset, 30, 3), (72 + offset, 30, 9), (46 + offset, 31, 9),
        (56 + offset, 31, 4), (72 + offset, 31, 11), (45 + offset, 32, 2),
        (53 + offset, 32, 5), (58 + offset, 32, 2), (71 + offset, 32, 6),
        (81 + offset, 32, 3), (44 + offset, 33, 2), (54 + offset, 33, 3),
        (59 + offset, 33, 2), (70 + offset, 33, 4), (76 + offset, 33, 2),
        (83 + offset, 33, 2), (43 + offset, 34, 2), (53 + offset, 34, 2),
        (56 + offset, 34, 2), (59 + offset, 34, 2), (69 + offset, 34, 4),
        (76 + offset, 34, 2), (84 + offset, 34, 2), (42 + offset, 35, 2),
        (52 + offset, 35, 2), (56 + offset, 35, 2), (59 + offset, 35, 2),
        (68 + offset, 35, 5), (77 + offset, 35, 2), (84 + offset, 35, 2),
        (42 + offset, 36, 2), (51 + offset, 36, 2), (57 + offset, 36, 2),
        (60 + offset, 36, 2), (67 + offset, 36, 5), (77 + offset, 36, 2),
        (85 + offset, 36, 2), (42 + offset, 37, 2), (50 + offset, 37, 2),
        (57 + offset, 37, 2), (60 + offset, 37, 2), (66 + offset, 37, 6),
        (77 + offset, 37, 2), (85 + offset, 37, 2), (42 + offset, 38, 2),
        (49 + offset, 38, 2), (57 + offset, 38, 2), (60 + offset, 38, 8),
        (70 + offset, 38, 2), (79 + offset, 38, 1), (85 + offset, 38, 2),
        (42 + offset, 39, 2), (49 + offset, 39, 16), (70 + offset, 39, 2),
        (85 + offset, 39, 2), (42 + offset, 40, 2), (50 + offset, 40, 14),
        (70 + offset, 40, 2), (85 + offset, 40, 2), (43 + offset, 41, 2),
        (56 + offset, 41, 2), (71 + offset, 41, 2), (84 + offset, 41, 2),
        (43 + offset, 42, 2), (56 + offset, 42, 2), (71 + offset, 42, 2),
        (84 + offset, 42, 2), (44 + offset, 43, 2), (55 + offset, 43, 2),
        (72 + offset, 43, 2), (83 + offset, 43, 2), (45 + offset, 44, 3),
        (53 + offset, 44, 3), (73 + offset, 44, 3), (81 + offset, 44, 3),
        (46 + offset, 45, 9), (74 + offset, 45, 9), (48 + offset, 46, 5),
        (76 + offset, 46, 5)
    ]
    for line in lines:
        x, y, length = line
        oled.hline(x, y, length, color)

def update_display(oled, prev_lines, new_lines):
    # Turn off the pixels that are not common between frames
    for line in prev_lines:
        x, y, length = line
        oled.hline(x, y, length, 0)  # Turn off the previous frame pixels

    # Draw the new frame
    for line in new_lines:
        x, y, length = line
        oled.hline(x, y, length, 1)  # Turn on the new frame pixels

def animate_bike(oled):
    prev_lines = []
    for offset in range(-100, 130, 6):
        oled.vline(0, 21, 63, 1)
        oled.vline(127, 21, 63, 1)
        # Adjust the range and step for the desired animation
        screen_reset(oled)  # Clear the display
        new_lines = [
            (54 + offset, 24, 7), (55 + offset, 25, 5), (73 + offset, 25, 8),
            (56 + offset, 25, 2), (73 + offset, 25, 2), (80 + offset, 25, 1),
            (56 + offset, 26, 2), (73 + offset, 26, 2), (80 + offset, 26, 1),
            (56 + offset, 27, 2), (73 + offset, 27, 2), (78 + offset, 27, 3),
            (56 + offset, 28, 18), (56 + offset, 29, 18), (48 + offset, 30, 5),
            (56 + offset, 30, 3), (72 + offset, 30, 9), (46 + offset, 31, 9),
            (56 + offset, 31, 4), (72 + offset, 31, 11), (45 + offset, 32, 2),
            (53 + offset, 32, 5), (58 + offset, 32, 2), (71 + offset, 32, 6),
            (81 + offset, 32, 3), (44 + offset, 33, 2), (54 + offset, 33, 3),
            (59 + offset, 33, 2), (70 + offset, 33, 4), (76 + offset, 33, 2),
            (83 + offset, 33, 2), (43 + offset, 34, 2), (53 + offset, 34, 2),
            (56 + offset, 34, 2), (59 + offset, 34, 2), (69 + offset, 34, 4),
            (76 + offset, 34, 2), (84 + offset, 34, 2), (42 + offset, 35, 2),
            (52 + offset, 35, 2), (56 + offset, 35, 2), (59 + offset, 35, 2),
            (68 + offset, 35, 5), (77 + offset, 35, 2), (84 + offset, 35, 2),
            (42 + offset, 36, 2), (51 + offset, 36, 2), (57 + offset, 36, 2),
            (60 + offset, 36, 2), (67 + offset, 36, 5), (77 + offset, 36, 2),
            (85 + offset, 36, 2), (42 + offset, 37, 2), (50 + offset, 37, 2),
            (57 + offset, 37, 2), (60 + offset, 37, 2), (66 + offset, 37, 6),
            (77 + offset, 37, 2), (85 + offset, 37, 2), (42 + offset, 38, 2),
            (49 + offset, 38, 2), (57 + offset, 38, 2), (60 + offset, 38, 8),
            (70 + offset, 38, 2), (79 + offset, 38, 1), (85 + offset, 38, 2),
            (42 + offset, 39, 2), (49 + offset, 39, 16), (70 + offset, 39, 2),
            (85 + offset, 39, 2), (42 + offset, 40, 2), (50 + offset, 40, 14),
            (70 + offset, 40, 2), (85 + offset, 40, 2), (43 + offset, 41, 2),
            (56 + offset, 41, 2), (71 + offset, 41, 2), (84 + offset, 41, 2),
            (43 + offset, 42, 2), (56 + offset, 42, 2), (71 + offset, 42, 2),
            (84 + offset, 42, 2), (44 + offset, 43, 2), (55 + offset, 43, 2),
            (72 + offset, 43, 2), (83 + offset, 43, 2), (45 + offset, 44, 3),
            (53 + offset, 44, 3), (73 + offset, 44, 3), (81 + offset, 44, 3),
            (46 + offset, 45, 9), (74 + offset, 45, 9), (48 + offset, 46, 5),
            (76 + offset, 46, 5)
        ]
        update_display(oled, prev_lines, new_lines)
        oled.show()
        prev_lines = new_lines.copy()
import pygame
from test_1_list_making import *

# color code
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 167, 0)
yellow = (255, 255, 0)
color = {
    'g': green,
    'r': red,
    'b': blue,
    'o': orange,
    'w': white,
    'y': yellow
}

# variables
screen_width = 800
screen_height = 500
fps = 30
running = True
margin = 10
game_window_width = screen_width - margin * 2
game_window_height = screen_height - margin * 2
line_width = 2
cell_height = game_window_height // 9
cell_width = game_window_width // 12

# position of cube sides
cube_position = [
    (margin, margin + cell_height * 3), (margin + cell_width * 3, margin + cell_height * 3),
    (margin + cell_width * 6, margin + cell_height * 3), (margin + cell_width * 9, margin + cell_height * 3),
    (margin + cell_width * 3, margin), (margin + cell_width * 3, margin + cell_height * 6)
]


def draw_maze(screen):
    # horizontal line
    for i in range(10):
        if i > 2 and i < 7:
            pygame.draw.rect(screen, black,
                             [margin, margin + cell_height * i, game_window_width,
                              line_width])
        else:
            pygame.draw.rect(screen, black,
                             [margin + game_window_width // 4, margin + cell_height * i, game_window_width // 4,
                              line_width])

    # vertical line
    for i in range(13):
        if i > 2 and i < 7:
            pygame.draw.rect(screen, black, [margin + cell_width * i, margin, line_width, game_window_height])
        else:
            pygame.draw.rect(screen, black, [margin + cell_width * i, margin + game_window_height // 3, line_width,
                                             game_window_height // 3])


def feel_color_in_side(screen, cube_side, pos_x, pos_y):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, color[cube_side[i][j][0]],
                             [pos_x + cell_width * j + line_width, pos_y + line_width + cell_height * i,
                              cell_width - line_width,
                              cell_height - line_width])


def feel_color_in_cube(screen, cube):
    for i in range(6):
        feel_color_in_side(screen, cube[i], cube_position[i][0], cube_position[i][1])


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("rubik's cube")
clock = pygame.time.Clock()
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    draw_maze(screen)
    feel_color_in_cube(screen, END.copy())
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

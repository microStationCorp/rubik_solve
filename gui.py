import pygame
from test_1_list_making import *

# variables
screen_width = 800
screen_height = 500
fps = 30
running = True
white = (255, 255, 255)
black = (0, 0, 0)
margin = 10
game_window_width = screen_width - margin * 2
game_window_height = screen_height - margin * 2
line_width = 2
cell_height = game_window_height // 9
cell_width = game_window_width // 12


def draw_maze(screen):
    # horizontal line
    pygame.draw.line(screen, black, (margin + game_window_width // 4, margin),
                     (margin + game_window_width // 4 * 2, margin),
                     line_width)
    pygame.draw.line(screen, black, (margin + game_window_width // 4, margin + cell_height),
                     (margin + game_window_width // 4 * 2, margin + cell_height), line_width)
    pygame.draw.line(screen, black, (margin + game_window_width // 4, game_window_height // 3 + margin - cell_height),
                     (margin + game_window_width // 4 * 2, game_window_height // 3 + margin - cell_height), line_width)
    pygame.draw.line(screen, black, (margin, game_window_height // 3 + margin),
                     (screen_width - margin, game_window_height // 3 + margin), line_width)
    pygame.draw.line(screen, black, (margin, game_window_height // 3 + margin + cell_height),
                     (screen_width - margin, game_window_height // 3 + margin + cell_height), line_width)
    pygame.draw.line(screen, black, (margin, game_window_height // 3 * 2 + margin - cell_height),
                     (screen_width - margin, game_window_height // 3 * 2 + margin - cell_height), line_width)
    pygame.draw.line(screen, black, (margin, game_window_height // 3 * 2 + margin),
                     (screen_width - margin, game_window_height // 3 * 2 + margin), line_width)
    pygame.draw.line(screen, black,
                     (margin + game_window_width // 4, margin + cell_height + game_window_height // 3 * 2),
                     (margin + game_window_width // 4 * 2, margin + cell_height + game_window_height // 3 * 2),
                     line_width)
    pygame.draw.line(screen, black, (margin + game_window_width // 4, screen_height - margin - cell_height),
                     (margin + game_window_width // 4 * 2, screen_height - margin - cell_height),
                     line_width)
    pygame.draw.line(screen, black, (margin + game_window_width // 4, screen_height - margin),
                     (margin + game_window_width // 4 * 2, screen_height - margin),
                     line_width)

    # vertical line
    pygame.draw.line(screen, black, (margin, game_window_height // 3 + margin),
                     (margin, game_window_height // 3 * 2 + margin), line_width)
    pygame.draw.line(screen, black, (margin + cell_width, game_window_height // 3 + margin),
                     (margin + cell_width, game_window_height // 3 * 2 + margin), line_width)
    pygame.draw.line(screen, black, (margin + cell_width * 2, game_window_height // 3 + margin),
                     (margin + cell_width * 2, game_window_height // 3 * 2 + margin), line_width)
    pygame.draw.line(screen, black, (game_window_width // 4 + margin, margin),
                     (game_window_width // 4 + margin, screen_height - margin), line_width)
    pygame.draw.line(screen, black, (game_window_width // 4 + margin + cell_width, margin),
                     (game_window_width // 4 + margin + cell_width, screen_height - margin), line_width)
    pygame.draw.line(screen, black, (game_window_width // 4 * 2 + margin - cell_width, margin),
                     (game_window_width // 4 * 2 + margin - cell_width, screen_height - margin), line_width)
    pygame.draw.line(screen, black, (game_window_width // 4 * 2 + margin, margin),
                     (game_window_width // 4 * 2 + margin, screen_height - margin), line_width)
    pygame.draw.line(screen, black,
                     (game_window_width // 4 * 2 + margin + cell_width, margin + game_window_height // 3),
                     (game_window_width // 4 * 2 + margin + cell_width,
                      screen_height - margin - game_window_height // 3), line_width)
    pygame.draw.line(screen, black,
                     (margin + game_window_width // 4 * 3 - cell_width, margin + game_window_height // 3),
                     (margin + game_window_width // 4 * 3 - cell_width,
                      screen_height - margin - game_window_height // 3),
                     line_width)
    pygame.draw.line(screen, black, (margin + game_window_width // 4 * 3, margin + game_window_height // 3),
                     (margin + game_window_width // 4 * 3, screen_height - margin - game_window_height // 3),
                     line_width)
    pygame.draw.line(screen, black,
                     (margin + game_window_width // 4 * 3 + cell_width, margin + game_window_height // 3),
                     (margin + game_window_width // 4 * 3 + cell_width,
                      screen_height - margin - game_window_height // 3),
                     line_width)
    pygame.draw.line(screen, black,
                     (margin + game_window_width // 4 * 3 + cell_width * 2, margin + game_window_height // 3),
                     (margin + game_window_width // 4 * 3 + cell_width * 2,
                      screen_height - margin - game_window_height // 3),
                     line_width)
    pygame.draw.line(screen, black, (screen_width - margin, margin + game_window_height // 3),
                     (screen_width - margin, screen_height - margin - game_window_height // 3),
                     line_width)


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
    pygame.display.update()
    clock.tick(fps)

pygame.quit()

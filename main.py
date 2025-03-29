import pygame

import time

pygame.init()

#CANVAS & GRID SETTING
CANVA_WIDTH = 400
CANVA_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

#COLORS
BLUE = (0,0,225)
WHITE = (255,255,255)
PINK = (225, 192, 193)

#Create window
screen = pygame.display.set_mode((CANVA_WIDTH, CANVA_HEIGHT))
pygame.display.set_caption("Enter effect in pygame")

#create grid
grid = []
for row in range(0, CANVA_HEIGHT, CELL_SIZE):
    for col in range(0, CANVA_WIDTH, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE,CELL_SIZE)
        grid.append(rect)

#eraser
eraser = pygame.Rect(200,200,ERASER_SIZE,ERASER_SIZE) 

#main loop
running = True
while running:
    screen.fill(WHITE)

    for rect in grid:
        pygame.draw.rect(screen, BLUE, rect)

    #eraser movement by mouse
    mouse_x, mouse_y =pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y) 

    #draw grid
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            new_grid.append(rect)

    grid = new_grid

    #draw eraser
    pygame.draw.rect(screen, PINK , eraser)

    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.05) #maintain 5 seconds

pygame.quit()    
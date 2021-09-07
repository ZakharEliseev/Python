import pygame

X = 800
Y = 600
game_over = False

pygame.init()
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('PyGame!')

myimage = pygame.image.load('kotik.png').convert()

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_over = True

    screen.blit(myimage, (100, 100))
    pygame.display.flip()

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Программа')
running = True
while running:
    
    
    
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
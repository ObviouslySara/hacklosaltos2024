import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Bill the Landlord")
clock = pygame.time.Clock()
font = pygame.font.Font('SourceCodePro-Light.ttf', 15)

surface = pygame.Surface((1000, 500))
surface.fill('#87CEEB')
bill = pygame.image.load('billfrthistime.png')

def displayParagraph(text, x, y, size):
    while len(text) >= size:
        line = font.render(text[:size], False, 'Black')
        text = text[size:]
        screen.blit(line, (x, y))
        y += 20
    screen.blit(font.render(text, False, 'Black'), (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0, 0))
    pygame.draw.rect(surface, (74, 217, 124), pygame.Rect(0, 400, 1000, 400))
    
    displayParagraph('Hi! I’m Bill and I’ll be your character. Currently, I’ve saved up $500,000 for investments. Join me on our journey of buying homes, renting properties, and more!', 600, 250, 35)
    screen.blit(bill, (100, 210))

    pygame.display.update()
    clock.tick(60)
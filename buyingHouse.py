import pygame
import csv
import random
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Bill the Landlord")
clock = pygame.time.Clock()
font = pygame.font.Font('SourceCodePro-Light.ttf', 15)

surface = pygame.Surface((1000, 500))
surface.fill('#87CEEB')
bill = pygame.image.load('billfrthistime.png')
leftButton = pygame.image.load('leftButton.png')
rightButton = pygame.image.load('rightButton.png')

def displayParagraph(text, x, y, size):
    while len(text) >= size:
        line = font.render(text[:size], False, 'Black')
        text = text[size:]
        screen.blit(line, (x, y))
        y += 20
    screen.blit(font.render(text, False, 'Black'), (x, y))

houses = {}

input = open('USA_Housing.csv')
csv_reader = csv.reader(input, delimiter=',')

house_prices = []
for row in csv_reader:
    house_prices.append(row)

for i in range(6):
    row = random.randint(1, 4999)
    rooms = round(float(house_prices[row][2]))
    bedrooms = round(float(house_prices[row][3]))
    price = round(float(house_prices[row][5]))
    houseImage = 'house' + str(i) + '.png'
    houses[i] = [rooms, bedrooms, price, houseImage]

key = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 25 <= mouse[0] <= 89 and 175 <= mouse[1] <= 116 + 175:
                key = ((key + 6) - 1) % 6
            if 915 <= mouse[0] <= 979 and 175 <= mouse[1] <= 116 + 175:
                key = (key + 1) % 6

    screen.blit(surface, (0, 0))
    pygame.draw.rect(surface, (74, 217, 124), pygame.Rect(0, 400, 1000, 400))
    screen.blit(leftButton, (25, 175))
    screen.blit(rightButton, (915, 175))

    curHouse = pygame.image.load(houses[key][3])
    screen.blit(curHouse, (300, 100))

    mouse = pygame.mouse.get_pos() 
    pygame.display.update()
    clock.tick(60)
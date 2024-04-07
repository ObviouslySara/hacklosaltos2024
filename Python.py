import pygame
import csv
import random
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(surface, (0, 0))
    pygame.draw.rect(surface, (74, 217, 124), pygame.Rect(0, 400, 1000, 400))

    pygame.display.update()
    clock.tick(60)
import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 200))  # flags=pygame.NOFRAME(убираем рамку), задаем размеры экрана
pygame.display.set_caption('Тестовое название для окошка')  # Задаем название для окошка
icon = pygame.image.load('images/main_logo_pic.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))  # Поверхность с заданными параметрами
square.fill((97, 187, 199))

my_font = pygame.font.Font('fonts/test_font.ttf', 20)  # настройки шрифта
text_surf = my_font.render('Dont touch ENEMY!!!', True, 'red')  # Русский не распознает шрифт
text_lose = my_font.render('LOOSER!!!', True, 'blue')
text_win = my_font.render('WINNER!!! GOOD JOB!!!', True, 'blue')

player = pygame.image.load('images/man.png')
enemy = pygame.image.load('images/enemy.png')

running = True
x = 100
y = 0
x_e = 300
y_e = 100
# count = 0
while running:

    screen.fill('white')
    # screen.blit(square, (20, 30))  # Рисуем обхект через blit
    screen.blit(text_surf, (0, 0))
    screen.blit(player, (x, y))
    screen.blit(enemy, (x_e, y_e))
    # pygame.draw.circle(screen, (30, 36, 89), (250, 50), 30)

    pygame.display.update()  # постоянное обновление приложения

    if x == x_e and y == y_e:
        screen.blit(text_lose, (50, 0))
        running = False
        pygame.quit()
    # elif count == 3:
    #     screen.blit(text_win, (50, 0))
    #     running = False
    #     pygame.quit()

    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 10
                x_e = randint(0, 400)
                y_e = randint(0, 200)
                # count += 1
            elif event.key == pygame.K_LEFT:
                x -= 10
                x_e = randint(0, 400)
                y_e = randint(0, 200)
                # count += 1
            elif event.key == pygame.K_DOWN:
                y += 10
                x_e = randint(0, 400)
                y_e = randint(0, 200)
                # count += 1
            elif event.key == pygame.K_UP:
                y -= 10
                x_e = randint(0, 400)
                y_e = randint(0, 200)
                # count += 1

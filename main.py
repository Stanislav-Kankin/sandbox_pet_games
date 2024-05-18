import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 700))  # flags=pygame.NOFRAME(убираем рамку), задаем размеры экрана
pygame.display.set_caption('Тестовое название для окошка')  # Задаем название для окошка
icon = pygame.image.load('images/main_logo_pic.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 170))  # Поверхность с заданными параметрами
square.fill((97, 187, 199))

my_font = pygame.font.Font('fonts/test_font.ttf', 48)
text_surf = my_font.render('Random text', True, 'red')  # Русский не распознает шрифт

player = pygame.image.load('images/man.png')

running = True
x = 100
y = 0
while running:

    screen.fill('white')
    screen.blit(square, (20, 30))  # Рисуем обхект через blit
    screen.blit(text_surf, (500, 200))
    screen.blit(player, (x, y))
    # pygame.draw.circle(screen, (30, 36, 89), (250, 50), 30)

    pygame.display.update()  # постоянное обновление приложения

    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_UP:
                y -= 10

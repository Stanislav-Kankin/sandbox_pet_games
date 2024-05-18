import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))  # flags=pygame.NOFRAME(убираем рамку), задаем размеры экрана
pygame.display.set_caption('Тестовое название для окошка')  # Задаем название для окошка
icon = pygame.image.load('images/main_logo_pic.png')
pygame.display.set_icon(icon)

running = True
while running:
    screen.fill((50, 168, 64))  # задний фон, заливка

    pygame.display.update()  # постоянное обновление приложения

    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:  # отслеживаем клавиши
                screen.fill((224, 103, 43))

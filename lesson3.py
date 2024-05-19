import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359))  # flags=pygame.NOFRAME(убираем рамку), задаем размеры экрана
pygame.display.set_caption('Тестовое название для окошка')  # Задаем название для окошка
icon = pygame.image.load('images/main_logo_pic.png')
pygame.display.set_icon(icon)

"""
Элементы на экране
"""
bg = pygame.image.load('images/bcg.png')

walk_rigth = [
    pygame.image.load('images/pl_r/first_r.png'),
    pygame.image.load('images/pl_r/second_r.png'),
    pygame.image.load('images/pl_r/third_r.png'),
    pygame.image.load('images/pl_r/fourth_r.png'),
]

walk_left = [
    pygame.image.load('images/pl_l/first.png'),
    pygame.image.load('images/pl_l/second.png'),
    pygame.image.load('images/pl_l/third.png'),
    pygame.image.load('images/pl_l/fourth.png'),
]

player_anim_count = 0
bg_x = 0
bg_sound = pygame.mixer.Sound('sound/bg.mp3')


running = True
bg_sound.play()
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))
    screen.blit(walk_rigth[player_anim_count], (300, 250))

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    bg_x -= 2
    if bg_x == -618:
        bg_x = 0

    pygame.display.update()  # постоянное обновление приложения

    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(15)

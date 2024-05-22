import pygame

# image_path = '/data/data/org.test.myapp_s/files/app/'

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption('Тестовое название для окошка')
icon = pygame.image.load('images/main_logo_pic.png')
pygame.display.set_icon(icon)

"""
Элементы на экране
"""
bg = pygame.image.load('images/bcg.png').convert()
ghost = pygame.image.load('images/ghost1.png').convert_alpha()

bullet = pygame.image.load('images/bullet1.png').convert_alpha()
bullet_list = []
bullet_left = 5


ghost_x = 620

ghost_in_game = []

walk_rigth = [
    pygame.image.load('images/pl_r/first_r.png').convert_alpha(),
    pygame.image.load('images/pl_r/second_r.png').convert_alpha(),
    pygame.image.load('images/pl_r/third_r.png').convert_alpha(),
    pygame.image.load('images/pl_r/fourth_r.png').convert_alpha(),
]

walk_left = [
    pygame.image.load('images/pl_l/first.png').convert_alpha(),
    pygame.image.load('images/pl_l/second.png').convert_alpha(),
    pygame.image.load('images/pl_l/third.png').convert_alpha(),
    pygame.image.load('images/pl_l/fourth.png').convert_alpha(),
]

player_anim_count = 0
bg_x = 0
bg_sound = pygame.mixer.Sound('sound/bg.mp3')
bullet_sound = pygame.mixer.SoundType('sound/pistol.mp3')
dead_sound = pygame.mixer.SoundType('sound/avy.mp3')
jump_sound = pygame.mixer.SoundType('sound/jump.mp3')
game_over_sound = pygame.mixer.SoundType('sound/go.mp3')

player_speed = 5
player_x = 150
player_y = 250

is_jump = False
jump_count = 9

gameplay = True

label = pygame.font.Font('fonts/test_font.ttf', 40)
lose_lable = label.render('You lose!!!', False, 'white')
restart_lable = label.render('Restart?', False, 'red')
restart_label_rect = restart_lable.get_rect(topleft=(180, 200))


running = True
bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2000)

while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(
            player_x, player_y
        ))

        if ghost_in_game:
            for (i, el) in enumerate(ghost_in_game):
                screen.blit(ghost, el)
                el.x -= 15

                if el.x < -10:
                    ghost_in_game.pop(i)

            if player_rect.colliderect(el):
                gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_rigth[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 500:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
                jump_sound.play(0)
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -618:
            bg_x = 0

        if bullet_list:
            for (i, el) in enumerate(bullet_list):
                screen.blit(bullet, (el.x, el.y))
                bullet_sound.play()
                el.x += 10

                if el.x > 630:
                    bullet_list.pop(i)

                if ghost_in_game:
                    for (index, ghost_el) in enumerate(ghost_in_game):
                        if el.colliderect(ghost_el):
                            ghost_in_game.pop(i)
                            bullet_list.pop(i)
                    dead_sound.play()

    else:
        screen.fill('black')
        game_over_sound.play()
        screen.blit(lose_lable, (180, 100))
        screen.blit(restart_lable, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_in_game.clear()
            bullet_list.clear()
            bullet_left = 5

    pygame.display.update()  # постоянное обновление приложения

    for event in pygame.event.get():  # Список всех доступных событий
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_in_game.append(ghost.get_rect(
                topleft=(620, 250)
            ))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullet_left > 0:
            bullet_list.append(bullet.get_rect(topleft=(
                player_x + 30, player_y + 10
            )))
            bullet_left -= 1

    clock.tick(15)

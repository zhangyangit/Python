# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python game, check_event.
'''

import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    '''
    :param event: 响应按键-》按键事件
    :param ship: 飞船对象
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    '''
    :param ai_settings:  设置
    :param screen: 窗口对象
    :param ship: 飞船对象
    :param bullets: 子弹编组
    :return: 产生子弹
    '''
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    '''
    :param event: 响应按键-》按键事件
    :param ship: 飞船对象
    :return:
    '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    '''
    :param ship: 飞船对象
    :return: 响应按键和和鼠标事件
    '''
    # listen the event of input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    '''
    :param stats:
    :param play_button:
    :param mouse_x:
    :param mouse_y:
    :return:  玩家点击
    '''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置统计信息
        stats.reset_stats()
        stats.game_active = True
        # 计分牌
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        # 情况外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建一群外星人
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    '''
    :param ai_settings: 游戏设置
    :param screen: surface 对象
    :param ship: 飞船对象
    :return:
    '''
    # 填充背景色
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    aliens.draw(screen)
    # 显示得分
    sb.show_score()
    # 非活动状态，创建按钮
    if not stats.game_active:
        play_button.draw_button()
    # redraw the screen
    pygame.display.flip()


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # 删除子弹，并新建外星人
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        
        create_fleet(ai_settings, screen, ship, aliens)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''
    :param bullets: 子弹储存编组
    :return: 更新子弹位置，并删除消失子弹
    '''
    # 更新子弹
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 碰撞检测
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    '''
    :param ai_settings:
    :param ship_height:
    :param alien_height:
    :return: 获取可容纳的外星人
    '''
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并加入对列
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    '''
    :param ai_settings:
    :param screen:
    :param aliens:
    :return: 创建外星人群
    '''
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创造第一行的外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    '''
    :param ai_settings:
    :param aliens:
    :return:  检测边缘
    '''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    '''
    :param ai_settings:
    :param aliens:
    :return: 外星人下移
    '''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen,stats, sb, ship, aliens, bullets):
    '''
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return: 外星人撞击ship
    '''
    if stats.ships_left > 0:
        stats.ships_left -= 1
        # 情况外星人和子弹 计分
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        # 创建外星人，飞船底端
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''
    :param aliens:
    :return:更新外星人
    '''
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检测飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    # 检测外星人到底
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    '''
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return: 外星人抵达底端
    '''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 按照飞船撞毁处理
            ship_hit(ai_settings, screen,stats, sb, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    '''检测最高分'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


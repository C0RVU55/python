import pygame

pygame.init()

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면타이틀
pygame.display.set_caption("LDH GAME")

#이벤트루프가 실행되고 있어야 게임이 꺼지지 않음
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생했는가?
            running = False


pygame.quit()
import pygame

pygame.init()

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면타이틀
pygame.display.set_caption("LDH GAME")

#배경 이미지 불러오가
background=pygame.image.load("C:/Users/LeeDahyeon/Desktop/pythonworkspace/pygame_basic/background.png")

#이벤트루프가 실행되고 있어야 게임이 꺼지지 않음
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생했는가?
            running = False
    screen.blit(background, (0,0))
    #또는 RGB값 정해서 채울 수 있음 screen.fill(0, 0, 255)
    pygame.display.update() #배경그리기(매번 겜화면을 다시 그려줘야 함)


pygame.quit()
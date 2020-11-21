import pygame

pygame.init()

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면타이틀
pygame.display.set_caption("LDH GAME")

#배경 이미지 불러오가
background=pygame.image.load("C:/Users/LeeDahyeon/Desktop/pythonworkspace/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character=pygame.image.load("C:/Users/LeeDahyeon/Desktop/pythonworkspace/pygame_basic/character.png")
character_size=character.get_rect().size #이미지크기를 구해옴
character_width=character_size[0] #캐릭터 가로크기
character_height=character_size[1] #캐릭터 세로크기
character_x_pos=(screen_width/2) - (character_width/2) #화면 가로 절반 위치
character_y_pos=screen_height - character_height #화면 세로 크기 가장 아래

#이동할 좌표
to_x=0
to_y=0

#이벤트루프가 실행되고 있어야 게임이 꺼지지 않음
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생했는가?
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5            
            elif event.key == pygame.K_DOWN:
                to_y += 5
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos += to_x
    character_y_pos += to_y

    #가로경계값
    if character_x_pos < 0:
        character_x_pos=0
    elif character_x_pos > screen_width - character_width:
        character_x_pos=screen_width-character_width
    #세로경계값
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos=screen_height-character_height


    screen.blit(background, (0,0)) #배경 그리기 우측 상단 기준으로 (0,0)임
    #또는 RGB값 정해서 채울 수 있음 screen.fill(0, 0, 255)
    screen.blit(character, (character_x_pos,character_y_pos))
    pygame.display.update() #배경그리기(매번 겜화면을 다시 그려줘야 함)
    


pygame.quit()
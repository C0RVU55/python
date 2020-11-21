import pygame

############################################################
#기본 초기화 (필수 요소)
pygame.init()

#화면크기 설정
screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면타이틀
pygame.display.set_caption("LDH GAME")
#frame per second
clock=pygame.time.Clock()
############################################################

#1.사용자 게임 초기화 : 배경화면, 게임 이미지, 캐릭터 좌표, 이속, 시간, 폰트 등)

running=True
while running:
    dt=clock.tick(60) 

    #2.이벤트 처리 : 키보드 ,마우스 등
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생했는가?
            running = False
        
    #3.게임 캐릭터 위치 정의
    character_x_pos += to_x * dt #프레임이 바뀌어도 이속 유지
    character_y_pos += to_y * dt


    #4.충돌처리
    

    #5.화면에 그리기
   

    pygame.display.update() #배경그리기(매번 겜화면을 다시 그려줘야 함)


pygame.quit()
import pygame

pygame.init()

screen_width=480
screen_height=640
screen=pygame.display.set_mode((screen_width, screen_height))

#화면타이틀
pygame.display.set_caption("LDH GAME")
#frame per second
clock=pygame.time.Clock()

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
#이속
character_speed = 0.5

#적
enemy=pygame.image.load("C:/Users/LeeDahyeon/Desktop/pythonworkspace/pygame_basic/enemy.png")
enemy_size=enemy.get_rect().size #이미지크기를 구해옴
enemy_width=enemy_size[0] #캐릭터 가로크기
enemy_height=enemy_size[1] #캐릭터 세로크기
enemy_x_pos=(screen_width/2) - (enemy_width/2) #화면 가로 절반 위치
enemy_y_pos=(screen_height/2) - (enemy_height/2) #화면 세로 크기 가장 아래

#폰트 정의
game_font=pygame.font.Font(None, 40) #폰트 객체 생성(폰트, 크기)
total_time=10 #총 시간
start_ticks=pygame.time.get_ticks() #시작 시간 : 시작 tick을 받아옴/현재 틱에서 시간을 빼는 식으로 계산

#이벤트루프가 실행되고 있어야 게임이 꺼지지 않음
running=True
while running:
    dt=clock.tick(60) #델타 = 초당 프레임수 30
    #프레임 표시법 > print("fps:"+str(clock.get_fps()))
    for event in pygame.event.get():#어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생했는가?
            running = False
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed            
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x=0
            elif event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                to_y=0

    character_x_pos += to_x * dt #프레임이 바뀌어도 이속 유지
    character_y_pos += to_y * dt

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

    #충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos

    #충돌체크
    if character_rect.colliderect(enemy_rect): #colliderect 사각형과 부딪히는 거 보는 함수?
        print("충돌했습니다")
        running=False


    screen.blit(background, (0,0)) #배경 그리기 우측 상단 기준으로 (0,0)임
    #또는 RGB값 정해서 채울 수 있음 screen.fill(0, 0, 255)
    screen.blit(character, (character_x_pos,character_y_pos))
    #그냥 이미지를 그리기만 할뿐 액팅이 반영되지는 않음
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    
    #타이머 넣기 : 경과 시간 계산, 기본이 분당초(ms)?이기 때문에 1000으로 나눠서 초(s)단위로 표시 
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    #render는 타이머를 그리는 거 / render(출력할 글자, True, 글자색상)
    timer=game_font.render(str(int(total_time-elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))
    #시간 0밑으로 안 내려가게 하기
    if total_time-elapsed_time <=0:
        print("타임 오버")
        running=False

    pygame.display.update() #배경그리기(매번 겜화면을 다시 그려줘야 함)

#잠시 대기 : 2초 정도 대기 (ms)라서 1000곱한 값
pygame.time.delay(2000) 
#pygame 종료
pygame.quit()
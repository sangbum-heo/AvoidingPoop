import pygame
import random

# pygame 초기화
pygame.init()

# FPS 설정
clock = pygame.time.Clock()

# 게임 이름
pygame.display.set_caption("YUMMY DDONG")

# sound
bgm = pygame.mixer.Sound("./resources/Someday_Roa.ogg")
bgm.set_volume(0.5)
bgm.play(-1)

# bgm이 현재 틀어져있나 체크하는 변수
bgm_i=1

# sound files

ks_sound = pygame.mixer.Sound("./resources/fart.ogg")

dead_sound = pygame.mixer.Sound("./resources/fart_sound.ogg")

ddong_sound = pygame.mixer.Sound("./resources/pop.ogg")

hb_sound = pygame.mixer.Sound("./resources/heartbeat.ogg")

bgm_end = pygame.mixer.Sound("./resources/country_end.ogg")

barking = pygame.mixer.Sound("./resources/barking.ogg")

# 폰트 설정
game_font = pygame.font.Font(None, 50)
game_font2 = pygame.font.Font(None, 70)
game_font3 = pygame.font.Font(None, 25)

#나의 이름
my_name = game_font3.render("Heo Sangbum", True, (255, 255, 255))

the_end = game_font2.render("THE END",True,(0,0,0))

date = game_font3.render("2020-12-09",True,(255,255,255))

# screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# background
background = pygame.image.load("./resources/bg2.png")
background_size = background.get_rect().size
background_width = background_size[0]
background_height = background_size[1]
bg = [pygame.image.load("./resources/bg2.png"),
      pygame.image.load("./resources/bg21.png"),
      pygame.image.load("./resources/bg22.png"),
      pygame.image.load("./resources/bg23.png"),
      pygame.image.load("./resources/bg25.png")]

# title background
t_background = pygame.image.load("./resources/astro_2_2.jpg")
t_background_size = t_background.get_rect().size
t_background_width = t_background_size[0]
t_background_height = t_background_size[1]

# ending background
e_background = pygame.image.load("./resources/end_0.jpg")

# help background
h_background = pygame.image.load("./resources/astro_help6.jpg")

h_run = False
run_ending = False

# character image
character_left = pygame.image.load("./resources/dog4.png")
character_right = pygame.image.load("./resources/dog3.png")

# ddong * 6
ddong = [0, 0, 0, 0, 0, 0]
ddong_size = [0, 0, 0, 0, 0, 0]
ddong_x_pos = [0, 0, 0, 0, 0, 0]
ddong_y_pos = [0, 0, 0, 0, 0, 0]
ddong_width = 0
ddong_height = 0
ddong1 = pygame.image.load("./resources/ddong.png")
ddong3 = pygame.image.load("./resources/ddong3.png")
ddong4 = pygame.image.load("./resources/ddong4.png")
ddong5 = pygame.image.load("./resources/ddong5.png")

ddong_speed = [0.5, 0.6, 0.7, 0.8, 0.9]

bk=0
###########################################################################################
# 타이틀 화면부터 결과 화면을 반복
run_last = 0
run_all = True
while run_all:
    if bgm_i==0:
        bgm.play(-1)
        bgm_i=1
    bgm_end.stop()
    bgm_e=0
    score = 0

    # 상하 방향키로 선택을 도와주는 변수 (key select)
    ks = 0

    # 타이틀 화면
    run = True
    running = True
    while run:

        for event in pygame.event.get():

            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                run = False
                running = False
                run_all = False

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:

                # ESC 키로 종료
                if event.key == pygame.K_ESCAPE:
                    run = False
                    running = False
                    run_all = False

                # 아래 방향키를 누르면
                if event.key == pygame.K_DOWN:
                    ks_sound.play()
                    if ks < 2:
                        ks += 1
                    print("ks :", ks)
                # 위 방향키를 누르면
                if event.key == pygame.K_UP:
                    ks_sound.play()
                    if ks > 0:
                        ks -= 1
                    print("ks :", ks)

                # 엔터 키를 누르면 ks 값에 따라 다음 화면으로 넘어감
                if event.key == pygame.K_RETURN:
                    ks_sound.play()
                    if ks == 0:
                        run = False
                    if ks == 1:
                        h_run = True
                        run = False
                    if ks == 2:
                        run = False
                        running = False
                        run_all = False
                        h_run = False
                    
        screen.blit(t_background, (0, 0))

        #메뉴 기본 폰트 설정
        start_button = game_font.render("START", True, (255, 255, 255))
        help_button = game_font.render("HELP",True, (255, 255, 255))
        quit_button = game_font.render("QUIT", True, (255, 255, 255))

        # ks의 값(상하 방향키로 선택한 메뉴 파란색으로 강조)
        if ks == 0:
            start_button = game_font2.render("START", True, (154, 218, 255))

        elif ks == 1:
            help_button = game_font2.render("HELP",True, (154, 218, 255))

        elif ks == 2:
            quit_button = game_font2.render("QUIT", True, (154, 218, 255))

        #각 글자들을 화면 중앙에 배치하기 위해 길이를 구해준다
        start_button_size = start_button.get_rect().size
        start_button_width = start_button_size[0]

        help_button_size = help_button.get_rect().size
        help_button_width = help_button_size[0]

        quit_button_size = quit_button.get_rect().size
        quit_button_width = quit_button_size[0]

        #screen blit
        screen.blit(my_name, (340, 600))
        screen.blit(date,(17,600))
        screen.blit(start_button, ((screen_width / 2) - (start_button_width / 2), 150))
        screen.blit(help_button, ((screen_width / 2) - (help_button_width / 2), 257))
        screen.blit(quit_button, ((screen_width / 2) - (quit_button_width / 2), 365))

        pygame.display.update()

###########################################################
#help 화면
    while h_run:

        for event in pygame.event.get():
    
            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                running = False
                run_all = False
                h_run = False

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:
                ks_sound.play()

                # ESC 키로 종료
                if (event.key == pygame.K_ESCAPE) or (event.key == pygame.K_RETURN):
                    h_run = False
                    running = False

        screen.blit(h_background,(0,0))

        pygame.display.update()

    ###############################################################################
    # 게임 시작
    # 좌 or 우 방향키를 누른 채로 들어왔을 때 오류 방지용 변수
    kr = 0
    kl = 0

    # 급똥 방지 ( 똥 갑툭튀 방지)
    dd=0

    # 심장소리 한 번만 들리게
    hb=0

    # 다음 게임을 위한 초기화
    # character
    character = pygame.image.load("./resources/dog3.png")
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (background_width / 2) - (character_width / 2)
    character_y_pos = background_height - character_height
    character_speed = 0.4
    to_go = 0
    bg_index = 0
    k = [0, 0, 0, 0, 0, 0]
    ddong_rect = [0, 0, 0, 0, 0, 0]

    for i in range(6):
        ddong[i] = pygame.image.load("./resources/ddong.png")
        ddong_size[i] = ddong[i].get_rect().size
        ddong_width = ddong_size[0][0]
        ddong_height = ddong_size[0][1]
        ddong_x_pos[i] = random.randrange(screen_width - ddong_width)
        ddong_y_pos[i] = 0 - (screen_height / 2)

    to_go = 0

    # running=True
    elapsed_time = 0

    # 시작 시간(기준 시간)을 틱으로 받아옴 (ms)
    start_ticks = pygame.time.get_ticks()

    # while running
    while running:
        dt = clock.tick(60)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

        # pygame에서 이벤트를 받을 수 있게 만들기 (이벤트 처리)
        for event in pygame.event.get():

            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                running = False
                run_all = False

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:

                # ESC 키로 종료
                if event.key == pygame.K_ESCAPE:
                    running = False
                    run_all = False

                if event.key == pygame.K_SPACE:
                    barking.play()

                # 왼쪽 키가 눌리면
                if event.key == pygame.K_LEFT:
                    kl = 1
                    to_go -= character_speed
                    print("왼쪽 눌림")
                    character = character_left
                # 오른쪽 키가 눌리면
                if event.key == pygame.K_RIGHT:
                    kr = 1
                    to_go += character_speed
                    print("오른쪽 눌림")
                    character = character_right

            # 키에서 손을 떼는 이벤트
            if event.type == pygame.KEYUP:

                # 왼쪽 키를 떼면
                if event.key == pygame.K_LEFT:
                    if kl == 1:
                        to_go += character_speed
                        print("왼쪽 뗌")
                    kl = 0

                # 오른쪽 키를 떼면
                if event.key == pygame.K_RIGHT:
                    if kr == 1:
                        to_go -= character_speed
                        print("오른쪽 뗌")
                    kr = 0

        # 캐릭터의 x 포지션은 to_go의 값만큼 상시 이동
        character_x_pos += to_go * dt
        if character_x_pos >= screen_width - character_width:
            character_x_pos = screen_width - character_width
        if character_x_pos <= 0:
            character_x_pos = 0

        for i in range(5):
            ddong_rect[i] = ddong[0].get_rect()
            ddong_rect[i].left = ddong_x_pos[i]
            ddong_rect[i].top = ddong_y_pos[i]

        # ddong의 낙하 (시간이 지남에 따라 최대 5개)
        for i in range(int(elapsed_time/5)+1):

            # out of index 방지
            if i >= 5:
                continue
                print("컨티뉴 실행")
            # 각 똥들의 위치 데이터를 리스트에 저장
            ddong_y_pos[i] += (ddong_speed[i] * dt) + (elapsed_time / 10)
            if ddong_y_pos[i] > screen_height - ddong_height:
                if dd==1:
                    if k[i] == 0:
                        ddong_sound.play()
                        k[i] = 1
                        ddong[i] = ddong5
                        
                ddong_rect[i] = ddong[5].get_rect()

            if ddong_y_pos[i] >= screen_height:
                ddong_x_pos[i] = random.randrange(screen_width - ddong_width)
                ddong_y_pos[i] = 0 - ddong_height
                ddong[i] = ddong1
                k[i] = 0

        # get rect (충돌 감지를 위해 직사각형 모양의 데이터 필요)
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        # 똥 갑툭튀 충돌 방지
        if dd==0:
            for i in range(5):
                ddong_y_pos[i] = 0 - ddong_height

        # collision ( colliderect ) 충돌
        for i in range(5):
            if dd==1:
                if character_rect.colliderect(ddong_rect[i]):
                    dead_sound.play()
                    running = False
                    run_last = True
                    score = int(elapsed_time)
                    print(score)
        dd=1

        # 배경 빨간 테두리
        if int(elapsed_time/5) >= 5:
            bg_idx = 4
        else:
            bg_index = int(elapsed_time/5)
        background = bg[bg_index]

        # screen blits
        screen.blit(background, (0, 0))

        timer = game_font.render(str(int(elapsed_time)), True, (0, 0, 0))

        stage = game_font.render(
            "STAGE "+str(int(elapsed_time/5)+1), True, (0, 0, 0))

        # STAGE 5가 되면 글씨를 빨간색으로 바꾸고 STAGE 5에서 더 이상 올라가지 않음
        if int(elapsed_time) >= 20:
            stage = game_font.render("STAGE "+str(5), True, (255, 0, 0))

        screen.blit(timer, (10, 10))

        screen.blit(stage, (320, 10))

        screen.blit(character, (character_x_pos, character_y_pos))

        for i in range(5):
            screen.blit(ddong[i], (ddong_x_pos[i], ddong_y_pos[i]))
        if hb==0:
            if int(elapsed_time) >= 20:
                hb_sound.play(-1)
                hb=1

        # 30초가 되면 엔딩 화면으로 넘어감
        if int(elapsed_time) >= 30:
            running=False
            run_ending=True

        pygame.display.update()
    ##################################################################
    # your score 화면
    while run_last:
        hb_sound.stop()
        for event in pygame.event.get():

            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                run_all = False
                run_last = False

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:

                # ESC 키로 종료
                if event.key == pygame.K_ESCAPE:
                    run_all = False
                    run_last = False

                if event.key == pygame.K_RETURN:
                    run_last = False

        screen.blit(t_background, (0, 0))
        sc = "Your Score :  "+str(score)
        your_score = game_font2.render(sc, True, (255, 255, 255))

        screen.blit(your_score, (60, 200))

        screen.blit(my_name, (340, 600))

        pygame.display.update()
    ###########################################################################
    # 엔딩 화면  귀여운 짖는 소리와 따뜻한 가정에 강아지가 있는 분위기
    up=0
    while run_ending:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        hb_sound.stop()
        bgm.stop()
        bgm_i=0
        if bgm_e == 0:
            bgm_end.play(-1)
            bgm_e=1
            barking.play()
            character = character_left
            character_x_pos=480
            character_y_pos=572

        for event in pygame.event.get():
    
            # X 버튼으로 프로그램 종료
            if event.type == pygame.QUIT:
                run_all = False
                run_ending = False

            # 키보드 입력 받기
            if event.type == pygame.KEYDOWN:

                # ESC 키로 종료
                if event.key == pygame.K_ESCAPE:
                    run = False
                    run_ending = False

                if event.key == pygame.K_RETURN:
                    run = False
                    run_ending = False
                    
        # 강아지가 뛰어오는 모습 구현
        if character_x_pos >= 250:
            character_x_pos-=0.05
        elif ((int(elapsed_time)+1) % 4 ==0) and bk==0:
            barking.play()
            bk=1
        elif ((int(elapsed_time)+1) % 4 ==1):
            bk=0
        
        # 강아지 점프 구현
        if up % 1000 <= 500:
            character_y_pos -= 0.02
        else:
            character_y_pos += 0.02
        up+=1

        screen.blit(e_background,(0,0))

        screen.blit(character,(character_x_pos,character_y_pos))

        screen.blit(the_end,(130,screen_height/2 -50))

        pygame.display.update()

pygame.quit()
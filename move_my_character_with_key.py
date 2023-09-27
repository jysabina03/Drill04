from pico2d import *

TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEICHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():
    global running
    global dir_x, dir_y, dir_see
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key==SDLK_UP:
                dir_y+=1
            elif event.key==SDLK_DOWN:
                dir_y-=1
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dir_x -= 1
                dir_see = 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
                dir_see = -1
            elif event.key==SDLK_UP:
                dir_y-=1
            elif event.key==SDLK_DOWN:
                dir_y+=1


        # fill here


running = True
x = 800 // 2
y=800//2
frame_see,frame_run,frame_up,frame_down=0,0,0,0
dir_x,dir_y=0,0
dir_see = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

    x += dir_x*10
    y += dir_y*10
    if x<0 or x>TUK_WIDTH:
        x-=dir_x*10
    if y<0 or y>TUK_HEICHT:
        y-=dir_y*10
        
    if dir_x == 0 and dir_y == 0:   # 대기 상태
        if dir_see == 1:
            character.clip_draw(29*frame_see,848,29,30,x,y,100,100)
        elif dir_see == -1:
            character.clip_composite_draw(29*frame_see,848,29,30,0,'h',x,y,100,100)
        frame_see = (frame_see + 1) % 10
    elif dir_x>0:   # 오른쪽으로 이동
        if frame_run <= 6:
            character.clip_draw(26 * frame_run, 701, 26, 30, x, y, 100, 100)
        elif frame_run<=10:
            character.clip_draw(26*6+(frame_run-7)*31,701,31,30,x,y,100,100)
        elif frame_run>10:
            character.clip_draw(26*6+31*4+26*(frame_run-11),701,26,30,x,y,100,100)
        frame_run = (frame_run + 1) % 12
    elif dir_x<0:   # 왼쪽으로 이동
        if frame_run <= 6:
            character.clip_composite_draw(26 * frame_run, 701, 26, 30,0,'h', x, y, 100, 100)
        elif frame_run <= 10:
            character.clip_composite_draw(26 * 6 + (frame_run - 7) * 31, 701, 31, 30,0,'h',x, y, 100, 100)
        elif frame_run > 10:
            character.clip_composite_draw(26 * 6 + 31 * 4 + 26 * (frame_run - 11), 701, 26, 30,0,'h',x, y, 100, 100)
        frame_run = (frame_run + 1) % 12
    elif dir_y > 0:  # 위로 이동
        character.clip_draw(24 * frame_up, 463, 24, 30, x, y, 100, 100)
        frame_up = (frame_up + 1) % 10
    elif dir_y < 0:  # 아래로 이동
        if dir_see == 1:
            character.clip_draw(29 * frame_down, 213, 29, 30, x, y, 100, 100)
        elif dir_see == -1:
            character.clip_composite_draw(29*frame_down,213,29,30,0,'h',x,y,100,100)

        frame_down = (frame_down + 1) % 10


    # 그리기
    update_canvas()
    handle_events()
    delay(0.1)

# fill here


close_canvas()


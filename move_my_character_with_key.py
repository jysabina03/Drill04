from pico2d import *

TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas(TUK_WIDTH,TUK_HEICHT)
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():
    global running
    global dirx,diry,dir_see
    # fill here

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= -1
            elif event.key==SDLK_UP:
                diry+=1
            elif event.key==SDLK_DOWN:
                diry-=1
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dirx -= 1
                dir_see = 1
            elif event.key == SDLK_LEFT:
                dirx += -1
                dir_see = -1
            elif event.key==SDLK_UP:
                diry-=1
            elif event.key==SDLK_DOWN:
                diry+=1


        # fill here


running = True
x = 800 // 2
y=800//2
frame_see,frame_run,frame_up,frame_down=0,0,0,0
dirx,diry=0,0
dir_see = 1

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

    if dirx == 0 and diry == 0:
        if dir_see == 1:
            character.clip_draw(29*frame_see,848,29,30,x,y,100,100)
        frame_see = (frame_see + 1) % 10
    elif dirx>0:
        if frame_run <= 6:
            character.clip_draw(26 * frame_run, 701, 26, 30, x, y, 100, 100)
        elif frame_run<=10:
            character.clip_draw(26*6+(frame_run-7)*31,701,31,30,x,y,100,100)
        elif frame_run>10:
            character.clip_draw(26*6+31*4+26*(frame_run-11),701,26,30,x,y,100,100)
        frame_run = (frame_run + 1) % 12
    elif dirx<0:
        if frame_run <= 6:
            character.clip_composite_draw(26 * frame_run, 701, 26, 30, x, y, 100, 100)
            character.clip_draw(26 * frame_run, 701, 26, 30, x, y, 100, 100)
        elif frame_run <= 10:
            character.clip_draw(26 * 6 + (frame_run - 7) * 31, 701, 31, 30, x, y, 100, 100)
        elif frame_run > 10:
            character.clip_draw(26 * 6 + 31 * 4 + 26 * (frame_run - 11), 701, 26, 30, x, y, 100, 100)
        frame_run = (frame_run + 1) % 12

    # 그리기

    update_canvas()
    handle_events()
    x+=dirx*7
    y+=diry*7
    delay(0.1)

# fill here


close_canvas()


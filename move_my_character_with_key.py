from pico2d import *

TUK_WIDTH,TUK_HEICHT=1280,1024
open_canvas()
character = load_image('animation_sheet.png')
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():
    global running
    global dirx,diry
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
            elif event.key == SDLK_LEFT:
                dirx += -1
            elif event.key==SDLK_UP:
                diry-=1
            elif event.key==SDLK_DOWN:
                diry+=1


        # fill here


running = True
x = 800 // 2
y=800//2
frame_run,frame_up,frame_down=0,0,0
dirx,diry=0,0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEICHT//2)

    # 그리기

    update_canvas()
    handle_events()
    x+=dirx*7
    y+=diry*7
    delay(0.05)

# fill here


close_canvas()


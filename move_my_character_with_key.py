from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('dril4.png')

def handle_events():
    global running, UDdir, RLdir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                RLdir += 1
            elif event.key == SDLK_LEFT:
                RLdir -= 1
            elif event.key == SDLK_UP:
                UDdir += 1
            elif event.key == SDLK_DOWN:
                UDdir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                RLdir -= 1
            elif event.key == SDLK_LEFT:
                RLdir += 1
            elif event.key == SDLK_UP:
                UDdir -= 1
            elif event.key == SDLK_DOWN:
                UDdir += 1




x = 800 // 2
y = 800 // 2
running = True
frame = 0
hide_cursor()
UDdir = 0
RLdir = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if UDdir == 0 and RLdir == 0:
        character.clip_draw(frame * 60, 180, 60, 60, x, y, 120, 120)
    elif RLdir == 1:
        character.clip_draw(frame * 60, 60, 60, 60, x, y,120,120)
    elif RLdir == -1:
        character.clip_composite_draw(frame * 60, 60, 60, 60, 0, 'h', x, y, 120, 120)
    elif UDdir == 1:
        character.clip_draw(frame * 60, 0, 60, 60, x, y, 120, 120)
    elif UDdir == -1:
        character.clip_draw(frame * 60, 180, 60, 60, x, y, 120, 120)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += RLdir * 20
    y += UDdir * 20
    if x >= 1280-50:
        x = 1280-50
    if y >= 1024-50:
        y = 1024-50
    if x <= 0:
        x = 20
    if y <= 0:
        y = 0

    delay(0.1)
import sounddevice as sd
import numpy as np
from pygame import *
from random import randint

sr = 16000
block = 256
mic_level = 0.0

def audio_callback(indata, frames, time_info, status):
    global mic_level
    if status:
        return
    rms = float(np.sqrt(np.mean(indata**2)))
    mic_level = 0.85 * mic_level * 0.15 * rms

init()
wn_sz = 1200, 800
screen = display.set_mode((wn_sz))
clock = time.Clock()

player_rect = Rect(150, 300, 100, 100 )
runnin = True
while running:
    for e in event.get():
        if e.type == QUET:
            running = False
    screen.fill((0, 0, 0))

def generate_pipes(count,pipe_width=140, gep=280, min_heiht = 50, max_height=450, distasnce=500)
    pipes = []
    srtart_x = window_size[0]
    for i in range(count)
        height = randint(min_heiht = 50, max_height=450)
        top_pipe = Rect(start_x, 0, pipe_width, height)
        bottom_pipe = Rect(stert_x, height + gap, pipe_width, wn_sz[1] - (height + gap))
        pipes.append([top_pipe, bottom_pipe])
        start_x += distance
    return pipes

pipes = generate_pipes(150)
main_font= font.Font(None, 100)
score = 0
lose = False
wait = 40
y_vel =0.0
gravity = 0.6
THRESH = 0.001
IMPULSE = -8.0

with sd.InputStream(samplerate=sr, channels=1, blocksize=block, callback=audio_cb):
    while True:
        for e in event.get():
            if e.type == QUIT:
                quit()

        # ЛОГІКА РУХУ
        # якщо голос гучніший за поріг — робимо "стрибок"
        if mic_level > THRESH:
            y_vel = IMPULSE

        y_vel += gravity
        player_rect.y += int(y_vel)

        window.fill('sky blue')
        draw.rect(window, 'red', player_rect)

        for pie in pies[:]:
            if not lose:
                pie.x -= 10
            draw.rect(window, 'green', pie)
            if pie.x <= -100:
                pies.remove(pie)
                score += 0.5

            if player_rect.colliderect(pie):
                lose = True

            if len(pies) < 8:
                pies += generate_pipes(150)

            score_text = main_font.render(f'{int(score)}', 1, 'black')
            window.blit(score_text, (window_size[0] // 2 - score_text.get_rect().w // 2, 40))


    display.update()
    clock.tick(60)
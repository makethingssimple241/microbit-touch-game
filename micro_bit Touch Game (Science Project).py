from microbit import *
import music

music.set_built_in_speaker_enabled(False)
basic.pause(3000)

score = 0
countdown = 4
basic.pause(1500)
while countdown > 1:
    countdown -= 1
    basic.show_number(countdown)
    music.play_tone(Note.C, music.beat(BeatFraction.WHOLE))
    basic.clear_screen()
    basic.pause(1000)
basic.show_leds("""
. . # . .
. . . # .
# # # # #
. . . # .
. . # . .
""")
level = 0
basic.clear_screen()

forhit_x = 0
forhit_y = 0

level = 1

hit_x = randint(0, 4)
led.plot(hit_x, 4)

def gameend():
    if level == 3:
        basic.show_number(score)
        music.play_tone(Note.C, music.beat(BeatFraction.WHOLE))
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.pause(1000)

while level < 3:
    music.set_tempo(100)
    def scorecount():
        global score
        if forhit_y == 3 and forhit_x == hit_x:
            score += 1
            if score == 6:
                levelup()
            elif score == 12:
                global level
                level += 1
        else:
            pass
    forhit_x = randint(0, 4)
    forhit_y = randint(0, 3)
    led.unplot(0, 0)
    led.plot(forhit_x, forhit_y)
    basic.pause(2000/level)
    led.unplot(forhit_x, forhit_y)
    def control_lr():
        def on_button_pressed_a(): # left
            global hit_x
            for i in range (1, 6):
                led.unplot(i-1, 4)
            if hit_x <= 0:
                hit_x = 4
            else:
                hit_x -= 1
            led.plot(hit_x, 4)
        input.on_button_pressed(Button.A, on_button_pressed_a)
        def on_button_pressed_b(): # right
            global hit_x
            for i in range (1, 6):
                led.unplot(i-1, 4)
            if hit_x >= 4:
                hit_x = 0
            else:
                hit_x += 1
            led.plot(hit_x, 4)
        input.on_button_pressed(Button.B, on_button_pressed_b)
    control.in_background(control_lr)
    scorecount()
def levelup():
    global level
    level += 1
    basic.show_string("L2")
    pins.digital_write_pin(DigitalPin.P1, 1)
    basic.pause(1000)
    basic.clear_screen()
    pins.digital_write_pin(DigitalPin.P1, 0)
    hit_x = randint(0, 4)
    led.plot(hit_x, 4)
gameend()
def on_received_number(receivedNumber):
    if active and not (send):
        if radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH) != -75:
            led.plot_bar_graph(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
                100)
            music.play_tone(Math.map(radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH),
                    0,
                    100,
                    131,
                    988),
                music.beat(BeatFraction.WHOLE))
        else:
            basic.show_icon(IconNames.ASLEEP)
            music.ring_tone(784)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global send
    send = not (send)
    if send:
        basic.show_icon(IconNames.YES)
    else:
        basic.show_icon(IconNames.NO)
input.on_button_pressed(Button.A, on_button_pressed_a)

def doSomething():
    global active
    active = False
    basic.show_arrow(ArrowNames.EAST)
    while not (input.button_is_pressed(Button.B)):
        basic.pause(1)
    active = True
    basic.clear_screen()

def on_button_pressed_ab():
    doSomething()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

active = False
send = False
music.set_volume(255)
send = False
doSomething()

def on_forever():
    if not (active):
        music.stop_all_sounds()
basic.forever(on_forever)

def on_forever2():
    if send and active:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
        music.ring_tone(349)
        basic.show_leds("""
            . . . . .
                        . . # . .
                        . # . # .
                        . . # . .
                        . . . . .
        """)
        music.ring_tone(698)
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . . . #
                        . # . # .
                        . . # . .
        """)
        music.ring_tone(175)
basic.forever(on_forever2)

def on_forever3():
    if send and active:
        radio.send_number(0)
basic.forever(on_forever3)

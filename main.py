radio.set_group(123)
ball = False

def on_received_number(receivedNumber):
    global ball
    if receivedNumber == 0:
        ball = True
    else:
        ball = False
radio.on_received_number(on_received_number)

T

def on_gesture_shake():
    global ball
    radio.send_number(0)
    ball = False
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if ball == True:
        basic.show_leds("""
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            """)
    if ball == False:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
basic.forever(on_forever)

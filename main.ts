radio.setGroup(123)
let ball = false

radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 0) {
        ball = true
    } else {
        ball = false
    }
})

input.onGesture(Gesture.Shake, function () {
    radio.sendNumber(0)
    ball = false
})

basic.forever(function () {
    if (ball == true) {
        basic.showLeds(`
            . # # # .
            # . . . #
            # . . . #
            # . . . #
            . # # # .
            `)
    }
    if (ball == false) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
})

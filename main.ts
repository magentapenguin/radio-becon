radio.onReceivedNumber(function (receivedNumber) {
    if (active && !(send)) {
        if (radio.receivedPacket(RadioPacketProperty.SignalStrength) > 0) {
            led.plotBarGraph(
            radio.receivedPacket(RadioPacketProperty.SignalStrength),
            100
            )
            music.playTone(Math.map(radio.receivedPacket(RadioPacketProperty.SignalStrength), 0, 100, 131, 988), music.beat(BeatFraction.Whole))
        } else {
            basic.showIcon(IconNames.Asleep)
            music.ringTone(988)
        }
    }
})
input.onButtonPressed(Button.A, function () {
    send = !(send)
    if (send) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
function doSomething () {
    active = false
    basic.showArrow(ArrowNames.East)
    while (!(input.buttonIsPressed(Button.B))) {
        basic.pause(1)
    }
    active = true
    basic.clearScreen()
}
input.onButtonPressed(Button.AB, function () {
    doSomething()
})
let active = false
let send = false
music.setVolume(255)
send = false
doSomething()
basic.forever(function () {
    if (!(active)) {
        music.stopAllSounds()
    }
})
basic.forever(function () {
    if (send && active) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
        music.ringTone(349)
        basic.showLeds(`
            . . . . .
            . . # . .
            . # . # .
            . . # . .
            . . . . .
            `)
        music.ringTone(698)
        basic.showLeds(`
            . . # . .
            . # . # .
            # . . . #
            . # . # .
            . . # . .
            `)
        music.ringTone(175)
    }
})
basic.forever(function () {
    if (send && active) {
        radio.sendNumber(0)
    }
})

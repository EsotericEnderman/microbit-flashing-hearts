basic.forever(function on_forever() {
    basic.showIcon(IconNames.Heart, 500)
    basic.clearScreen()
    basic.pause(500)
    basic.showLeds(`
    . . . . .
    . # # # .
    . # # # .
    . . # . .
    . . . . .
    `)
    basic.clearScreen()
    basic.pause(500)
    basic.showIcon(IconNames.SmallHeart, 500)
    basic.clearScreen()
    basic.pause(500)
    
})

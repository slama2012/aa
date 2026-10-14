basic.forever(function () {
    if (input.lightLevel() < 150) {
        basic.showString("N")
    } else {
        basic.showString("J")
    }
})

def on_forever():
    if input.light_level() < 150:
        basic.show_string("N")
    else:
        basic.show_string("J")
    basic.pause(5000)
basic.forever(on_forever)

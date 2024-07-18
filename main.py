def on_forever():
    basic.show_icon(IconNames.HEART, 250)
    basic.clear_screen()
    basic.pause(2000)

basic.forever(on_forever)

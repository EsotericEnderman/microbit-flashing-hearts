def on_forever():
    basic.show_icon(IconNames.HEART, 500)
    basic.clear_screen()
    basic.pause(500)

    basic.show_leds("""
    . . . . .
    . # # # .
    . # # # .
    . . # . .
    . . . . .
    """)
    basic.clear_screen()
    basic.pause(500)

    basic.show_icon(IconNames.SMALL_HEART, 500)
    basic.clear_screen()
    basic.pause(500)
    pass

basic.forever(on_forever)

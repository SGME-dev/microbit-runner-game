def on_button_pressed_a():
    if game.is_paused():
        game.resume()
        basic.show_string("Unpaused")
        return
    game.pause()
    basic.show_string("Paused")
input.on_button_pressed(Button.A, on_button_pressed_a)

# Handler for tilting left

def on_gesture_tilt_left():
    player.move(-1)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

# Handler for Button B press

def on_button_pressed_b():
    player.turn(Direction.RIGHT, 90)
    basic.pause(100)
    player.move(-0.5)
    basic.pause(100)
    player.move(-0.5)
    basic.pause(100)
    player.move(-0.5)
    basic.pause(100)
    player.move(-0.5)
    basic.pause(100)
    player.move(0.5)
    basic.pause(100)
    player.move(0.5)
    basic.pause(100)
    player.move(0.5)
    basic.pause(100)
    player.move(0.5)
    player.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)



# --- Event Handlers (Registered only once) ---
# Handler for tilting right

def on_gesture_tilt_right():
    player.move(1)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

player: game.LedSprite = None
# Initialize the player sprite
player = game.create_sprite(2, 2)
player1 = game.create_sprite(1, 3)
player2 = game.create_sprite(2, 3)
player3 = game.create_sprite(3, 3)
player4 = game.create_sprite(4, 3)
player5 = game.create_sprite(3, 3)
player6 = game.create_sprite(0, 5)
player7 = game.create_sprite(1, 5)
player8 = game.create_sprite(2, 5)
player9 = game.create_sprite(3, 5)
player10 = game.create_sprite(4, 5)
player11 = game.create_sprite(5, 5)
player12 = game.create_sprite(0, 3)
score = int("0")
wall1 = game.create_sprite(6, 2)

def on_forever():
    if player.is_touching(wall1):
        wall1.delete()
        game.game_over()
        wall1.delete()
    else:
        pass
basic.forever(on_forever)

# --- Main Program Loop (Runs forever, but no longer redraws static background) ---
# Start the forever loop

def on_forever2():
    if game.is_game_over():
        return
    basic.pause(400)
    wall1.move(-1)
    basic.pause(400)
    wall1.move(-1)
    basic.pause(400)
    wall1.move(-1)
    basic.pause(400)
    wall1.move(-1)
    basic.pause(400)
    wall1.move(-1)
    basic.pause(400)
    game.add_score(1)
    wall1.change(LedSpriteProperty.X, 5)
basic.forever(on_forever2)

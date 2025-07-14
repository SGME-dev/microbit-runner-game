input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (game.isPaused()) {
        game.resume()
        basic.showString("Unpaused")
        return
    }
    
    game.pause()
    basic.showString("Paused")
})
//  Handler for tilting left
input.onGesture(Gesture.TiltLeft, function on_gesture_tilt_left() {
    player.move(-1)
})
//  Handler for Button B press
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    player.turn(Direction.Right, 90)
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
    player.turn(Direction.Left, 90)
})
//  --- Event Handlers (Registered only once) ---
//  Handler for tilting right
input.onGesture(Gesture.TiltRight, function on_gesture_tilt_right() {
    player.move(1)
})
let player : game.LedSprite = null
//  Initialize the player sprite
player = game.createSprite(2, 2)
let player1 = game.createSprite(1, 3)
let player2 = game.createSprite(2, 3)
let player3 = game.createSprite(3, 3)
let player4 = game.createSprite(4, 3)
let player5 = game.createSprite(3, 3)
let player6 = game.createSprite(0, 5)
let player7 = game.createSprite(1, 5)
let player8 = game.createSprite(2, 5)
let player9 = game.createSprite(3, 5)
let player10 = game.createSprite(4, 5)
let player11 = game.createSprite(5, 5)
let player12 = game.createSprite(0, 3)
let score = parseInt("0")
let wall1 = game.createSprite(6, 2)
basic.forever(function on_forever() {
    if (player.isTouching(wall1)) {
        wall1.delete()
        game.gameOver()
        wall1.delete()
    } else {
        
    }
    
})
//  --- Main Program Loop (Runs forever, but no longer redraws static background) ---
//  Start the forever loop
basic.forever(function on_forever2() {
    if (game.isGameOver()) {
        return
    }
    
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
    game.addScore(1)
    wall1.change(LedSpriteProperty.X, 5)
})

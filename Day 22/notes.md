# PONG LOGIC BREAKDOWN

# Classes

## Paddles

### Two instances of paddles. move_up / move_down methods key presses

## Ball

### Moves side to side, if paddlepos < 10 then reverse heading direction. Bounce off floors

## Stage

### If ball y_pos > 300 then player1 scores else < -300 player2 scores

## Scoreboard

### Updates each time ball passes x value by each player

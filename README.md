# B-Ball-Bash
https://code.thumby.us/

A small game made for the Thumby Console (Pi RP2040), written in MicroPython. 

The objective of the game is to hit the ball at the optimal position on the bat. Each hit can either be "Great", "Good", or a "Miss" and the score is denoted by the legend in the bottom right corner. A or B hit the ball.

The game itself is run entirely in a while loop, but I plan on making the code more modular. The game logic itself is just a simple statemachine. For stability purposes the game runs at 40 FPS to account for potential slowdown due to the statemachine logic, as well as the delay for sprite drawing. 

The pixel art was also done by me, but the text is included as a system function. 

The ball's throw is randomized using a formula that creates a curve that ends at the randomized value on the x-axis, and starts at a semi-random value on the y-axis. 

The ball can be hit, and is redirected to fly off screen, then and respawns when off screen.
Demonstration using Thumby emulator:
![bballbash_thumby](https://github.com/cscrosati98/B-Ball-Bash/assets/93940260/e2cc163c-eafe-45b1-9bab-0f0c268221d4)

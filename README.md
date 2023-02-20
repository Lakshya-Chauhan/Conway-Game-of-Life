<h1 align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Game_of_life_blinker.gif" height=35 width=35>
 Conway's Game of Life <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Game_of_life_blinker.gif" height=35 width=35></h1>
 
 ... is a cellular automaton devised by Mathematician John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
 
 <br>
 
<img align="right" src="https://user-images.githubusercontent.com/97667653/220025907-d10b997c-e9db-47d1-9e43-256edf5afbdd.png">

## Rules

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, (in this project a 60 x 80 grid of square cells) each of which is in one of two possible states, live `(1)` or dead `(0)` (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time _(or simply generation)_ , the following transitions occur:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

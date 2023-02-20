<h1 align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Game_of_life_blinker.gif" height=35 width=35>
 Conway's Game of Life <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Game_of_life_blinker.gif" height=35 width=35></h1>
 
 ... is a cellular automaton devised by Mathematician John Conway. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
 
 <br>
 
<img align="right" src="https://user-images.githubusercontent.com/97667653/220025907-d10b997c-e9db-47d1-9e43-256edf5afbdd.png">

## Rules 📝

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, (in this project a 60 x 80 grid of square cells) each of which is in one of two possible states, live `(1)` or dead `(0)` (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time _(or simply generation)_ , the following transitions occur:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## Implementation in Python

Following functions make up the whole game in Python:

#### `neighbours_count()`

It counts the number of neighbours a specific cell has, and returns it. 

#### `check_next_state()`

It decides whether a specific cell *(either dead or alive)* survives the next **generation**, on the basis of the number of its neighbours surrounding it.

#### `next_gen()`

It creates a new generation by taking an old generation and generating a new one on the basis of the above rules.

#### `construct_gen()`

It constructs a new, empty generation *i.e* it creates a generation of the mentioned size, with all cells being dead.

#### `main()`

Main body of the game, its functionings are below:

Upon running, a black grid of cells (squares) appears.
- On left clicking a square, it turns into a live cell.
- On right clicking a square, it turns into a dead cell.

<hr>

Instead of mere white squares representing live cells, the following color coding has been used:
- If the cell survives for the next 3 generations, **consecutively**, its color is displayed as `BLUE`.
- If the cell survives for the next 2 generations, **consecutively**, its color is displayed as `PEACH`.
- If the cell survives the 1st generation, dies the second generation, and turns alive the 3rd generation, its color is displayed as `GREEN`.
- If the cell survives only 1 generation, its color is displayed as `RED`.
- Elsewise if the cell is dead, its color is displayed `BLACK`.

> A prerequisite to run the program is to install *pygame* module. 

> Write the command `pip install pygame` in the terminal, to install the module and use it.

# The Power of Colouring

An interactive exposition on one small idea: colour a problem in, count the colours, and see what falls out.
It starts with a tiling puzzle and ends at two open problems, with a live figure for every step. Reading time is about 15 minutes.

By Tanav Gupta, for the Vedanta Ganita Samanwaya (VGS) exploratory phase, 2026.

## What is inside

| Section | Idea | Live figure |
| --- | --- | --- |
| A puzzle with no way in | Diagonal colouring of a 10 × 10 board | Place strips, switch colourings |
| The oldest trick on the board | Mutilated chessboard | Remove squares; the page finds a tiling |
| Where counting goes blind | Balanced colours, still no tiling | Free play |
| A knight has two colours | Parity | Move a knight |
| Does my trick always work? | Strips of any length on any board | Sliders |
| Rectangles with a whole-number side | Half-unit chessboard | Sliding rectangle |
| Necklaces | Fermat's little theorem | Bead groups |
| Guarding a gallery | Fisk's three-colour proof | Triangulate, colour, post guards |
| Six people at a party | Ramsey's theorem | Colour links, exhaustive check |
| Colouring by coin flip | Erdős's probabilistic method | Random colourings |
| A triangle that must have a rainbow | Sperner's lemma and fair rent | Recolour dots, see the walks |
| Colouring you already do | Graph colouring | Exam timetable |
| Where nobody knows the answer | R(5,5) and the colouring of the plane | Seven-colour tiling, Moser spindle |

## Files

```
index.html        the whole page: text, design and every figure, in one file
check_claims.py   checks every number quoted on the page
```
Clicking `index.html` in the file list only shows its code. To see the page download `index.html` and open it in any browser (Chrome, Safari, Firefox).

## Check the numbers

```
python3 check_claims.py
```

## How this was made

The starting point, the diagonal colouring of grid problems, comes from my own olympiad practice, and I described it in my application to this camp. To turn it into this page I worked with Claude, an AI model made by Anthropic. Claude helped me survey the literature, suggested several of the problems, and wrote the code for the interactive figures. Every number on the page was checked by a program, `check_claims.py`. I tried to include every colouring problem that I once stumbled upon, or in which colouring is applied beautifully.


